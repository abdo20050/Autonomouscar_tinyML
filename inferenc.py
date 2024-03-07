import cv2
import numpy as np

imagenet_labels = ['idle', 'left', 'right']
# read converted .onnx model with OpenCV API
opencv_net = cv2.dnn.readNetFromONNX("./model/inferencEng.onnx")
# read the image
def inference_img(inputImg):
    # input_img = cv2.imread(f'dataset/{test_label}/{test_label}0200.jpg', cv2.IMREAD_COLOR)
    input_img = inputImg.astype(np.float32)
    
    input_img = cv2.resize(input_img, (600, 600))
    
    # define preprocess parameters
    mean = np.array([0.485, 0.456, 0.406]) * 255.0
    scale = 1 / 255.0
    std = [0.229, 0.224, 0.225]
    
    # prepare input blob to fit the model input:
    # 1. subtract mean
    # 2. scale to set pixel values from 0 to 1
    input_blob = cv2.dnn.blobFromImage(
        image=input_img,
        scalefactor=scale,
        size=(224, 224),  # img target size
        mean=mean,
        swapRB=True,  # BGR -> RGB
        crop=True  # center crop
    )
    # 3. divide by std
    input_blob[0] /= np.asarray(std, dtype=np.float32).reshape(3, 1, 1)

    # set OpenCV DNN input
    opencv_net.setInput(input_blob)
    
    # OpenCV DNN inference
    out = opencv_net.forward()
    
    return out
    # get the predicted class ID
    # imagenet_class_id = np.argmax(out)
    
    # # get confidence
    # confidence = out[0][imagenet_class_id]
    # print("* class ID: {}, label: {}".format(imagenet_class_id, imagenet_labels[imagenet_class_id]))
    # print("* confidence: {:.4f}".format(confidence))

if __name__ == '__main__':
    test_label = 'right'
    input_img = cv2.imread(f'dataset/{test_label}/{test_label}0200.jpg', cv2.IMREAD_COLOR)
    out = inference_img(input_img)
    print(np.array(out))
    imagenet_class_id = np.argmax(out)
    # get confidence
    confidence = out[0][imagenet_class_id]
    print("* class ID: {}, label: {}".format(imagenet_class_id, imagenet_labels[imagenet_class_id]))
    print("* confidence: {:.4f}".format(confidence))
import inferenc
from inferenc import inference_img, cv2, np
from picamera2 import Picamera2
import os
import atexit
takedir = ""
def creat_take_dir(directory):
    count = 0
    for root, dirs, files in os.walk(directory):
        # print(dirs)
        for dir in dirs:
            if 'take' in dir:
                count += 1
    dir_name = directory+f"/take{count}/"
    os.makedirs(dir_name)
    return dir_name

def convert_images_to_video(image_folder, video_name, fps):
    images = [img for img in os.listdir(image_folder) if img.endswith(".png") or img.endswith(".jpg")]
    # Sort the images by name
    images.sort()

    frame = cv2.imread(os.path.join(image_folder, images[0]))
    height, width, layers = frame.shape

    video = cv2.VideoWriter(video_name, cv2.VideoWriter_fourcc(*'mp4v'), fps, (width,height))

    for image in images:
        video.write(cv2.imread(os.path.join(image_folder, image)))
        # os.remove(os.path.join(image_folder, image))

    cv2.destroyAllWindows()
    video.release()

def exit_handler():
    print("Terminat!")
    convert_images_to_video(takedir,takedir+'vid.mp4',30)

atexit.register(exit_handler)

# Grab images as numpy arrays and leave everything else to OpenCV.
labels = ['idle', 'left', 'right']
cv2.startWindowThread()
picam2 = Picamera2()
picam2.configure(picam2.create_preview_configuration(main={"format":"RGB888","size": (600, 600)}))
picam2.start()
i = 0
takedir = creat_take_dir('./vidStream')
while True:
    im = picam2.capture_array()
    out = inference_img(im)
    id = np.argmax(out)
    pred = labels[id]
    print(pred)
    cv2.putText(im,f"Prediction: {pred}",org = (5,5),fontFace= cv2.FONT_HERSHEY_SIMPLEX,fontScale = 1 , color=(0,0,255))
    img_name = str(i)
    img_name = img_name.zfill(len(img_name)+1)
    cv2.imwrite(takedir+f"/{img_name}.jpg",im)
    i += 1
    # cv2.imshow("Camera", im)
    cv2.waitKey(1)

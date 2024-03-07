import inferenc
from inferenc import inference_img, cv2, np
from picamera2 import Picamera2

# Grab images as numpy arrays and leave everything else to OpenCV.
labels = ['idle', 'left', 'right']
cv2.startWindowThread()
picam2 = Picamera2()
picam2.configure(picam2.create_preview_configuration(main={"format":"RGB888","size": (600, 600)}))
picam2.start()
while True:
    im = picam2.capture_array()
    out = inference_img(im)
    id = np.argmax(out)
    print(labels[id])
    # cv2.imshow("Camera", im)
    cv2.waitKey(1)
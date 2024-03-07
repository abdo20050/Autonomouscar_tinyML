from inferenc import inference_img, cv2, np
from picamera2 import Picamera2
import os
import shutil
import re
import atexit
from gamepad import XboxController,ser
import time

vid_dir = './vids_AIdriver/'
joy = XboxController()
isPaused = False
fps = 15
def motors_switch(state:bool):
    msg = bytearray([ord('M'),state])
    ser.write(msg)
def led_switch(state:bool):
    msg = bytearray([ord('L'),state])
    ser.write(msg)
def resetArduion():
    ser.write(b'R0')

def drive(input):
    _type = ord('d')
    val = 0
    if input == 0:#forward
        val=0
    elif input == 1:#turn left
        val=1
    elif input == 2:#turn right
        val =3
    msg = bytearray([_type,val])
    ser.write(msg) 
def getState():
    state = ''
    if joy.LeftDPad:
        state = 'left'
    elif joy.RightDPad:
        state = 'right'
    else:
        state = 'idle'
    return state
def natural_sort_key(s, _nsre=re.compile('([0-9]+)')):
    return [
        int(text)
        if text.isdigit() else text.lower()
        for text in _nsre.split(s)]

def creat_take_dir(directory):
    count = 0
    for root, dirs, files in os.walk(directory):
        # print(dirs)
        for file in files:
            if 'take' in file:
                count += 1
    vidname = directory+f"/take{count}.mp4"
    # os.makedirs(dir_name)
    return vidname

def convert_images_to_video(image_folder, video_name, fps):
    images = [img for img in os.listdir(image_folder) if img.endswith(".png") or img.endswith(".jpg")]
    # Sort the images by name
    images.sort()

    frame = cv2.imread(os.path.join(image_folder, images[0]))
    height, width, layers = frame.shape

    video = cv2.VideoWriter(video_name, cv2.VideoWriter_fourcc(*'mp4v'), fps, (width,height))
    sorted_images = sorted(images, key=natural_sort_key)
    for image in sorted_images:
        video.write(cv2.imread(os.path.join(image_folder, image)))
        os.remove(os.path.join(image_folder, image))

    cv2.destroyAllWindows()
    video.release()
def check_human():
    output = joy.LeftDPad or joy.RightDPad or joy.UpDPad or joy.DownDPad
    return output
def exit_handler():
    print("Terminat!")
    resetArduion()
    picam2.close()
    convert_images_to_video(vid_dir+'/Tmp',vid_name,fps)
    shutil.rmtree(vid_dir+'/Tmp')

atexit.register(exit_handler)

# Grab images as numpy arrays and leave everything else to OpenCV.
labels = ['idle', 'left', 'right']
cv2.startWindowThread()
picam2 = Picamera2()
picam2.configure(picam2.create_preview_configuration(main={"format":"RGB888","size": (600, 600)}))
picam2.start()
i = 0
vid_name = creat_take_dir(vid_dir)
try:
    os.makedirs(vid_dir+'/Tmp')
except:
    pass

print("Press START to start record!")
while(not joy.Start): pass
led_switch(1)
motors_switch(1)
print("Go!")
time.sleep(0.5)
print("Press Y to pause dataRecording")

while True:
    if joy.Start:
        break
    if joy.Y:
        if not isPaused:
            print("pause!")
            motors_switch(0)
            led_switch(0)
            isPaused = True
        else:
            print("Start Recording!")
            led_switch(1)
            motors_switch(1)
            isPaused = False
        while(joy.Y): pass
    if not isPaused: 
        im = picam2.capture_array()
        out = inference_img(im)
        id = np.argmax(out)
        if(not check_human()):
            drive(id)
        pred = labels[id]
        conf = out[0][id]
        real = getState()
        print(pred)
        cv2.putText(im,f"AI: {pred}, confidence: {round(conf*100,1)}%",org = (10,30),fontFace= cv2.FONT_HERSHEY_SIMPLEX,fontScale = 1 , color=(0,0,255),thickness=2)
        cv2.putText(im,f"Human: {real}",org = (10,60),fontFace= cv2.FONT_HERSHEY_SIMPLEX,fontScale = 1 , color=(0,0,255),thickness=2)
        img_name = str(i)
        cv2.imwrite(vid_dir+f"/Tmp/{img_name}.jpg",im)
        i += 1
    # cv2.imshow("Camera", im)
    cv2.waitKey(1)

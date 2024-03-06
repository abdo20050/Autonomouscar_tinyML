from gamepad import XboxController,ser
import os
import json
import cv2
import atexit


#!/usr/bin/python3

# Capture a JPEG while still running in the preview mode. When you
# capture to a file, the return value is the metadata for that image.

import time

from picamera2 import Picamera2, Preview
joy = XboxController()
picam2 = Picamera2()
data = None
try: 
    with open("./dataset/data.json", "r") as f:
        data = json.load(f)
except:
    pass
if data:
    statesCount = data
    print(statesCount)
else:
    statesCount = {'idle':0,'left':0,'right':0}
    print(statesCount)
# while 1: pass
def motors_switch(state:bool):
    msg = bytearray([ord('M'),state])
    ser.write(msg)
def led_switch(state:bool):
    msg = bytearray([ord('L'),state])
    ser.write(msg)
def resetArduion():
    ser.write(b'R0')
def getState():
    if joy.LeftDPad:
        state = 'left'
        statesCount[state]+=1
        return state
    elif joy.RightDPad:
        state = 'right'
        statesCount[state]+=1
        return state
    else:
        state = 'idle'
        statesCount[state]+=1
        return state
    
def exit_handler():
    print("Terminat!")
    resetArduion()
    print(statesCount)
    picam2.close()
    with open('./dataset/data.json', 'w') as f:
        json.dump(statesCount, f)
    
atexit.register(exit_handler)

isPaused = False
preview_config = picam2.create_preview_configuration(main={"size": (600, 600)})
picam2.configure(preview_config)

# picam2.start_preview(Preview.QTGL)
picam2.start()
# time.sleep(2)
prevTime = time.time()
i = 0
# while time.time() - prevTime <= 5:
print("Press START to start record!")
while(not joy.Start): pass
led_switch(1)
print("Go!")
time.sleep(0.5)
print("Press Y to pause dataRecording")
while 1:
    if joy.Start:
        break
    if joy.Y:
        if not isPaused:
            print("pause!")
            motors_switch(0)
            time.sleep(0.1)
            led_switch(0)
            isPaused = True
        else:
            print("Start Recording!")
            led_switch(1)
            isPaused = False
        while(joy.Y): pass
    if not isPaused:    
        state = getState()
        img_name = str(statesCount[state]-1)
        img_name = img_name.zfill(len(img_name)+1)
        directory = f"./dataset/{state}/{img_name}.jpg"
        metadata = picam2.capture_file(directory)
        # print(metadata)
        i = i+1
# print(f"fps[{i/5}]")

# exit_handler()

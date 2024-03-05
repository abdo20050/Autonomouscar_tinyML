from gamepad import XboxController
import os
import json
import cv2
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
    
isPaused = False
preview_config = picam2.create_preview_configuration(main={"size": (600, 600)})
picam2.configure(preview_config)

# picam2.start_preview(Preview.QTGL)
picam2.start()
# time.sleep(2)
prevTime = time.time()
i = 0
# while time.time() - prevTime <= 5:
print("press A to start!")
while(not joy.A): pass
print("Go!")

while 1:
    if joy.Start:
        break
    if joy.Y:
        if not isPaused:
            print("pause!")
            isPaused = True
        else:
            print("continue!")
            isPaused = False
        while(joy.Y): pass
    if not isPaused:    
        state = getState()
        directory = f"./dataset/{state}/{str(statesCount[state]-1).zfill(5)}.jpg"
        metadata = picam2.capture_file(directory)
        # print(metadata)
        i = i+1
# print(f"fps[{i/5}]")
print("Terminat!")
print(statesCount)
with open('./dataset/data.json', 'w') as f:
    json.dump(statesCount, f)

picam2.close()


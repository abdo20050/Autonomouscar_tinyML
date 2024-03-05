import gamepad
import cv2
#!/usr/bin/python3

# Capture a JPEG while still running in the preview mode. When you
# capture to a file, the return value is the metadata for that image.

import time

from picamera2 import Picamera2, Preview

picam2 = Picamera2()

preview_config = picam2.create_preview_configuration(main={"size": (600, 600)})
picam2.configure(preview_config)

# picam2.start_preview(Preview.QTGL)

picam2.start()
# time.sleep(2)
prevTime = time.time()
i = 0
while time.time() - prevTime <= 5:
    num = str(i).zfill(4)
    metadata = picam2.capture_file("./dataset/"+num+".jpg")
    # print(metadata)
    i = i+1
print(f"fps[{i/5}]")
picam2.close()
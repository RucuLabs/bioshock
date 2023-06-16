import subprocess
import os
import time

# detect: void -> bool
# indicates if usb webcam is connected to the rpi
def detect():
    try:
        output = subprocess.getoutput("lsusb")
        webcam = "webcam" in output.lower()
        print(f"Webcam: Detected {webcam}")
        return webcam
    except:
        print("Webcam: Error detecting webcam")
        return False

# take_picture: path(str) -> void
# takes a picture from the usb webcam and saves it to path
# uses fswebcam
def take_picture(path, filename):
    filename = filename + ".jpg"
    command = "fswebcam -r 1280x720 --no-banner " + os.path.join(path, filename)
    try:
        os.system(command)
        print(f"Webcam: Taking picture {filename}")
    except:
        print(f"Webcam: Error taking picture {filename}")

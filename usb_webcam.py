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
def take_picture(path):
    filename = time.strftime("%Y%m%d-%H%M%S") + ".jpg"
    command = "fswebcam -r 1280x720 --no-banner " + os.path.join(directory, filename)
    try:
        os.system(command)
        print(f"Webcam: Taking picture {filename}")
    except:
        print(f"Webcam: Error taking picture {filename}")

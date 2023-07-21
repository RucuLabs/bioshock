import subprocess
import os
import time

RESOLUTIONS_16_9 = {
    "360p": "640x360",
    "480p": "854x480",
    "540p": "960x540",
    "576p": "1024x576",
    "720p": "1280x720",
    "768p": "1366x768",
    "900p": "1600x900",
    "FullHD": "1920x1080",
    "1440p": "2560x1440",
    "4K": "3840x2160"
}

# detect: void -> list / false
# indicates if videocams are connected to the rpi
def detect():
    try:
        output = subprocess.getoutput("ls /dev/video[0-9]")
        output = output.split()
        cams_n = len(output)
        if cams_n == 0:
            print("No cams detected")
            return False
        else:
            print(f"{cams_n} cam(s) detected.")
            return output
    except:
        print("Error detecting cams")
        return False

# take_picture: path(str) resolution(str) cam_name(str) filename -> void
# takes a picture from the usb webcam and saves it to path
# uses fswebcam
def take_picture(path, resolution, cam_name, filename):
    cam_number = cam_name[-1]
    filename = f"cam{cam_number}-{filename}.jpg"
    command = f"fswebcam -d {cam_name} -r {resolution} --no-banner " + os.path.join(path, filename)
    try:
        os.system(command)
        print(f"Webcam: Taking picture on cam{cam_number}: {filename}")
    except:
        print(f"Webcam: Error taking picture on cam{cam_number}: {filename}")

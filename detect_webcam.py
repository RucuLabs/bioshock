import subprocess

def detect_webcam():
    output = subprocess.getoutput("lsusb")

    if "webcam" in output.lower():
        print("Webcam detected")

    else:
        print("No webcam detected")

detect_webcam()

import os, subprocess

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

# take_picture: path(str) resolution(str) cam_name(str) filename(str) -> void
# takes a picture (fswebcam) from the usb webcam and saves it to path
def take_picture(path, resolution, cam_name, filename):
    cam_number = cam_name[-1]
    filename = f"cam{cam_number}-{filename}.jpg"
    command = f"fswebcam -d {cam_name} -r {resolution} --no-banner " + os.path.join(path, filename)
    try:
        print(command)
        os.system(command)
        print(f"Webcam: Taking picture on cam{cam_number}: {filename}")
    except:
        print(f"Webcam: Error taking picture on cam{cam_number}: {filename}")

# take_picture: path(str) resolution(str) cam_name(str) filename(str) -> void
# takes a picture (fswebcam) from the usb webcam and saves it to path
def take_picture_test(path, resolution, cam_name, filename):
    cam_number = cam_name[-1]
    filename = f"{filename}.jpg"
    command = f"fswebcam -d {cam_name} -r {resolution} --no-banner " + os.path.join(path, filename)
    try:
        print(command)
        os.system(command)
        print(f"Webcam: Taking picture on cam{cam_number}: {filename}")
    except:
        print(f"Webcam: Error taking picture on cam{cam_number}: {filename}")
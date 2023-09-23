import os, subprocess
import cv2

MAX_CAM_PORTS = 4

def list_ports():
    """
    Test the ports and returns a tuple with the available ports and the ones that are working.
    """
    non_working_ports = []
    dev_port = 0
    working_ports = []
    available_ports = []
    supported_resolutions = []
    while len(non_working_ports) < MAX_CAM_PORTS:
        camera = cv2.VideoCapture(dev_port)
        if not camera.isOpened():
            non_working_ports.append(dev_port)
            print("Port %s is not working." %dev_port)
        else:
            is_reading, img = camera.read()
            w = camera.get(3)
            h = camera.get(4)
            if is_reading:
                print("Port %s is working and reads images (%s x %s)" %(dev_port,h,w))
                working_ports.append(dev_port)
                supported_resolutions.append(f"{int(w)}x{int(h)}")
            else:
                print("Port %s for camera ( %s x %s) is present but does not reads." %(dev_port,h,w))
                available_ports.append(dev_port)
        dev_port +=1
    return available_ports, working_ports, non_working_ports, supported_resolutions

def capture_images(working_ports, pictures_path, picture_name):

    for port in working_ports:

        port_path = f"{pictures_path}/cam{str(port)}"
        os.makedirs(port_path, exist_ok=True)

        camera = cv2.VideoCapture(port)
        # camera.set(cv2.CAP_PROP_FRAME_WIDTH, w)
        # camera.set(cv2.CAP_PROP_FRAME_HEIGHT, h)

        if not camera.isOpened():
            print(f"Can't open camera at /video{str(port)}")
            continue

        ret, frame = camera.read()
        if ret:
            picture_file_name = f"{picture_name}.jpg"
            image_path = os.path.join(port_path, picture_file_name)
            cv2.imwrite(image_path, frame)
            print(f"Captured image: {image_path}")
        else:
            print(f"Can't take picture at /video{str(port)}")

        camera.release()


### DEPRECATED

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
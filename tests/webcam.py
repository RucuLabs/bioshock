import cv2
import os

    
def list_ports():
    """
    Test the ports and returns a tuple with the available ports and the ones that are working.
    """
    non_working_ports = []
    dev_port = 0
    working_ports = []
    available_ports = []
    while len(non_working_ports) < 10: # if there are more than 5 non working ports stop the testing. 
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
            else:
                print("Port %s for camera ( %s x %s) is present but does not reads." %(dev_port,h,w))
                available_ports.append(dev_port)
        dev_port +=1
    return available_ports,working_ports,non_working_ports

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
            picture_name = f"{picture_name}.jpg"
            image_path = os.path.join(port_path, picture_name)
            cv2.imwrite(image_path, frame)
            print(f"Captured image: {image_path}")
        else:
            print(f"Can't take picture at /video{str(port)}")

        camera.release()

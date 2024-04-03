import cv2
import os

def list_ports():
    """
    Test the ports and return a tuple with the available ports and the ones that are working.
    """
    non_working_ports = []
    working_ports = []
    available_ports = []

    for dev_port in range(10):
        camera = cv2.VideoCapture(dev_port)
        if not camera.isOpened():
            non_working_ports.append(dev_port)
            print("Port %s is not working." % dev_port)
        else:
            is_reading, _, _ = camera.read()
            if is_reading:
                print(f"Port {dev_port} is working.")
                working_ports.append(dev_port)
            else:
                print(f"Port {dev_port} is present but does not read.")
                available_ports.append(dev_port)
            camera.release()

    return available_ports, working_ports, non_working_ports

def capture_images(working_ports, pictures_path, picture_name):
    for port in working_ports:
        port_path = f"{pictures_path}/cam{port}"
        os.makedirs(port_path, exist_ok=True)

        camera = cv2.VideoCapture(port)
        if not camera.isOpened():
            print(f"Can't open camera at /video{port}")
            continue

        ret, frame = camera.read()
        if ret:
            picture_name = f"{picture_name}-{port}.jpg"
            image_path = os.path.join(port_path, picture_name)
            cv2.imwrite(image_path, frame)
            print(f"Captured image: {image_path}")
        else:
            print(f"Can't take picture at /video{port}")

        camera.release()

available_ports, working_ports, non_working_ports = list_ports()
print("Available Ports:", available_ports)
print("Working Ports:", working_ports)
print("Non-working Ports:", non_working_ports)

pictures_path = "pictures"
picture_name = "test"
capture_images(working_ports, pictures_path, picture_name)

import picamera
import time

def take_picture(path):
    camera = picamera.PiCamera()
    try:
        camera.resolution = (1280, 720)
        camera.framerate = 30
        camera.start_preview()
        time.sleep(2)
        camera.capture(path)
        print("Imagen capturada correctamente.")

    finally:
        camera.stop_preview()
        camera.close()

NUM_PHOTOS = 10
INTERVAL = 5

for i in range(NUM_PHOTOS):
    path = f"imagen_{i+1}.jpg"
    take_picture(path)
    time.sleep(INTERVAL)


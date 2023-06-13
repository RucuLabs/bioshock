import usb_webcam
import sys
import time

BANNER = """
oooooooooo.   o8o             .oooooo..o oooo                            oooo
`888'   `Y8b  `"'            d8P'    `Y8 `888                            `888
 888     888 oooo   .ooooo.  Y88bo.       888 .oo.    .ooooo.   .ooooo.   888  oooo
 888oooo888' `888  d88' `88b  `"Y8888o.   888P"Y88b  d88' `88b d88' `"Y8  888 .8P'
 888    `88b  888  888   888      `"Y88b  888   888  888   888 888        888888.
 888    .88P  888  888   888 oo     .d8P  888   888  888   888 888   .o8  888 `88b.
o888bood8P'  o888o `Y8bod8P' 8""88888P'  o888o o888o `Y8bod8P' `Y8bod8P' o888o o888o


                                                                                    """
print(BANNER)

if not usb_webcam.detect():
    print("Exiting")
    sys.exit(0)

directory = "./usb_pictures/"
num_photos = int(input("Indica el número de fotos: "))
interval = int(input("Indica el intervalo (segundos): "))

print("Iniciando captura de fotos")
for i in range(num_photos):
    usb_webcam.take_picture(directory)
    time.sleep(interval)

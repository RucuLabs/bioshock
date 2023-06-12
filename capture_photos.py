import os
import time

# Directorio donde se guardarán las fotos
directory = "./usb_pictures/"

# Número de fotos a tomar
num_photos = 10

# Intervalo entre cada foto (en segundos)
interval = 5

# Captura de fotos
for i in range(num_photos):
    # Nombre de archivo con la fecha y hora actual
    filename = time.strftime("%Y%m%d-%H%M%S") + ".jpg"

    # Comando para capturar la foto utilizando fswebcam
    command = "fswebcam -r 1280x720 --no-banner " + os.path.join(directory, filename)

    # Ejecutar el comando
    os.system(command)

    # Esperar el intervalo antes de tomar la siguiente foto
    time.sleep(interval)

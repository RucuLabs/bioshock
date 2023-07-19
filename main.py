import usb_webcam
import sys
import time
import csv
import os
from dumb import BANNER
import adafruit_dht
import ds18x20
import board

print(BANNER)

cams = usb_webcam.detect()
if not cams:
    print("Exiting")
    sys.exit(0)

# Initial the dht device, with data pin connected to:
AM2302 = adafruit_dht.DHT22(board.D18)
DS18X20_id = '28-3c01d607a2d3'

while True:
    directory = input("Ingresa el nombre del proyecto: ")
    if not os.path.exists(directory):
        try:
            os.mkdir(directory)
            os.mkdir(directory+'/pictures')
            break
        except:
            print("Error creando directorio, intenta de nuevo")
            continue
    print(f"{directory} ya existe, ocupa otro nombre")

while True:
    try:
        num_photos = int(input("Indica el número de registros: "))
        interval = int(input("Indica el intervalo (segundos): "))
        if num_photos >= 0 and interval >= 0:
            break
    except:
        print("Error de input, intenta de nuevo")
        continue
    print("Ingresa un número de registros y tiempo de intervalo válidos")

HEADERS = ['id', 'time', 'temperatura', 'humedad', 'temp_interna', 'foto']
FILE_NAME = f'{directory}/data.csv'
RESOLUTION = "1280x720"

print(f"Proyecto {directory}")
print("Iniciando monitoreo")

with open(FILE_NAME, 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(HEADERS)
    for i in range(num_photos):
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        for cam in cams:
            usb_webcam.take_picture(directory+'/pictures/', RESOLUTION, cam, str(i))
        humidity, temperature = AM2302.humidty, AM2302.temperature
        inner_temperature = '{:.3f}'.format(ds18x20.gettemp(id)/float(1000))
        row = [i, timestamp, temperature, humidity, inner_temperature, str(i)+'.jpg']
        writer.writerow(row)
        time.sleep(interval)

print("Monitoreo terminado")
sys.exit(1)

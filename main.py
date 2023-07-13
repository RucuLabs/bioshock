import usb_webcam
import sys
import time
import csv
import Adafruit_DHT
import os
from dumb import BANNER
from w1thermsensor import W1ThermSensor

print(BANNER)
if not usb_webcam.detect():
    print("Exiting")
    sys.exit(0)

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

SENSOR_1 = Adafruit_DHT.AM2302
SENSOR_2 = W1ThermSensor()
SENSOR_1_PIN = 5
HEADERS = ['id', 'time', 'temperatura', 'humedad', 'temp_interna', 'foto']
FILE_NAME = f'{directory}/data.csv'

print(f"Proyecto {directory}")
print("Iniciando monitoreo")

with open(FILE_NAME, 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(HEADERS)
    for i in range(num_photos):
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        usb_webcam.take_picture(directory+'/pictures/', str(i))
        humidity, temperature = Adafruit_DHT.read_retry(SENSOR_1, SENSOR_1_PIN)
        inner_temperature = SENSOR_2.get_temperature()
        row = [i, timestamp, temperature, humidity, inner_temperature, str(i)+'.jpg']
        writer.writerow(row)
        time.sleep(interval)

print("Monitoreo terminado")
sys.exit(1)

#!/usr/bin/python

import time
import Adafruit_DHT
import csv
from w1thermsensor import W1ThermSensor
from os.path import exists

#Revisar documentación para ver sensores soportados por adafruit
sensor = Adafruit_DHT.AM2302
sensor2 = W1ThermSensor()
#pin de data del sensor
pin = 4
#intervalo de tiempo entre registro
interval = 5
n_regitros = 10


log_exists = exists('data/sensor_logs.csv')
if (not log_exists):

    header = ['timestamp', 'temperature', 'humidity']
    with open('data/sensor_logs.csv', 'w', encoding='UTF-8') as f:
        writer = csv.writer(f)
        writer.writerow(header)

for i in n_regitros:

    timestamp = time.strftime("%Y%m%d-%H%M%S")
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    temp2 = sensor2.get_temperature()
    print(temp2)
    data = [timestamp, temperature, humidity]
    with open('data/sensor_logs.csv', 'w', encoding='UTF-8') as f:
        writer = csv.writer(f)
        writer.writerow(data)
    time.sleep(interval)
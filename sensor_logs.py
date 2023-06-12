#!/usr/bin/python

import time
import Adafruit_DHT

#Revisar documentación para ver sensores soportados por adafruit
sensor = Adafruit_DHT.AM2302
#pin de data del sensor
pin = 4

#imprime humedad y temp
while True:
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    print(humidity, temperature)
    time.sleep(3)


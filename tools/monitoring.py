import tools.ds18x20 as ds18x20
import tools.cameras as cameras
import csv, time
import Adafruit_DHT
import os

HEADERS = ['iteration', 
            'time', 
            'temperature', 
            'humidity', 
            'inner_temperature']

DHT_PIN = 18
DHT_SENSOR = Adafruit_DHT.DHT22
# DS18X20_id = '28-3c01d607a2d3'

def start_monitoring(monitoring_path, working_ports, interval):
    data_path = f'{monitoring_path}/data.csv'
    pictures_path = f'{monitoring_path}/pictures'
    
    # open the data csv
    with open(data_path, 'w', newline='') as data_file:
        writer = csv.writer(data_file)
        writer.writerow(HEADERS)

        i = 0
        
        # create a registry for the requested ammount of iterations
        while True:

            timestamp = time.strftime("%Y%m%d-%H%M%S")
            
            cameras.capture_images(working_ports=working_ports, pictures_path=pictures_path, picture_name=str(i))
            
            # ADD SENSORS

            humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
            inner_temperature = '{:.3f}'.format(ds18x20.gettemp()/float(1000))
            # humidity = 'humidity'
            # temperature = 'temperature'
            # inner_temperature = 'inner_temperature'

            # write the registry
            row = [i, timestamp, temperature, humidity, inner_temperature]
            writer.writerow(row)

            i += 1

            # wait for next iteration
            time.sleep(interval)

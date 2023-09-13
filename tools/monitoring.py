import tools.ds18x20 as ds18x20
import tools.cameras as cameras
import csv, time
# import board
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

def start_monitoring(monitoring_name, monitoring_path, cams, resolution, num_photos, interval):
    data_path = f'{monitoring_path}/data.csv'
    pictures_path = f'{monitoring_path}/pictures/'
    
    # create a folder for each camera (pictures)
    cam_names = []
    for cam in cams:
        cam_name = cam.split('/')[2]
        cam_names.append(cam_name)
        os.mkdir(f"{monitoring_path}/{cam_name}/")
    
    # open the data csv
    with open(data_path, 'w', newline='') as data_file:
        writer = csv.writer(data_file)
        writer.writerow(HEADERS)
        
        # create a registry for the requested ammount of iterations
        for i in range(num_photos):
            timestamp = time.strftime("%Y%m%d-%H%M%S")
            
            # take a picture on each available camera
            for idx, cam in enumerate(cams):
                cameras.take_picture(f"{monitoring_path}/{cam_names[idx]}/", resolution, cam, str(i))
            
            # ADD SENSORS

            humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
            # inner_temperature = '{:.3f}'.format(ds18x20.gettemp(DS18X20_id)/float(1000))
            # humidity = 'humidity'
            # temperature = 'temperature'
            inner_temperature = 'inner_temperature'

            # write the registry
            row = [i, timestamp, temperature, humidity, inner_temperature]
            writer.writerow(row)

            # wait for next iteration
            time.sleep(interval)

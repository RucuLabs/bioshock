import tools.ds18x20 as ds18x20
import tools.cameras as cameras
import csv, time
import Adafruit_DHT

HEADERS = ['iteration', 
            'time', 
            'temperature', 
            'humidity', 
            'inner_temperature',
            'inner_temperature2']

# DHT_PIN = 18
# DHT_SENSOR = Adafruit_DHT.DHT22
# DS18X20_id = '28-3c01d607a2d3'
DS18X20_ids = ds18x20.getTempSensors()

def monitoring_cycle(monitoring_path, working_ports, iteration):

    # paths for data mgmt
    data_path = f'{monitoring_path}/data.csv'
    pictures_path = f'{monitoring_path}/pictures'
    
    # take pictures
    cameras.capture_images(working_ports=working_ports, pictures_path=pictures_path, picture_name=iteration)
            
    # ADD SENSORS
    # humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
    inner_temperature = '{:.3f}'.format(ds18x20.gettemp()[0]/float(1000))
    inner_temperature2 = '{:.3f}'.format(ds18x20.gettemp()[1]/float(1000))
    
    humidity = '0'
    temperature = '0'
    # inner_temperature = '0'
    timestamp = time.strftime("%d%m%Y-%H%M%S")

    with open(data_path, mode='a', newline='', encoding='utf-8') as data_csv:
        
        writer_csv = csv.DictWriter(data_csv, fieldnames=HEADERS)
        
        if data_csv.tell() == 0:
            writer_csv.writeheader()
        
        row = { 'iteration' : iteration, 
                    'time' : timestamp, 
                    'temperature' : temperature, 
                    'humidity' : humidity, 
                    'inner_temperature' : inner_temperature,
                    'inner_temperature2' : inner_temperature2
        } 
        
        writer_csv.writerow(row)

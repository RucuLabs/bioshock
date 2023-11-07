import tools.ds18x20 as ds18x20
import tools.cameras as cameras
import csv, time
import Adafruit_DHT
import tools.stemma as stemma

HEADERS = ['iteration', 
            'time', 
            'temperature', 
            'humidity']
for i in range(len(ds18x20.gettemp())):
    HEADERS.append(f'in_temp_{i}')

# DHT_PIN = 18
# DHT_SENSOR = Adafruit_DHT.DHT22
DS18X20_ids = ds18x20.getTempSensors()

# Se intenta inicializar el sensor de humedad, deberia funcionar con blinka y siguiendo el esquema de conexion mostrado en 
# https://cdn-learn.adafruit.com/downloads/pdf/adafruit-stemma-soil-sensor-i2c-capacitive-moisture-sensor.pdf
# Si funciona descomentar inner_humidity para que haga lecturas. Tmbn lee temperatura con read_temp
try:
    # Si falla por address equivocada pasar como argumento a la clase, por default se tiene addr=0x36 que deberia ser 
    # la correcta si se sigue el esquema de conexion
    # Para ver la direccion hay que escanear las direcciones i2c de la raspi, deberia ser la unica q aparezca, Si no aparece... rezar.
    stemma = stemma.Stemma()
except Exception as e :
    print(e)

def monitoring_cycle(monitoring_path, working_ports, iteration):

    # paths for data mgmt
    data_path = f'{monitoring_path}/data.csv'
    pictures_path = f'{monitoring_path}/pictures'
    
    # take pictures
    cameras.capture_images(working_ports=working_ports, pictures_path=pictures_path, picture_name=iteration)
            
    # ADD SENSORS
    # humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)

    # ds13x20 sensosrs
    in_temps = []
    for i in range(len(ds18x20.gettemp())):
        in_temps.append('{:.3f}'.format(ds18x20.gettemp()[i]/float(1000)))
      
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
        } 
        for i in range(len(in_temps)):
            row[f'in_temp_{i}'] = in_temps[i]
        writer_csv.writerow(row)

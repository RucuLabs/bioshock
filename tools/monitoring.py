import tools.ds18x20
import board, csv, time

HEADERS = ['iteration', 'time', 'temperature', 'humidity', 'inner_temperature', 'picture_name']
AM2302 = adafruit_dht.DHT22(board.D18)
DS18X20_id = '28-3c01d607a2d3'

def start_monitoring(monitoring_name, monitoring_path, cams, resolution, num_photos, interval):
    data_path = f'{monitoring_path}/data.csv'
    pictures_path = f'{monitoring_path}/pictures/'
    for cam in cams:
        os.mkdir(f"{monitoring_path}/{cam}/")
    with open(data_path, 'w', newline='') as data_file:
        writer = csv.writer(data_file)
        writer.writerow(HEADERS)
        for i in range(num_photos):
            timestamp = time.strftime("%Y%m%d-%H%M%S")
            for cam in cams:
                cameras.take_picture(f"{monitoring_path}/{cam}/", resolution, cam, str(i))
            humidity, temperature = AM2302.humidity, AM2302.temperature
            inner_temperature = '{:.3f}'.format(ds18x20.gettemp(DS18X20_id)/float(1000))
            row = [i, timestamp, temperature, humidity, inner_temperature, str(i)+'.jpg']
            writer.writerow(row)
            time.sleep(interval)
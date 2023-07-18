import Adafruit_DHT
from w1thermsensor import W1ThermSensor

SENSOR_1 = Adafruit_DHT.AM2302
SENSOR_2 = W1ThermSensor()
SENSOR_1_PIN = 5

humidity, temperature = Adafruit_DHT.read_retry(SENSOR_1, SENSOR_1_PIN)
inner_temperature = SENSOR_2.get_temperature()

print(humidity, temperature, inner_temperature)
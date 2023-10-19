import board
from adafruit_seesaw.seesaw import Seesaw


class Stemma:
    def __init__(self, addr=0x36):
        self.i2c_bus = board.I2C()
        self.ss = Seesaw(self.i2c_bus, addr=addr)
    
    def read_temp(self):
        return self.ss.get_temp()
    
    def read_humidity(self):
        return self.ss.moisture_read()

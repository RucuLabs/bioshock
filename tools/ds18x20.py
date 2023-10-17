#!/usr/bin/python
import glob
import os
def gettemp():
  mytemp = ''
  base_dir = '/sys/bus/w1/devices/'
  # device_folder = glob.glob(base_dir + '28*')[0]
  temperatures = []
  for device_folder in glob.glob(base_dir + '28*'):
    device_file = device_folder + '/w1_slave'
    
    f = open(device_file, 'r')
    line = f.readline() # read 1st line
    crc = line.rsplit(' ',1)
    crc = crc[1].replace('\n', '')
    if crc=='YES':
      line = f.readline() # read 2nd line
      mytemp = line.rsplit('t=',1)
    else:
      mytemp = 123456789
    f.close()
    temperatures.append(int(mytemp[1]))

  return temperatures

def getTempSensors():
  sensors = []
  base_dir = '/sys/bus/w1/devices/'
  for filename in os.listdir(base_dir):
    if filename == 'w1_bus_master1':
      continue
    sensors.append(filename)
    return sensors

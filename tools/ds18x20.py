#!/usr/bin/python
import glob

def gettemp(id):
  mytemp = ''
  base_dir = '/sys/bus/w1/devices/'
  device_folder = glob.glob(base_dir + '28*')[0]
  device_file = device_folder + 'w1_slave'
  
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

  return int(mytemp[1])

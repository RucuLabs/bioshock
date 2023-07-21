#!/usr/bin/python
def gettemp(id):
  mytemp = ''
  filename = 'w1_slave'
  f = open('/sys/bus/w1/devices/' + str(id) + '/' + filename, 'r')
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
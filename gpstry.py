import serial
import time
a=0
while True:
	rcv=serial.Serial("/dev/ttyUSB0",9600,timeout=1)
	raw=rcv.readline()
	if '$GPVTG' in raw:
		print(raw)
	if '$GPGGA' in raw:
		a=a+1
		print(raw)
		print "iteration amount=",a	
		datas=raw.split(',')
		for i in range(0,len(datas)-1):
			print(datas[i])
			print('\r\n')
	time.sleep(1)


import serial
import time
a=0
while True:
	rcv=serial.Serial("/dev/ttyUSB0",9600,timeout=1)
	rawrcv=rcv.readline()
	if '$GPVTG' in rawrcv:
		print(rawrcv)
	if '$GPGGA' in rawrcv:
		a=a+1
		print(rawrcv)
		print "iteration amount=",a	
		datas=rawrcv.split(',')
		
			
	time.sleep(1)


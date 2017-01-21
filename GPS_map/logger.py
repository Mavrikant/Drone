#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
import serial
import sys, traceback


rcv=serial.Serial("/dev/ttyUSB0",9600,timeout=1)
rcv.flushInput()
time.sleep(1)
while(1):
	
	rawrcv=rcv.readline()
	if '$GPGGA' in rawrcv:
			rawinputs=rawrcv.split(",")
			print rawinputs
			if len(rawinputs[2])>0 and len(rawinputs[3])>0 :
				D1=str((rawinputs[2][0:2]))
				M1=str((rawinputs[2][2:9]))
				
				D2=str((rawinputs[4][0:3]))
				M2=str((rawinputs[4][3:10]))

				long=str(float(D1)+float(M1)/60)
				lat=str(float(D2)+float(M2)/60)
				saat = str((int(rawinputs[1][:2])+3)%24)
				dak = rawinputs[1][2:4]
				san = rawinputs[1][4:6]
			
				print lat
				print long
				with open("gps.txt", "w") as myfile:
					myfile.write(str(long)+","+str(lat)+","+saat+":"+dak+":"+san)
					
			else:
				with open("gps.txt", "w") as myfile:
					myfile.write("ERROR")

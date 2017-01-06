import RPi.GPIO as GPIO # always needed with RPi.GPIO  
from math import atan
import time
import curses
import serial
a=0
latinput=raw_input("Please enter latitude(dd):")
longinput=raw_input("Please enter longitude(dd):")
#init the curses screen
stdscr = curses.initscr()
curses.noecho()
#use cbreak to not require a return key press
curses.cbreak()
print "press k to quit"
quit=False
# loop
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)
led1=GPIO.PWM(11,50)
led1.start(7.5)
GPIO.setup(12,GPIO.OUT)
led2=GPIO.PWM(12,50)
led2.start(7.5)
GPIO.setup(38,GPIO.OUT)
led3=GPIO.PWM(38,50)
led3.start(7.5)
GPIO.setup(15,GPIO.OUT)
led4=GPIO.PWM(15,50)
led4.start(5)
GPIO.setup(16,GPIO.OUT)
led5=GPIO.PWM(16,50)
led5.start(7.5)
GPIO.setup(18,GPIO.OUT)
led6=GPIO.PWM(18,50)
led6.start(5.0)
i=5.0
while quit !=True:
			rcv=serial.Serial("/dev/ttyUSB0",9600)
        		rawrcv=rcv.readline()
        		if '$GPVTG' in rawrcv:
                		heading=rawrcv.split(',')
				direction=heading[1]
				
        		if '$GPGGA' in rawrcv:
               			a=a+1
                		print rawrcv
                		print "iteration amount=",a
                		datas=rawrcv.split(',')
				currentlat=double(datas[2])*100
				latlist=currentlat.split(".")
				currentlatdeg=latlist[0]
				currentlatmin=latlist[1]
				ddlat=currentlatdeg+currentlatmin/60
				currentlong=double(datas[3])*100
				longlist=currentlong.split(".")
				currentlongdeg=longlist[0]
				currentlongmin=longlist[1]
				ddlong=currentlongdeg+currentlongmin/60
				northaxis=latinput-ddlat
				eastaxis=longinput-ddlong
				movedir=atan(northaxis/eastaxis)
			c = stdscr.getch()
			print curses.keyname(c)
			if curses.keyname(c)=="w":
				led1.ChangeDutyCycle(10)
				time.sleep(0.035)
				led1.ChangeDutyCycle(7.5)
			if curses.keyname(c)=="a":
				led2.ChangeDutyCycle(5)
				time.sleep(0.035)
				led2.ChangeDutyCycle(7.5)
			if curses.keyname(c)=="d":
       			       	led2.ChangeDutyCycle(10)
        		       	time.sleep(0.035)
        		       	led2.ChangeDutyCycle(7.5)
			if curses.keyname(c)=="s":
        		       	led1.ChangeDutyCycle(5)
        		       	time.sleep(0.035)
        		       	led1.ChangeDutyCycle(7.5)
			if curses.keyname(c)=="q":
       			        led3.ChangeDutyCycle(5)
       		       		time.sleep(0.035)
       		        	led3.ChangeDutyCycle(7.5)
			if curses.keyname(c)=="e":
       		        	led3.ChangeDutyCycle(10)
       		       		time.sleep(0.035)
       		        	led3.ChangeDutyCycle(7.5)
			if curses.keyname(c)=="u":
				i+=0.1
				if i<=10.0 and i>=5.0 :
       			     		led4.ChangeDutyCycle(i)
       			        if i>10:
					i=9.9

			if curses.keyname(c)=="j":
				i-=0.1
				if i<=10.0 and i>=5.0:
       			        	led4.ChangeDutyCycle(i)
				if i<5.0:
					i=5.1
			
			if curses.keyname(c)=="1":
				led5.ChangeDutyCycle(5)
			if curses.keyname(c)=="2":
				led5.ChangeDutyCycle(7.5)
			if curses.keyname(c)=="3":
				led5.ChangeDutyCycle(10)
			if curses.keyname(c)=="o":
       			        led6.ChangeDutyCycle(5)
			if curses.keyname(c)=="p":
       			        led6.ChangeDutyCycle(10)
			
	
			elif curses.keyname(c)=="k" :
				quit=True
				led1.stop()
				led2.stop()
				led3.stop()
				led4.stop()
				led5.stop()
				led6.stop()
				GPIO.cleanup()
curses.endwin()


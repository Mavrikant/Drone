from __future__ import division
import Adafruit_PCA9685  
import time
import curses
import serial
curlatdecimal=[None]*10
curlondecimal=[None]*10
pwm = Adafruit_PCA9685.PCA9685()
minval=210
halfmin=262
halfmax=368
maxval=420
midval=315
#init the curses screen
print "press k to quit"
quit=False
# loop
pwm.set_pwm(0, 0, midval)
pwm.set_pwm(1, 0, midval)
pwm.set_pwm(2, 0, midval)
pwm.set_pwm(3, 0, minval)
pwm.set_pwm(4, 0, midval)
pwm.set_pwm(5, 0, minval)
i=minval
j=minval
counterint=0
pwm.set_pwm_freq(49)
tryouts=0
choice=raw_input("Enter A for auto pilot M for manual control:")
print choice
if (choice=="A"):
	descoords=raw_input("Please enter decimal coordinates (ex:38.316557, 26.638197)")
	desired=descoords.split(",")
	deslat=float(desired[0])
	deslon=float(desired[1])
	while counterint<10:
		rcv=serial.Serial("/dev/ttyUSB0",9600,timeout=1)
		rawrcv=rcv.readline()
		if '$GPGGA' in rawrcv:
			rawinputs=rawrcv.split(",")
			print rawinputs
			if len(rawinputs[2])>0 and len(rawinputs[3])>0 :
				curlat=float(rawinputs[2])/100
				curlats=str(curlat).split(".")
				curlatdecimal[counterint]=(float(curlats[0])+float(curlats[1])/600000)
				curlon=float(rawinputs[4])/100
	                        curlons=str(curlon).split(".")
	                        curlondecimal[counterint]=(float(curlons[0])+float(curlons[1])/600000)
				counterint+=1
			else:
				print "gps can't locate"
				tryouts+=1
				if tryouts >30:
					print "gps timed out"

					exit()
		if counterint==10:
			meanlatcoords=(sum(curlatdecimal)-curlatdecimal[9])/9
			meanloncoords=(sum(curlondecimal)-curlondecimal[9])/9
			print curlatdecimal , curlondecimal
			if abs(curlatdecimal[9]-meanlatcoords)<=0.0003 and abs(curlondecimal[9]-meanloncoords)<=0.0003:
				print "flight starting!"
 				
			else:
				counterint=0
		ser.flushinput()	
		
elif (choice=="M"):
	stdscr = curses.initscr()
	curses.noecho()
#use cbreak to not require a return key press
	curses.cbreak()
	while quit !=True:
			c = stdscr.getch()
			print curses.keyname(c)
			if curses.keyname(c)=="w":
				pwm.set_pwm(0,0,halfmin)
				time.sleep(0.035)
				pwm.set_pwm(0,0,midval)
			if curses.keyname(c)=="a":
				pwm.set_pwm(1,0,halfmin)
				time.sleep(0.035)
				pwm.set_pwm(1,0,midval)
			if curses.keyname(c)=="d":
       			       	pwm.set_pwm(1,0,halfmax)
        		       	time.sleep(0.035)
        		       	pwm.set_pwm(1,0,midval)
			if curses.keyname(c)=="s":
        		       	pwm.set_pwm(0,0,halfmax)
        		       	time.sleep(0.035)
        		       	pwm.set_pwm(0,0,midval)
			if curses.keyname(c)=="q":
       			        pwm.set_pwm(2,0,halfmin)
       		       		time.sleep(0.035)
       		        	pwm.set_pwm(2,0,midval)
			if curses.keyname(c)=="e":
       		        	pwm.set_pwm(2,0,halfmax)
       		       		time.sleep(0.035)
       		        	pwm.set_pwm(2,0,midval)
			if curses.keyname(c)=="u":
				if i<=420 and i>=210 :
       			     		pwm.set_pwm(3,0,i)
       			        if i>=420:
					i=419
				i+=1
				print i
			if curses.keyname(c)=="U":
                                if i<=420 and i>=210 :
                                        pwm.set_pwm(3,0,i)
                                if i>=420:
                                        i=410
                                i+=10
                                print i
			if curses.keyname(c)=="j":
				if i<=420 and i>=210:
       			        	pwm.set_pwm(3,0,i)
				if i<=210:
					i=211
				i-=1
				print i
			if curses.keyname(c)=="J":
                                if i<=420 and i>=210:
                                        pwm.set_pwm(3,0,i)
                                if i<=210:
                                        i=220
                                i-=10
                                print i
			if curses.keyname(c)=="1":
				pwm.set_pwm(4,0,minval)
			if curses.keyname(c)=="2":
				pwm.set_pwm(4,0,midval)
			if curses.keyname(c)=="3":
				pwm.set_pwm(4,0,maxval)
			if curses.keyname(c)=="o":
                                pwm.set_pwm(5,0,minval)
                        if curses.keyname(c)=="p":
                                pwm.set_pwm(5,0,maxval)
	
			elif curses.keyname(c)=="k" :
				quit=True
				pwm.set_pwm(0,0,0)
				pwm.set_pwm(1,0,0)
				pwm.set_pwm(2,0,0)
				pwm.set_pwm(3,0,0)
				pwm.set_pwm(4,0,0)
				pwm.set_pwm(5,0,0)
	curses.endwin()
else:
	print "wrong input"
	pwm.set_pwm(0,0,0)
        pwm.set_pwm(1,0,0)
        pwm.set_pwm(2,0,0)
        pwm.set_pwm(3,0,0)
      	pwm.set_pwm(4,0,0)
        pwm.set_pwm(5,0,0)
	exit()

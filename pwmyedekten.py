from __future__ import division
import Adafruit_PCA9685  
import time
import curses
pwm = Adafruit_PCA9685.PCA9685()
minval=210
halfmin=262
halfmax=368
maxval=420
midval=315
#init the curses screen
stdscr = curses.initscr()
curses.noecho()
#use cbreak to not require a return key press
curses.cbreak()
print "press q to quit"
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
pwm.set_pwm_freq(49)
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

import pygame
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)
led1=GPIO.PWM(11,50)
led1.start(7.5)
GPIO.setup(12,GPIO.OUT)
led2=GPIO.PWM(12,50)
led2.start(7.5)
GPIO.setup(13,GPIO.OUT)
led3=GPIO.PWM(13,50)
led3.start(7.5)
GPIO.setup(15,GPIO.OUT)
led4=GPIO.PWM(15,50)
led4.start(7.5)
GPIO.setup(16,GPIO.OUT)
led5=GPIO.PWM(16,50)
led5.start(7.5)
GPIO.setup(18,GPIO.OUT)
led6=GPIO.PWM(18,50)
led6.start(7.5)
pygame.init()
pygame.display.set_mode()
gamecont=True
while gamecont==True:
	for event in pygame.event.get():
		if event.type==pygame.KEYDOWN:
			if event.key==pygame.K_w:
				led1.ChangeDutyCycle(90)
			elif event.key==pygame.K_k:
				GPIO.cleanup()
				gamecont=False
		else :
			led1.ChangeDutyCycle(7.5)
		

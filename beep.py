#!/usr/bin/python
#cording: utf-8

import RPi.GPIO as GPIO
import time

def beep():

	GPIO.setmode(GPIO.BOARD)

	GPIO.setup(10,GPIO.OUT)

	for i in range(3):
		GPIO.output(10, 1)
		time.sleep(1)
		GPIO.output(10, 0)
		time.sleep(0.5)

	GPIO.cleanup()

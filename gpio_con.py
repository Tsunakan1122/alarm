#!/usr/bin/python
#cording: utf-8
import RPi.GPIO as GPIO
import subprocess
import beep
import time
from datetime import datetime as dt




beep.beep()


GPIO.setmode(GPIO.BOARD)

GPIO.setup(8,GPIO.OUT)








GPIO.output(8, 1)

time.sleep(0.001)

GPIO.output(8,0)

volt=GPIO.input(8)
if volt != 0:
    dt_now = dt.now().strftime('%Y/%m/%d %H:%M:%S \n')
    text='ERROR! Warning. There\'s possibility that break machine  '
    file = open('./scrypt/log.txt', 'a')
    file.write(text)
    file.write(dt_now)
    file.close()


GPIO.cleanup()

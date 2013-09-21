#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

#GPIO.cleanup()
pin_lamp=4
pin_pump=23
pin_relee=24
pin_in=17

GPIO.setmode(GPIO.BCM)

GPIO.setup(pin_in, GPIO.IN)
GPIO.setup(pin_lamp, GPIO.OUT)
GPIO.setup(pin_pump, GPIO.OUT)
GPIO.setup(pin_relee, GPIO.OUT)

GPIO.output(pin_lamp, 0)
GPIO.output(pin_pump, 0)
GPIO.output(pin_relee, 0)
time.sleep(1)
GPIO.output(pin_lamp, 1)
GPIO.output(pin_pump, 1)
GPIO.output(pin_relee, 1)
time.sleep(3)

#for i in range (10):
#	input=GPIO.input(17)
#	print input
#	time.sleep(1)
#	GPIO.output(4,input)

GPIO.cleanup()
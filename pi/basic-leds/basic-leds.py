#!/bin/env python

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

ON = 1
OFF = 0

LED_R = 12
LED_G = 16
LED_B = 21

GPIO.setup(LED_R, GPIO.OUT)
GPIO.setup(LED_G, GPIO.OUT)
GPIO.setup(LED_B, GPIO.OUT)

GPIO.output(LED_G, ON)
time.sleep(10)
GPIO.output(LED_G, OFF)

GPIO.cleanup()

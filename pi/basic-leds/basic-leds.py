#!/bin/env python

import logging
import RPi.GPIO as GPIO
import time

logging.basicConfig(level='INFO')
GPIO.setmode(GPIO.BCM)

ON = GPIO.HIGH
OFF = GPIO.LOW

LED_R = 12
LED_G = 16
LED_B = 21

INTERVAL = 1   # in seconds

GPIO.setup(LED_R, GPIO.OUT)
GPIO.setup(LED_G, GPIO.OUT)
GPIO.setup(LED_B, GPIO.OUT)

logging.info("Starting...")

while True:

    try:
        for i in xrange(0, 8):
            logging.info("  %d", i)

            GPIO.output(LED_R, ON if i & 0b100 else OFF)
            GPIO.output(LED_G, ON if i & 0b010 else OFF)
            GPIO.output(LED_B, ON if i & 0b001 else OFF)

            time.sleep(INTERVAL)
    except KeyboardInterrupt:
        break

    except:
        logging.exception()
        break

logging.info("done.")

GPIO.output(LED_R, OFF)
GPIO.output(LED_G, OFF)
GPIO.output(LED_B, OFF)
GPIO.cleanup()

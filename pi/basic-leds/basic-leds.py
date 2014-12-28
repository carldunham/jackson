#!/usr/bin/env python

import argparse
import logging
import RPi.GPIO as GPIO
import time

DEBUG = 0

ON = GPIO.HIGH
OFF = GPIO.LOW

LED_R = 12
LED_G = 16
LED_B = 21

INTERVAL = 1   # in seconds

logger = logging.getLogger(__name__)

def main():
    parser = argparse.ArgumentParser(description='Control red, green and blue LEDs')
    parser.add_argument('-d', '--debug', type=str, default='INFO', help='set debug level to DEBUG (default: %(default)s)')
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-q', '--quiet', action='store_true')
    group.add_argument('-v', '--verbose', action='store_true')

    opts = parser.parse_args()

    global DEBUG
    DEBUG = opts.debug

    logging.basicConfig(level='INFO')
    logger.debug('opts="%s"',  opts)

    GPIO.setmode(GPIO.BCM)

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

if __name__ == '__main__':
    main()

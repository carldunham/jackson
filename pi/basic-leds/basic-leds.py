#!/usr/bin/env python

import argparse
import logging
import RPi.GPIO as GPIO

ON = GPIO.HIGH
OFF = GPIO.LOW

LED_R = 12
LED_G = 16
LED_B = 21

ALL_LEDS = [LED_R, LED_G, LED_B]

logger = logging.getLogger(__name__)


def setup():
    GPIO.setmode(GPIO.BCM)

    GPIO.setup(LED_R, GPIO.OUT)
    GPIO.setup(LED_G, GPIO.OUT)
    GPIO.setup(LED_B, GPIO.OUT)

    alloff()


def teardown():
    alloff()
    GPIO.cleanup()


def pin(which, on=True):
    GPIO.output(which, ON if on else OFF)


def red(on=True):
    pin(LED_R, on)


def green(on=True):
    pin(LED_G, on)


def blue(on=True):
    pin(LED_B, on)


def alloff():
    [pin(p, OFF) for p in ALL_LEDS]


def main():
    parser = argparse.ArgumentParser(description='Control red, green and blue LEDs')
    parser.add_argument('-d', '--debug', type=str, default='INFO', help='set debug level to DEBUG (default: %(default)s)')
    parser.add_argument('-p', '--plugin', type=str, default='counter', help='Which plugin to run (default: %(default)s)')

    opts = parser.parse_args()

    logging.basicConfig(level=opts.debug)
    logger.debug('opts="%s"',  opts)

    plugin = __import__('plugins', fromlist=[opts.plugin])

    setup()
    plugin.setup()

    logging.info("Starting...")

    while True:

        try:
            plugin.step()

        except KeyboardInterrupt:
            break

        except:
            logging.exception()

    logging.info("done.")

    plugin.teardown()
    teardown()


if __name__ == '__main__':
    main()


# like rand, but only one led on at a time
#
import random
import time

import control


def setup():
    pass


def teardown():
    pass


def step(interval):
    n = random.choice(control.ALL_LEDS)

    control.alloff()
    control.on(n)

    time.sleep(interval)

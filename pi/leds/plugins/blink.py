
import time

import control


def setup():
    pass


def teardown():
    pass


def step(interval):
    control.allon())
    time.sleep(interval)

    control.alloff())
    time.sleep(interval)

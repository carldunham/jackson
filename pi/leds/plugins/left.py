
import time

import control


def setup():
    pass


def teardown():
    pass


def step(interval):
    control.red(False)  # maybe from the last step
    control.blue(True)
    time.sleep(interval)

    control.blue(False)
    control.green(True)
    time.sleep(interval)

    control.green(False)
    control.red(True)
    time.sleep(interval)

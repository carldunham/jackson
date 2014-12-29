
import logging
import time
import RPi.GPIO as GPIO

ON = GPIO.HIGH
OFF = GPIO.LOW

LED_R = 12
LED_G = 16
LED_B = 21

ALL_LEDS = [LED_R, LED_G, LED_B]

RESET_BUTTON = 23
LEFT_BUTTON = 18
RIGHT_BUTTON = 24

ALL_BUTTONS = [RESET_BUTTON, LEFT_BUTTON, RIGHT_BUTTON]

logger = logging.getLogger(__name__)

# an array, in case we want to support multiple later
_callbacks = []


# just make sure bounces on release don't trigger falling
#
def _filter_bounces(channel):
    time.sleep(0.2)

    if get(channel) == OFF:
        global _callbacks
        [cb(channel) for cb in _callbacks]


def setup(button_function=None):
    GPIO.setmode(GPIO.BCM)

    GPIO.setup(ALL_LEDS, GPIO.OUT, initial=OFF)

    GPIO.setup(ALL_BUTTONS, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    global _callbacks
    _callbacks = []

    if button_function:
        _callbacks += button_function

        for b in ALL_BUTTONS:
            logger.debug("setting up callback on button %d", b)
            GPIO.add_event_detect(b, GPIO.BOTH, callback=_filter_bounces, bouncetime=200)


def teardown():
    alloff()

    global _callbacks
    _callbacks = []

    GPIO.cleanup()


def get(which):
    GPIO.input(which)


def set(which, on=True):
    GPIO.output(which, ON if on else OFF)


def on(which):
    set(which, ON)


def off(which):
    set(which, OFF)


def toggle(which):
    set(which, not get(which))


def red(on=True):
    set(LED_R, on)


def green(on=True):
    set(LED_G, on)


def blue(on=True):
    set(LED_B, on)


def all(on=True):
    set(ALL_LEDS, on)


def allon():
    all(ON)


def alloff():
    all(OFF)

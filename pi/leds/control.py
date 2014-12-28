
import RPi.GPIO as GPIO

ON = GPIO.HIGH
OFF = GPIO.LOW

LED_R = 12
LED_G = 16
LED_B = 21

ALL_LEDS = [LED_R, LED_G, LED_B]

RESET_BUTTON = 23
LEFT_BUTTON = 24
RIGHT_BUTTON = 25

ALL_BUTTONS = [RESET_BUTTON, LEFT_BUTTON, RIGHT_BUTTON]


def setup(button_function=None):
    GPIO.setmode(GPIO.BCM)

    GPIO.setup(ALL_LEDS, GPIO.OUT, initial=OFF)

    GPIO.setup(ALL_BUTTONS, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    if button_function:
        GPIO.add_event_detect(ALL_BUTTONS, GPIO.FALLING)
        GPIO.add_event_callback(ALL_BUTTONS, button_function)


def teardown():
    alloff()
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

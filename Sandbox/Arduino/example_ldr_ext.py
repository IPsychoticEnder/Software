import time
import sys
from fhict_cb_01.custom_telemetrix import CustomTelemetrix

# -----------
# Constants
# -----------
LDRPIN = 2  # analog pin A2

# ------------------------------
# Initialized global variables
# ------------------------------
value = 0

# -----------
# functions
# -----------


def LDRChanged(data):
    global value
    value = data[2]
    # print("data:")
    # print(data)


def setup():
    global board
    board = CustomTelemetrix()
    board.set_pin_mode_analog_input(
        LDRPIN, callback=LDRChanged, differential=10)


def loop():
    global value
    print(value)
    time.sleep(1)


# --------------
# main program
# --------------
setup()

while True:
    try:
        loop()
    except KeyboardInterrupt:  # crtl+C
        print('shutdown')
        board.shutdown()
        sys.exit(0)

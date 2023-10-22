from fhict_cb_01.custom_telemetrix import CustomTelemetrix
import sys,time


LDR_PIN = 16


def setup():
    global board
    board = CustomTelemetrix()
    # board.set_pin_mode_analog_input(LDR_PIN)
    board.set_pin_mode_dht(LDR_PIN, dht_type=11)


def getLightLevel():
    sensor_value = board.dht_read(LDR_PIN)
    return sensor_value


setup()
print(getLightLevel())
import time
import sys
from fhict_cb_01.custom_telemetrix import CustomTelemetrix
from flask import Flask, render_template , request


board = CustomTelemetrix()

HTPIN = 12
BUTTON_HUMIDITY = 8
BUTTON_TEMPERATURE = 9

LEDRED = 4
LEDBLUE = 6

levelHumid = 0
prevLevelHumid = 0

levelTemp = 0
prevLevelTemp = 0

humidity_measurements = []
temperature_measurements =[]

def ButtonChange(data):
    global levelHumid, levelTemp
    levelHumid = data[2] 
    levelTemp = data[2]

def setup():
    global board
    board.displayOn()
    board.set_pin_mode_dht(HTPIN, dht_type=11)
    board.set_pin_mode_digital_output(LEDRED)
    board.set_pin_mode_digital_output(LEDBLUE)
    board.set_pin_mode_digital_input_pullup(BUTTON_HUMIDITY, callback=ButtonChange)
    board.set_pin_mode_digital_input_pullup(BUTTON_TEMPERATURE, callback=ButtonChange)

def loop():
    time.sleep(0.01)

    global prevLevelHumid, prevLevelTemp

    humidity, temperature, timestamp = board.dht_read(HTPIN)

    def add_humidity():
        board.displayShow(humidity)
        print(f"The humidity is: {humidity}")
        humidity_measurements.append(humidity)


    def add_temperature():
        board.displayShow(temperature)
        print(f"The temperature is: {temperature}")
        temperature_measurements.append(temperature)


    if prevLevelHumid != levelHumid:
        add_humidity()
        board.digital_write(LEDRED, 1)
        prevLevelHumid = levelHumid

    if prevLevelTemp != levelTemp:
        add_temperature()
        prevLevelTemp = levelTemp
        board. digital_write(LEDBLUE, 1)
    else:
        board.digital_write(LEDBLUE, 0)
        board.digital_write(LEDRED, 0)
setup()
while True:
    try:
        loop()
    except KeyboardInterrupt:  # crtl+C
        print('shutdown')
        board.shutdown()
        sys.exit(0)
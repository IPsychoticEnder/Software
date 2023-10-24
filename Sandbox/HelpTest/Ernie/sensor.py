import time
import sys
from fhict_cb_01.custom_telemetrix import CustomTelemetrix
from flask import Flask, render_template , request
import csv

board = CustomTelemetrix(com_port="COM4",arduino_instance_id=1)

HTPIN = 12
BUTTON1 = 9
LDRPIN = 2

options = 0

add_temperature = []
add_humidity = []
add_light = []

level = 0

def buttonChangeOption(data):
    global options 
    level = data[2]
    if level != 1:
            if options == 0:
                board.displayShow(getHumidity())
            elif options == 1:
                board.displayShow(getTemperature()) 
            if options == 2:
                board.displayShow(getLight())
                options = -1
            options += 1
    time.sleep(1)

def getHumidity():
        humidity, temperature, timestamp = board.dht_read(HTPIN)
        light = board.analog_read(LDRPIN)
        board.displayShow(humidity)
        add_humidity.append(humidity)
        return humidity
    
def getLight():
        humidity, temperature, timestamp = board.dht_read(HTPIN)
        light = board.analog_read(LDRPIN)
        board.displayShow(light[0])
        add_light.append(light)
        return light[0]

def getTemperature():
        humidity, temperature, timestamp = board.dht_read(HTPIN)
        light = board.analog_read(LDRPIN)
        board.displayShow(temperature)
        add_temperature.append(temperature)
        return temperature

def setup():
    global board
    board.displayOn()
    board.set_pin_mode_dht(HTPIN, dht_type=11)
    board.set_pin_mode_analog_input(LDRPIN)
    board.set_pin_mode_digital_input_pullup(BUTTON1, callback=buttonChangeOption)

def loop():

    time.sleep(1)

setup()
while True:
    try:
        loop()
    except KeyboardInterrupt:
        print('shutdown')
        board.shutdown()
        sys.exit(0)



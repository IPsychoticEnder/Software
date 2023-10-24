from fhict_cb_01.custom_telemetrix import CustomTelemetrix
import sys,time


BUTTON = 8
LDR_PIN = 2
DHT_PIN = 12


options_index = 0


def setup():
    global board
    board = CustomTelemetrix()
    board.displayOn()
    board.set_pin_mode_digital_input_pullup(BUTTON, callback=buttonChanged)
    board.set_pin_mode_analog_input(LDR_PIN)
    board.set_pin_mode_dht(DHT_PIN, dht_type=11)


def getHumidity():
    humidity, temperature, timestamp = board.dht_read(DHT_PIN)
    # print(humidity)
    return humidity

def getTemperature():
    humidity, temperature, timestamp = board.dht_read(DHT_PIN)
    # print(temperature)
    return temperature

def getLightLevel():
    light_level = board.analog_read(LDR_PIN)
    # print(light_level[0])
    return light_level[0]


def buttonChanged(data):
    global options_index
    if data[2] != 1:
        if options_index == 0:
            board.displayShow(getHumidity())
            print("Humidity")
            
        elif options_index == 1:
            board.displayShow(getTemperature()) 
            print("Temperature")                      
            
        if options_index == 2:
            board.displayShow(getLightLevel())
            print("Light level")
            options_index = -1
            
        options_index += 1
        
    
def loop():
    time.sleep(1)
        
setup()
while True:
    try:
        loop()
    except KeyboardInterrupt:
        print("shutdown...")
        board.shutdown()
        sys.exit(0)
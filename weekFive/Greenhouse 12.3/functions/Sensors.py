from fhict_cb_01.custom_telemetrix import CustomTelemetrix


LDR_PIN = 2
DHT_PIN = 12


options_index = 0
board = CustomTelemetrix(com_port="COM4", arduino_instance_id=1)
board.set_pin_mode_dht(DHT_PIN, dht_type=11)
board.set_pin_mode_analog_input(LDR_PIN)



def getHumidity():
    global board
    humidity, temperature, timestamp = board.dht_read(DHT_PIN)
    board.displayOn()
    print(humidity)
    return humidity

def getTemperature():
    global board
    humidity, temperature, timestamp = board.dht_read(DHT_PIN)
    board.displayOn()
    print(temperature)
    return temperature

def getLightLevel():
    global board
    light_level = board.analog_read(LDR_PIN)
    board.displayOn()
    print(light_level[0])
    return light_level[0]

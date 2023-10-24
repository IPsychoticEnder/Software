from fhict_cb_01.custom_telemetrix import CustomTelemetrix

LDRPIN = 2
HTPIN = 12

board = CustomTelemetrix(arduino_instance_id=1)

board.set_pin_mode_dht(HTPIN, dht_type=11)
board.set_pin_mode_analog_input(LDRPIN)

def getHumidity():
        humidity, temperature, timestamp = board.dht_read(HTPIN)
        print(humidity)
        return humidity
        
    
def getLight():
        light = board.analog_read(LDRPIN)
        print(light[0])
        return light[0]

def getTemperature():
        humidity, temperature, timestamp = board.dht_read(HTPIN)
        print(temperature)
        return temperature

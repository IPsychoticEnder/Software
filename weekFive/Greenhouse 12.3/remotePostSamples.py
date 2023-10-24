import requests, time
from functions import Sensors

while True:
    try:
        temperature = Sensors.getTemperature()
        humidity = Sensors.getHumidity()
        light_level = Sensors.getLightLevel()

        data = {'sent_temperature': temperature, 
                'sent_humidity': humidity, 
                'sent_light_level': light_level}
        response = requests.post('http://localhost:5000/receive-sample', json=data)
        time.sleep(5)
    except KeyboardInterrupt:
        print("Shutting down...")
        break
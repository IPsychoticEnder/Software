import time, requests
import Sensors

while True:
    try:
        temperature = Sensors.getTemperature()
        humidity = Sensors.getHumidity()
        light = Sensors.getLight()
        print(temperature, humidity, light)

        data = {'post_temp': temperature, 'post_humid': humidity, 'post_light': light}
        response = requests.post('http://localhost:5000//post_data', json=data)
        time.sleep(3)
    except KeyboardInterrupt:
        print("Shutting down...")
        break
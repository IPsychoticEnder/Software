import random

def getTemperature():
    temperature = random.randint(20, 40)
    return temperature

def getHumidity():
    humidity = random.randint(0, 100)
    return humidity

def getLightlevel():
    light_levels = random.randint(0, 1000)
    return light_levels
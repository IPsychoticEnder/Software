from datetime import datetime
import random

samples_list = []

def getTime():
    rightNow = datetime.now()
    time = rightNow.strftime("%I:%M%p")
    time = time.lstrip("0")
    time = time.lower()
    return time

def getDate():
    rightNow = datetime.now()
    day = rightNow.strftime("%A")
    return day

def getLightLevel():
    return random.randint(0,1000)

def makeList():
    if len(samples_list) == 15:
        samples_list.insert(0, [getTime(), getDate(), getLightLevel()])
        samples_list.pop()
    else:
        samples_list.insert(0, [getTime(), getDate(), getLightLevel()])
    return samples_list
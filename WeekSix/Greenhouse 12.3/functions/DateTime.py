from datetime import datetime

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
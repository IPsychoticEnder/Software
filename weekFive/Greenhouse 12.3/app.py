from flask import Flask, render_template
from functions import DateTime, Sensors, HandleLists

samples = []

app = Flask(__name__)

@app.route('/')
def index():
    global samples
    timeDay = (DateTime.getTime(), DateTime.getDate())
    temperature = HandleLists.makeList("one", Sensors.getTemperature())
    humidity = HandleLists.makeList("two", Sensors.getHumidity())
    light_level = HandleLists.makeList("three", Sensors.getLightlevel())

    samples = [temperature, humidity, light_level]
    return render_template('index.html',
                           timeDay = timeDay,
                           temperature = temperature,
                           humidity = humidity,
                           light_level = light_level
                           )

@app.route('/get-list', methods=['GET'])
def getSamples():

    if len(samples) == 0:
        return {}
    
    send_samples = samples
    return {'sent_samples': send_samples}

app.run()

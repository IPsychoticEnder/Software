from flask import Flask, render_template, request
from functions import DateTime, Sensors, HandleLists

samples = []

app = Flask(__name__)

@app.route('/')
def index():
    global samples
    timeDay = (DateTime.getTime(), DateTime.getDate())

    return render_template('index.html',
                           timeDay = timeDay,
                           temperature = HandleLists.makeList("temperature", Sensors.getTemperature()),
                           humidity = HandleLists.makeList("humidity", Sensors.getHumidity()),
                           light_level = HandleLists.makeList("light_level", Sensors.getLightLevel()))


@app.route('/get-list', methods=['GET'])
def getRemoteSamples():

    if len(samples) == 0:
        return {}
    
    send_samples = samples
    return {'sent_samples': send_samples}

@app.route('/receive-sample', methods=['POST'])
def setRemoteSamples():
    data = request.get_json()

    temperature = data['sent_temperature'] 
    humidity = data['sent_humidity'] 
    light_level = data['sent_light_level']

    new_samples = (temperature, humidity, light_level)
    samples.append(new_samples)

    return "Ok"

app.run()

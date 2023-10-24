from flask import Flask, render_template, request
from functions import DateTime, HandleLists, Sensors

samples = []
temperature = 0
humidity = 0
light_level = 0

app = Flask(__name__)

@app.route('/')
def index():
    global samples
    global temperature
    global humidity
    global light_level
    
    timeDay = (DateTime.getTime(), DateTime.getDate())

    # samples = ["One", "Two", "Three"]

    return render_template('index.html',
                           timeDay = timeDay,
                           temperature = HandleLists.makeList('temperature', Sensors.getTemperature()),
                           humidity = HandleLists.makeList('humidity', Sensors.getHumidity()),
                           light_level = HandleLists.makeList('light_level', Sensors.getLightLevel()),)


@app.route('/get-list', methods=['GET'])
def getRemoteSamples():

    if len(samples) == 0:
        return {}
    
    send_samples = samples
    return {'sent_samples': send_samples}

@app.route('/receive-sample', methods=['POST'])
def setRemoteSamples():
    global temperature
    global humidity
    global light_level

    data = request.get_json()

    temperature = data['sent_temperature'] 
    humidity = data['sent_humidity']
    light_level = data['sent_light_level']

    return "Ok"

app.run()

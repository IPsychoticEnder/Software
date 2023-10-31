from flask import Flask, render_template, request
from functions import DateTime, HandleLists

temperature = 0
humidity = 0
light_level = 0
samples = []

app = Flask(__name__)

@app.route('/')
def index():
    global temperature, humidity, light_level
    
    timeDay = (DateTime.getTime(), DateTime.getDate())

    return render_template('index.html',
                           timeDay = timeDay,
                           temperature = temperature,
                           humidity = humidity,
                           light_level = light_level,
                           average_temperature = HandleLists.get_averaqge(samples[0], 2) if samples else 0,
                           average_humidity = HandleLists.get_averaqge(samples[1], 2) if samples else 0,
                           average_light_level = HandleLists.get_averaqge(samples[2], 2) if samples else 0,
                           max_temperature = HandleLists.get_maximum(samples[0]) if samples else 0,
                           max_humidity = HandleLists.get_maximum(samples[1]) if samples else 0,
                           max_light_level = HandleLists.get_maximum(samples[2]) if samples else 0,
                           min_temperature = HandleLists.get_minimum(samples[0]) if samples else 0,
                           min_humidity = HandleLists.get_minimum(samples[1]) if samples else 0,
                           min_light_level = HandleLists.get_minimum(samples[2]) if samples else 0
                           )


@app.route('/get-list', methods=['GET'])
def getRemoteSamples():
    global samples

    if len(samples) == 0:
        return {}
    
    return {'sent_samples': samples}

@app.route('/receive-sample', methods=['POST'])
def setRemoteSamples():
    global temperature, humidity, light_level, samples

    data = request.get_json()

    temperature = data['sent_temperature'] 
    humidity = data['sent_humidity']
    light_level = data['sent_light_level']

    sample_temperature = HandleLists.makeList("temperature", temperature)
    sample_humidity = HandleLists.makeList("humidity", humidity)
    sample_light_level = HandleLists.makeList("light_level", light_level)

    samples = (sample_temperature, sample_humidity, sample_light_level)

    return "Ok"

app.run()

from flask import Flask, render_template
from functions import DateTime, Sensors, HandleLists

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html',
                           text = (DateTime.getTime(), DateTime.getDate()),
                           temperature = HandleLists.makeList("one", Sensors.getTemperature()),
                           humidity = HandleLists.makeList("two", Sensors.getHumidity()),
                           light_level = HandleLists.makeList("three", Sensors.getLightlevels())
                           )

app.run()

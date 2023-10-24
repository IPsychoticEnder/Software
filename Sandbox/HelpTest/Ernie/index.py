from flask import Flask, render_template , request
 
app = Flask(__name__)

add_light = []
add_temperature = []
add_humidity = []

temperature = 0
humidity = 0
light = 0

@app.route('/')
def index():
    global temperature, humidity, light
    add_temperature.append(temperature)
    add_humidity.append(humidity)
    add_light.append(light)
    return render_template('index.html', 
                           temperature = add_temperature, 
                           humidity = add_humidity, 
                           light = add_light)

@app.route("/post_data", methods=["POST"])
def receive_data():
    global temperature, humidity, light

    json_data = request.get_json()

    temperature = json_data['post_temp']
    humidity = json_data['post_humid']
    light = json_data['post_light']

    return "OK"

app.run()




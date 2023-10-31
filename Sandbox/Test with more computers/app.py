from flask import Flask, render_template, request

name = ""
password = ""

app = Flask(__name__)

@app.route('/')
def index():
    global name, password

    return render_template('index.html',
                           name = name if name else "No name yet",
                           password = password if password else "No password yet")


@app.route('/receive-credentials', methods=['POST'])
def setCredentials():
    global name, password

    data = request.get_json()

    name = data['sent_name']
    password = data['sent_password']

    return "Ok"

app.run(host="0.0.0.0", port=80)
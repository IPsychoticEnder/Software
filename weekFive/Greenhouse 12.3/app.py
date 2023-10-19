from flask import Flask, render_template, redirect, request
from functions import DateTime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html',
                           text = (DateTime.getTime(), DateTime.getDate()))

@app.route('/add_text', methods=['POST'])
def receive_text():
    global text

    text = request.form['text']

    return redirect('/display')

@app.route('/display')
def display_text():
    text = text
    return render_template('/display.html',
                           text = text)

app.run()
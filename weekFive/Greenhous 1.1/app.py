from flask import Flask, render_template
from functions import samples

app = Flask(__name__)

@app.route('/')
def init():
    return render_template('index.html',
                           samples_list = samples.makeList())

app.run()
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/buy-now')
def buy_now():
    return render_template('buy-now.html')

@app.route('/our-product')
def our_products():
    return render_template('our-product.html')

@app.route('/forms')
def forms():
    return render_template('forms.html')


app.run()
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!!!!!'


@app.route('/blog')
def blog():
    return 'blogs'


@app.route('/blog/2021/dogs')
def blog2():
    return 'dog'

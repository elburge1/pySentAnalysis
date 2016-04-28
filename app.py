from flask import Flask, request
from analysis import get_score
import json

app = Flask(__name__)

text = 'Good morning!'

@app.route('/')
def index():
    return json.dumps(get_score(text))

@app.route('/', methods = ['POST'])
def sent():
    return json.dumps([get_score(tweet['text']) for tweet in request.json])

if __name__ == '__main__':
    app.run()

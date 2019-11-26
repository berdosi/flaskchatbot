from flask import Flask, redirect, url_for, render_template, jsonify
import urllib, json

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('main.html.j2')

@app.route('/chatbot-api/<path:apipath>')
def api_call(apipath):
    print(apipath)
    url = "http://api:5001/api/" + apipath
    response = urllib.request.urlopen(url)
    return response.read()

if __name__ == '__main__':
    app.run(
        host="0.0.0.0",
        port=5000)

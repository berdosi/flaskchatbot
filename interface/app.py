from flask import Flask, redirect, url_for, render_template, jsonify
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('main.html.j2')

@app.route('/api/<path:apipath>')
def api_call(apipath):
    return jsonify({"error": "Not implemented.", "requested": apipath})

if __name__ == '__main__':
    app.run()
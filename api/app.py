from flask import Flask, redirect, url_for, render_template, jsonify
app = Flask(__name__)

@app.route('/api/<path:apipath>')
def api_call(apipath):
    return jsonify({"error": "Not implemented through API.", "requested": apipath})

if __name__ == '__main__':
    app.run(
        host="0.0.0.0",
        port=5001)

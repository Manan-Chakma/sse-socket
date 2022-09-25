from time import sleep
import json
from flask import Flask, jsonify, make_response, Response, render_template
from flask_sse import sse

app = Flask(__name__, template_folder='../frontend')
app.config["REDIS_URL"] = 'redis://localhost:6379'
app.register_blueprint(sse, url_prefix='/stream')


@app.route('/listen')
def listen():
    sse.publish({"message": "Hello!"}, type='online')
    return "Message sent!"

@app.route("/")
def home():
    return render_template('index.html')



if __name__ == '__main__':
    # https://flask-sse.readthedocs.io/en/latest/quickstart.html

    # gunicorn app:app --worker-class gevent --bind 127.0.0.1:5000
    app.run(debug=True)
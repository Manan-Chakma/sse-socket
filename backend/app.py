import imp
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    data = {
        'name': 'Python'
    }
    return jsonify(data)



if __name__ == '__main__':
    app.run(debug=True)
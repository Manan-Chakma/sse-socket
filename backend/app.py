from time import sleep
import json
from flask import Flask, jsonify, make_response, Response, render_template

app = Flask(__name__, template_folder='../frontend')


@app.route('/listen')
def listen():
    def stream():
        for i in range(5):
            _data = json.dumps({"name":'Python', "task":'SSE'})
            yield f"data: {_data}\nevent: online\n\n"
            sleep(1)

    return Response(stream(), mimetype='text/event-stream')

@app.route("/")
def home():
    return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True)
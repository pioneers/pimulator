import datetime
import time
import robot
import sys
import urllib
import os
from base64 import b64decode
from flask import Flask, render_template, jsonify
app = Flask(__name__)

@app.route('/start_teleop')
def start_teleop():
    print('Starting Teleop Mode!', file=sys.stderr)
    return str(robot.start(auto=0))

@app.route('/start_auto/<f>')
def start_auto(f):
    print('Starting Autonomous Mode!', file=sys.stderr)
    print(f, file=sys.stderr)
    #h, encoded = f.split(",", 1)
    data = b64decode(f)
    with open("student_code.py", "wb") as file:
        file.write(data)
    return str(robot.start(auto=1))

@app.route('/stop')
def stop():
    return str(robot.stop())

@app.route('/state')
def state():
    if robot.robot_thread is None:
        return jsonify(x=72, y=72, theta=0)
    else:
        result = robot.get_state()
        return jsonify(x=result['x'], y=result['y'], theta=result['dir'])

@app.route('/')
def hello_world(name=None):
    return render_template('index.html', name=name)

@app.route('/time')
def get_time():
    return str(datetime.datetime.now())


@app.route('/okay')
def ewkay():
    return "okay"

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)

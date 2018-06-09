from flask import Flask, render_template, url_for, request
app = Flask(__name__)
from src.utils import Utils
import json
# from src.position import Positioner


data = open('static/misc/data.json', 'r')
data = json.load(data)

utils = Utils()

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/top')
def route_top():
    return render_template('top.html')

@app.route('/timer')
def route_timer():
    return render_template('timer.html')

@app.route('/participants', methods=['GET', 'POST'])
def get_participants():
    print("/participants")
    num_p = 10
    if request.method == 'POST':
        num_p = int(request.form.get('participants', 3))

    # TODO: /participantsへのpostの参加人数を受け取って、jsonに入れる
    # data[0]["participant"] = str(num_p)

    data, positions = utils.decide_positions(num_p)
    print(positions)
    print(data)
    now = 1
    return render_template(
        'play_position.html',
        num_p=num_p,
        positions=positions,
        data=data,
        data_dump=json.dumps(data),
        now=now
    )

@app.route('/playing_do', methods=['GET', 'POST'])
def doing_in_night():
    # TODO: /participantsへのpostの参加人数を受け取って、jsonに入れる
    num_p = 3
    # data[0]["participant"] = str(num_p)

    data, positions = utils.decide_positions(num_p)
    print(positions)
    print(data)
    now = 1
    return render_template('play_position.html', positions=positions, data=data, now=now,num_p=num_p)


if __name__ == '__main__':

    # app.run(host='0.0.0.0', port=80)
    app.run(host='0.0.0.0', port=5000)

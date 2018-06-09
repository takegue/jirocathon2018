from flask import Flask, render_template, url_for, request
app = Flask(__name__)
from src.utils import Utils
import json
# from src.position import Positioner


data = open('static/misc/data.json', 'r')
data = json.load(data)

utils = Utils()

@app.route('/start')
def hello():
    return render_template('index.html')

@app.route('/')
def route_top():
    return render_template('top.html')

@app.route('/timer')
def route_timer():
    return render_template('timer.html')

@app.route('/participants', methods=['GET', 'POST'])
def get_participants():
    print("/participants")
    
    if request.method == 'POST':
        utils.num_p = int(request.form.get('participants', 3))
        print("num_p: {}".format(utils.num_p))

    # TODO: /participantsへのpostの参加人数を受け取って、jsonに入れる
    # data[0]["participant"] = str(num_p)

    data, positions = utils.decide_positions(utils.num_p)
    print(positions)
    print(data)
    utils.now += 1
    return render_template(
        'play_position.html',
        num_p=utils.num_p,
        positions=positions,
        data=data,
        data_dump=json.dumps(data),
        now=utils.now
    )

@app.route('/playing_do', methods=['GET', 'POST'])
def doing_in_night():
    # TODO: /participantsへのpostの参加人数を受け取って、jsonに入れる
    if request.method == 'POST':
        # now = int(request.form.get('now', 3))
        print("now: {}".format(request.form))
        if utils.now >= utils.num_p:
            return render_template('result.html')

    # data[0]["participant"] = str(num_p)

    data, positions = utils.decide_positions(utils.num_p)
    # print(positions)
    # print(data)
    utils.now += 1
    print("now : {}".format(utils.now))

    

    return render_template('play_position.html', positions=positions, data=data, now=utils.now,num_p=utils.num_p, data_dump=json.dumps(data))

@app.route('/vote', methods=['GET', 'POST'])
def vote():
    # p_num = data[0]["participant"]
    num_p = 3
    now = 2
    print(now)
    return render_template('vote.html', num_p=num_p, now=now)

if __name__ == '__main__':

    # app.run(host='0.0.0.0', port=80)
    app.run(host='0.0.0.0', port=5000)

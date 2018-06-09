from flask import Flask, render_template, url_for, request
app = Flask(__name__)
import json
data = open('../data/data.json', 'r')
data = json.load(data)


@app.route('/')
def hello():
    print(data)
    return render_template('index.html')


@app.route('/participants', methods=['GET', 'POST'])
def get_participants():
    print("/participants")
    # TODO: /participantsへのpostの参加人数を受け取って、jsonに入れる
    p = 3
    data[0]["participant"] = str(p)
    print(data)
    return render_template('index.html')


if __name__ == '__main__':

    # app.run(host='0.0.0.0', port=80)
    app.run(host='0.0.0.0', port=5000)

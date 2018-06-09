from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/top')
def route_top():
    return render_template('top.html')

@app.route('/timer')
def route_timer():
    return render_template('timer.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

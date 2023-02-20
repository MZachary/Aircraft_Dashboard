from flask import Flask, jsonify, request, render_template
import sqlite3
import serial

from flask import Flask, render_template
from flask_socketio import SocketIO





# configuration
DEBUG = True


#instantiate the app
app = Flask(__name__, static_url_path='', static_folder='static', template_folder='templates')
app.config['SECRET_KEY'] = 'asdf1234'
socketio = SocketIO(app)


@app.route('/', methods=['GET'])
def dashboard():
    return render_template("dashboard.html")

@socketio.on('my event')
def handle_my_custom_event(json):
    print('received json: ' + str(json))



if __name__ == '__main__':
    socketio.run(app)
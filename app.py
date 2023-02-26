from threading import Lock
from flask import Flask, jsonify, request, render_template
from flask_socketio import SocketIO, send, emit
import sqlite3
import serial


# Set this variable to "threading", "eventlet" or "gevent" to test the
# different async modes, or leave it set to None for the application to choose
# the best option based on installed packages.
async_mode = None

#instantiate the app
app = Flask(__name__, static_url_path='', static_folder='static', template_folder='templates')
app.config['SECRET_KEY'] = 'asdf1234'
socketio = SocketIO(app, async_mode=async_mode)

thread = None
thread_lock = Lock()

@app.route('/', methods=['GET'])
def dashboard():
    return render_template("dashboard.html", async_mode=socketio.async_mode)

def background_thread():
    count = 0
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    db = conn.cursor()
    db.execute('SELECT * FROM serial_data ORDER BY time_recorded DESC')
    data = db.fetchall()
    conn.close()
    while count < len(data):
        socketio.sleep(1)
        print('count', count, '/', len(data))
        
        socketio.emit('data', dict(data[count]))
        if(count == (len(data) - 1)):
            count = 0
        else:
            count += 1

@socketio.event
def connect():
    global thread
    with thread_lock:
        if thread is None:
            thread = socketio.start_background_task(background_thread)
    emit('my_response', {'data': 'Connected', 'count': 0})

if __name__ == '__main__':
    socketio.run(app)
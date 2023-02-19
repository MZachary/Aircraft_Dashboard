from flask import Flask, jsonify
from flask_cors import CORS
import sqlite3
import serial


# configuration
DEBUG = True


#instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)


#enable CORS
CORS(app, resources={'/*': {'origins': '*'}})



def get_db_connection():
    conn = sqlite3.connect('/home/zach/Aircraft_Dashboard/flask-vue-crud/server/database.db')
    
    # conn.row_factory = sqlite3.Row
    return conn


@app.route('/serial_data')
def get_data():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM serial_data ORDER BY time_recorded DESC LIMIT 1')
    data = cursor.fetchone()
    conn.close()
    
    return jsonify({
    'lat' : data[0],
    'lon' : data[1],
    'heading_deg' : data[2],
    'bearing_deg' : data[3],
    'range_ft' : data[4],
    'target_lat' : data[5],
    'target_lon' : data[6],
    'airspeed_fps' : data[7],
    'groundspeed_fps' : data[8],
    'theta_deg' : data[9],
    'phi_deg' : data[10],
    'gps_altitude_ft' : data[11],
    'baro_altitude_ft' : data[12],
    'bat_voltage_V' : data[13],
    'local_time' : data[14],
    'time_recorded' : data[15],
  })

app.route('/serial_ports')
def list_serial_ports():
  return jsonify(['port1','port2','port3'])

if __name__ == '__main__':
    app.run()

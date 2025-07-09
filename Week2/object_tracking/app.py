from flask import Flask, jsonify, render_template
import serial
import threading
import time

app = Flask(__name__)

SERIAL_PORT = '/dev/pts/4'
BAUD_RATE = 9600

ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
gps_data = {'lat': 37.4221, 'lon': -122.0841}

def read_serial():
    global gps_data
    while True:
        if ser.in_waiting:
            line = ser.readline().decode().strip()
            print(f"[FLASK] Got: {line}")
            try:
                lat_str, lon_str = line.split(",")
                gps_data['lat'] = float(lat_str)
                gps_data['lon'] = float(lon_str)
            except ValueError:
                print("[FLASK] Malformed GPS data!")
        time.sleep(1)

threading.Thread(target=read_serial, daemon=True).start()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/location')
def location():
    return jsonify(gps_data)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)

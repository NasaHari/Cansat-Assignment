from flask import Flask, jsonify, render_template
import serial
import threading
import time

app = Flask(__name__)

SERIAL_PORT = '/dev/pts/4'
BAUD_RATE = 9600

ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
sensor_data = {'temp': '--'}

def read_serial():
    global sensor_data  # ✅ make sure it's the same!
    while True:
        if ser.in_waiting:
            line = ser.readline().decode().strip()
            print(f"[FLASK] Got: {line}")
            sensor_data['temp'] = line
        time.sleep(1)

t = threading.Thread(target=read_serial)
t.daemon = True
t.start()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data')
def data():
    print(f"[FLASK] Returning: {sensor_data}")  # ✅ print this too
    return jsonify(sensor_data)

if __name__ == '__main__':
    app.run(debug=False)

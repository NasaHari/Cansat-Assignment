from flask import Flask, render_template, request, jsonify
import serial
import threading
import time

app = Flask(__name__)

SERIAL_PORT = '/dev/pts/4'  # 🔁 Update for your PTY
BAUD_RATE = 9600

ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
led_status = {'status': 'Unknown'}

def listen_serial():
    global led_status
    while True:
        if ser.in_waiting:
            response = ser.readline().decode().strip()
            print(f"[FLASK] ESP32 says: {response}")
            led_status['status'] = response
        time.sleep(1)

threading.Thread(target=listen_serial, daemon=True).start()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/control', methods=['POST'])
def control():
    action = request.json.get('action')
    print(f"[FLASK] Sending command: {action}")
    ser.write(f"{action}\n".encode())
    return jsonify({"sent": action})

@app.route('/status')
def status():
    return jsonify(led_status)

if __name__ == '__main__':
    app.run(debug=False)

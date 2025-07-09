import serial
import time
import random

SERIAL_PORT = '/dev/pts/5'  # This must match the other side of your socat PTY pair!
BAUD_RATE = 9600

ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
print(f"[ESP32 SIMULATOR] GPS Tracker running on {SERIAL_PORT}")

lat, lon = 37.4221, -122.0841

try:
    while True:
        lat += random.uniform(-0.0002, 0.0002)
        lon += random.uniform(-0.0002, 0.0002)

        coords = f"{lat},{lon}\n"
        ser.write(coords.encode())
        print(f"[ESP32 SIMULATOR] Sent: {coords.strip()}")

        time.sleep(2)

except KeyboardInterrupt:
    ser.close()
    print("Stopped.")

import serial
import time

SERIAL_PORT = '/dev/pts/5'  # The other PTY pair
BAUD_RATE = 9600

ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
print(f"[ESP32 SIM] Listening on {SERIAL_PORT}")

try:
    while True:
        if ser.in_waiting:
            cmd = ser.readline().decode().strip()
            print(f"[ESP32 SIM] Got command: {cmd}")
            if cmd == "ON":
                response = "LED ON"
            elif cmd == "OFF":
                response = "LED OFF"
            else:
                response = "Unknown Command"
            ser.write(f"{response}\n".encode())
        time.sleep(1)

except KeyboardInterrupt:
    ser.close()
    print("Stopped.")

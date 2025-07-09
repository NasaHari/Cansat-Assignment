import serial
import time

SERIAL_PORT = '/dev/pts/5'
BAUD_RATE = 9600

ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
print(f"ESP32 SIMULATOR on {SERIAL_PORT}")

try:
    while True:
        # Send fake temp
        temp = 25 + (time.time() % 5)
        ser.write(f"{temp:.2f}\n".encode())
        print(f"[ESP32] Sent: {temp:.2f}")

        # Listen for commands
        if ser.in_waiting:
            line = ser.readline().decode().strip()
            print(f"[ESP32] Got: {line}")
            if line == "ON":
                ser.write(b"LED ON\n")
                print("[ESP32] Sent: LED ON")
            elif line == "OFF":
                ser.write(b"LED OFF\n")
                print("[ESP32] Sent: LED OFF")

        time.sleep(2)

except KeyboardInterrupt:
    ser.close()
    print("Stopped.")

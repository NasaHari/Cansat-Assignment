#!/usr/bin/env python3
import serial

# Connect to the *other* end of the pair
PORT = "/dev/pts/6"
BAUD = 115200

def main():
    ser = serial.Serial(PORT, BAUD, timeout=2)
    try:
        print(f"Listening on {PORT} at {BAUD}bps...")
        while True:
            line = ser.readline().decode('utf-8', errors='ignore').strip()
            if line:
                print(f"received ← {line}")
    except KeyboardInterrupt:
        print("Stopping")
    finally:
        ser.close()

if __name__ == "__main__":
    main()

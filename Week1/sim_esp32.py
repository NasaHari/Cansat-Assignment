#!/usr/bin/env python3
import time
import serial

# Replace with one end of your socat pair:
PORT = "/dev/pts/7"
BAUD = 115200

def main():
    ser = serial.Serial(PORT, BAUD, timeout=1)
    try:
        while True:
            ser.write(b"Hello, Cansat!\n")
            print("sent → Hello, Cansat!")
            time.sleep(1)
    except KeyboardInterrupt:
        print("Exiting")
    finally:
        ser.close()

if __name__ == "__main__":
    main()

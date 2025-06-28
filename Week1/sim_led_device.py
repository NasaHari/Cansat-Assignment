#!/usr/bin/env python3
import serial

PORT = "/dev/pts/6"
BAUD = 9600

def main():
    ser = serial.Serial(PORT, BAUD, timeout=1)
    try:
        while True:
            cmd = ser.readline().decode().strip()
            if cmd == "ON":
                ser.write(b"LED ON\n")
                print("→ LED ON")
            elif cmd == "OFF":
                ser.write(b"LED OFF\n")
                print("→ LED OFF")
    except KeyboardInterrupt:
        pass
    finally:
        ser.close()

if __name__ == "__main__":
    main()

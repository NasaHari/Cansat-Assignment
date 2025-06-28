#!/usr/bin/env python3
import serial
import time

PORT = "/dev/pts/7"
BAUD = 9600

def main():
    ser = serial.Serial(PORT, BAUD, timeout=2)
    try:
        for cmd in ["ON", "OFF", "ON"]:
            ser.write(f"{cmd}\n".encode())
            print(f"sent → {cmd}")
            # wait for confirmation
            resp = ser.readline().decode().strip()
            if resp:
                print(f"recv ← {resp}")
            time.sleep(1)
    except KeyboardInterrupt:
        pass
    finally:
        ser.close()

if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
sim_data_sender.py

Simulates an ESP32 sending a numeric sensor value (counter) over serial
every two seconds to be read and logged by log_data.py.
"""

import time
import serial

# ----------------------------------------------------------------------
# CONFIGURATION
# ----------------------------------------------------------------------

# Serial port to write to (must be the mate of the log_data.py port)
PORT = "/dev/pts/7"
# Match the baud rate used by log_data.py
BAUD = 9600

# Interval between sends (in seconds)
SEND_INTERVAL = 2

def main():
    try:
        # Open the serial port for writing
        ser = serial.Serial(PORT, BAUD, timeout=1)
        print(f"Simulator sending to {PORT} @ {BAUD} baud every {SEND_INTERVAL}s")
    except serial.SerialException as e:
        print(f"Error opening serial port {PORT}: {e}")
        return

    counter = 0
    try:
        while True:
            # Prepare the numeric string and send it
            msg = f"{counter}\n"
            ser.write(msg.encode('utf-8'))
            print(f"sent → {counter}")
            
            # Increment or generate next value
            counter += 1
            
            # Wait before sending the next reading
            time.sleep(SEND_INTERVAL)

    except KeyboardInterrupt:
        print("\nSimulator stopped by user.")
    finally:
        ser.close()

if __name__ == "__main__":
    main()

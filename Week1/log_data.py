#!/usr/bin/env python3
"""
log_data.py

Reads numeric data from an ESP32 (or simulator) over serial every two seconds,
timestamps each reading in UTC, and appends to cansatdata.csv.
"""

import os
import csv
import time
from datetime import datetime
import serial

# ----------------------------------------------------------------------
# CONFIGURATION
# ----------------------------------------------------------------------

# Serial port to listen on (adjust to your socat or actual COM port)
PORT = "/dev/pts/6"
# Baud rate must match ESP32's serial configuration
BAUD = 9600

# CSV filename
CSV_FILE = "cansatdata.csv"

# Interval between readings (in seconds)
READ_INTERVAL = 2


def ensure_csv_header(csv_path):
    """
    Create the CSV file with header if it doesn't already exist.
    """
    if not os.path.isfile(csv_path):
        with open(csv_path, mode='w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["timestamp_utc", "value"])
        print(f"Created new CSV file with header: {csv_path}")


def main():
    # Ensure CSV exists with header
    ensure_csv_header(CSV_FILE)

    # Open serial port
    try:
        ser = serial.Serial(PORT, BAUD, timeout=5)
        print(f"Listening on {PORT} @ {BAUD} baud. Logging to {CSV_FILE}")
    except serial.SerialException as e:
        print(f"Error opening serial port {PORT}: {e}")
        return

    # Open CSV for appending
    try:
        with open(CSV_FILE, mode='a', newline='') as csvfile:
            writer = csv.writer(csvfile)

            while True:
                # Read one line from serial (blocking up to timeout)
                raw = ser.readline().decode('utf-8', errors='ignore').strip()

                # If the line contains a numeric value, log it
                if raw.isdigit():
                    # Get current UTC timestamp in ISO format
                    ts = datetime.utcnow().isoformat()
                    # Write row and flush to disk immediately
                    writer.writerow([ts, raw])
                    csvfile.flush()
                    print(f"{ts} → {raw}")
                else:
                    # Non-numeric lines are ignored (you could log them or warn)
                    if raw:
                        print(f"Ignored non-numeric data: {raw}")

                # Wait before next reading
                time.sleep(READ_INTERVAL)

    except KeyboardInterrupt:
        print("\nInterrupted by user. Exiting.")
    finally:
        ser.close()


if __name__ == "__main__":
    main()

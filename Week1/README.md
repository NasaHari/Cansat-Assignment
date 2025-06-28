
# Cansat Communications — Week 1

## ✅ Prerequisites

- **Python 3.x**
- Install Python dependencies:
  ```bash
  pip install pyserial


 **Linux**: install `socat` to create virtual serial ports:

  ```bash
  sudo apt-get install socat
  ```

---

## 🔌 Virtual Serial Port Setup (Linux)

1️⃣ In one terminal, run:

```bash
socat -d -d pty,raw,echo=0 pty,raw,echo=0
```

2️⃣ You’ll see output like:

```
2025/06/28 10:15:01 socat[12345] N PTY is /dev/pts/6
2025/06/28 10:15:01 socat[12345] N PTY is /dev/pts/7
```

3️⃣ These two device names form a linked pair:

* `/dev/pts/6` ↔ `/dev/pts/7`

Leave this terminal running while you test the scripts.

---

## ⚙️ Script Configuration

* **Simulators (write side)**
  In `sim_data_sender.py` and `sim_led_device.py`, set:

  ```python
  PORT = "/dev/pts/6"  # write side of the pair
  BAUD = 9600
  ```

* **Readers / Controllers (read side)**
  In `log_data.py`, `recv_data.py`, and `controller.py`, set:

  ```python
  PORT = "/dev/pts/7"  # read side of the pair
  BAUD = 9600
  ```

✅ **Always check your `/dev/pts/X` numbers — they can change if you restart `socat`.**

---

## ▶️ Running the Scripts

Open **separate terminals** for each process:

1. **Simulate numeric data sending:**

   ```bash
   python3 sim_data_sender.py
   ```

2. **Log data to CSV:**

   ```bash
   python3 log_data.py
   ```

3. **Simulate ESP32 LED responder (optional):**

   ```bash
   python3 sim_led_device.py
   ```

4. **Run the controller to send ON/OFF commands (optional):**

   ```bash
   python3 controller.py
   ```

---

## 📂 Repository Structure

```
Cansat-Assignment/
└── Week1/
    ├── sim_data_sender.py
    ├── log_data.py
    ├── sim_led_device.py
    ├── controller.py
    └── recv_data.py
```

---

## 📝 Notes

* Ensure each script’s `PORT` matches your active `socat` ports.
* The `cansatdata.csv` file is auto-created and appended by `log_data.py`.
* Use **CTRL+C** to stop any script safely.


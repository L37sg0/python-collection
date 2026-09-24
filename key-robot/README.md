# key-robot (Robo Support)

A specialized desktop keyboard automation and macro robot built using Python, Tkinter, and `pynput` to handle automated server maintenance scripts, provisionings, and system restarts.

Originally engineered during night-shift technical support duties for a cable television provider to automate DHCP server reboots during heavy end-of-month subscription payment peaks—preventing network dropouts and saving valuable sleep time without emergency pager interruptions.

---

## Architecture & Core Features

* 🤖 **Automated Macro Execution (`robo` class):**
    * Sends configured keyboard commands automatically using the `pynput.keyboard` controller.
    * Handles automated keystroke sequences including typing text strings and sending control actions like `Enter`.


* ⏱️ **Timing & Scheduling Control:**
    * Configurable total running duration (in minutes) and repetition intervals (in seconds).
    * Utilizes asynchronous `after` scheduling loops combined with manual `Start`/`Stop` handlers to maintain responsive GUI states during automation.


* 🖥️ **Graphical User Interface (Tkinter):**
    * Features an intuitive configuration panel with input fields for total time, interval timing, and custom command strings, accompanied by built-in operator instructions.


* 📦 **Standalone Executable Packaging:**
    * Includes build configurations and spec files (`key-robot.spec`) for compiling into a standalone Windows executable (`dist/key-robot.exe`).



---

## Project Structure

```text
key-robot/
├── build/                  # PyInstaller build artifacts and logs
├── dist/                   # Compiled distribution binaries (key-robot.exe)
├── key-robot.py            # Main application script (GUI and keyboard macro controller)
├── key-robot.spec          # PyInstaller packaging specification file
├── README.md               # Project documentation
├── robot.ico               # Application window icon asset
├── robot.jpg               # Companion illustration image asset
└── test.py                 # Tkinter asynchronous counter prototype script

```

---

## Tech Stack & Libraries

* **Language:** Python 3
* **GUI Framework:** Tkinter (`tkinter`, `ttk`)
* **Automation / Input Control:** `pynput` (`pynput.keyboard.Controller`, `Key`)
* **Compilation Tool:** PyInstaller (`key-robot.spec`)
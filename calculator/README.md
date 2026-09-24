# calculator (Python Tkinter Calculator)

A classic desktop calculator application built using Python's **Tkinter** GUI library and `ttk` widgets, featuring a custom state machine, event router, and a retro MS Paint UI mockup.

---

## Architecture & Core Features

* 🖥️ **GUI & Grid Layout:**
    * Dynamically generates the keypad using a nested loop over a custom key matrix (`_keys`) and binds buttons via `functools.partial` to route inputs to the central logic.
    * Features a clean entry display label styled with custom fonts and padding.


* 🧠 **State & Brain Logic (`brain`):**
    * Uses a memory dictionary (`mem`) to track operands (`x`, `y`), active mathematical operations (`math`), and input digit sequences (`act`).
    * Implements input validation (handling decimals, character limits, and clearing mechanisms like `AC` and `C`).


* 🔢 **Result & Display Formatting:**
    * Includes custom float handling and string formatting (`display_settings`) to manage large results and scientific notation constraints.
---

## Project Structure

```text
calculator/
├── calculator.png   # Original MS Paint UI mockup design
├── calculator.py    # Main Python script containing GUI and calculation logic
└── README.md        # Project description and future goals

```

---

## Tech Stack

* **Language:** Python 3
* **GUI Framework:** Tkinter (`tkinter`, `ttk`)
* **Utilities:** `functools.partial`
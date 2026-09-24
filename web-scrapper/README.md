# web-scrapper

A dual-mode (Graphical UI and Command Line) Python web scraper utility engineered from Fabrizio Romano's book *Learning Python*. It parses target web pages using **BeautifulSoup**, discovers all embedded image elements, and saves them either directly as files or encoded in JSON format.

---

## Architecture & Core Features

* 🖥️ **Graphical User Interface (`guiscrape.py`):**
    * Built using Python's `tkinter` and `ttk` widget libraries with a fully resizable layout.
    * Features a URL entry field, dynamic scrollable listbox displaying discovered images, status bar messaging, and directory/file dialog pickers.
    * Supports choosing output formats dynamically via radio buttons (**As Images** or **As JSON**).


* ⌨️ **Command-Line Interface (`scrape.py`):**
    * Powered by `argparse` for flexible terminal execution.
    * Supports filtering images by file extension (`--type` options: `all`, `png`, `jpg`) and specifying target formats (`--format` options: `img`, `json`).


* 🔄 **Data Reader & JSON Utilities (`data.reader.py`):**
    * Provides helper scripts to parse and inspect generated base64-encoded JSON image archives (`images.json`).



---

## Project Structure

```text
web-scrapper/
├── data.reader.py          # Helper script for reading and loading generated JSON image dumps
├── guiscrape.py            # Tkinter desktop GUI application script
├── images.json             # Sample or generated Base64-encoded image archive
├── README.md               # Project documentation and feature roadmap
└── scrape.py               # CLI argument parser and scraping engine

```

---

## Tech Stack & Libraries

* **Language:** Python 3
* **GUI Framework:** `tkinter` (`ttk`, `filedialog`, `messagebox`)
* **Web Parsing & Requests:** `requests`, `BeautifulSoup` (`bs4`)
* **Data Serialization:** `json`, `base64`, `argparse`
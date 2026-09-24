# Python Recall & Projects Reference (`python-recall`)

A comprehensive compilation of Python fundamentals, data structures, object-oriented programming, standard modules, and practical utility scripts created following programming tutorials.

---

## Repository Structure

```text
python-recall/
├── CountDownApp/                 # Goal deadline calculator using datetime
│   ├── README.md                 # Countdown application documentation
│   └── time-till-deadline.py     # Script calculating remaining hours/days to a goal
├── GitlabApiIntegration/         # REST API integration script
│   └── main.py                   # Fetches public GitLab user projects via requests
├── WorkingWithSpreadsheets/      # Excel automation and data extraction
│   ├── inventory.xlsx            # Source inventory data sheet
│   ├── inventory_with_total_value.xlsx # Processed output sheet with calculated totals
│   ├── main.py                   # Spreadsheet parsing and modification script
│   └── README.md                 # Spreadsheet automation documentation
├── helper.py                     # Validation and unit-conversion helper functions
├── lists.py                      # Examples of list data structures and indexing
├── main.py                       # Core learning script covering basic to intermediate concepts
├── oop.py                        # Object-oriented programming implementation tests
├── post.py                       # Post class definition for user modeling
├── user.py                       # User class blueprint with instance methods
├── sets.py                       # Set operations and uniqueness rules demonstration
└── README.md                     # Main repository overview

```

---

## Core Modules & Concepts Covered

* **Basic Syntax & Data Types:** Strings, integers, floats, booleans, and type casting.
* **Collections:** Lists (ordered, indexed, allow duplicates), Sets (unordered, unique items), and Dictionaries (key-value mapping).
* **Control Flow & Error Handling:** `if/elif/else` conditionals, `while` loops, `for` loops, and `try/except` blocks for runtime exception management.
* **Functions & Scope:** Modularizing logic, passing parameters, returning values, and variable scope rules.
* **Modules & Packages:** Creating custom modules, importing specific functions or whole files, and utilizing built-in libraries (`logging`, `os`, `datetime`).
* **Object-Oriented Programming (OOP):** Defining classes, utilizing constructors (`__init__`), managing instance state via `self`, and implementing methods.
* **Third-Party Integrations:**
* **Requests:** Fetching and parsing JSON data from remote REST endpoints (GitLab API).
* **OpenPyXL:** Reading, writing, and updating spreadsheet cells for automated data processing.
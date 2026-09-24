# django-polls (Reusable Web Polling Application)

A simple, reusable Django web application built following the official Django tutorial to conduct web-based polls, packaged as an installable Python module (`setuptools`).

---

## Architecture & Core Features

* 📦 **Reusable Package Design:** Configured with `setup.py` and `MANIFEST.in` for easy distribution and installation across Django projects (distributed as `dist/django-polls-0.1.tar.gz`).
* 🗳️ **Polling Core (`polls/`):**
* **Models (`models.py`):** Defines question and choice structures with built-in Django Admin integration (`admin.py`).
* **Views & Templates (`views.py`, `templates/polls/`):** Dynamic views rendering index, question details, and live voting results.
* **Custom Styling:** Includes a dedicated static stylesheet (`style.css`) and background imagery (`background.jpg`).


* 🧪 **Testing:** Comprehensive test suite (`tests.py`) ensuring model and view reliability.

---

## Project Structure

```text
django-polls/
├── dist/                   # Distribution archives (.tar.gz)
├── django_polls.egg-info/  # Package metadata and dependencies
├── polls/                  # Core polling application package
│   ├── migrations/         # Database initial migration files
│   ├── static/polls/       # Custom CSS and background assets
│   ├── templates/polls/    # HTML templates (detail, index, results)
│   ├── admin.py            # Admin dashboard configuration
│   ├── apps.py             # App configuration
│   ├── models.py           # Question and Choice data models
│   ├── tests.py            # Unit and integration tests
│   ├── urls.py             # App-level URL routing
│   └── views.py            # Request handler views
├── LICENSE                 # BSD License agreement
├── MANIFEST.in             # Package file manifest
├── README.rst              # Official package quickstart documentation
└── setup.py                # Setuptools installation script

```

---

## Quick Start Guide

- **Install the package** in your Django project environment (or include it in your project path).
- Add `polls` to your `INSTALLED_APPS` setting in `settings.py`:
```python
INSTALLED_APPS = [
    ...
    'polls',
]

```


- Include the polls URLconf in your project's main `urls.py`:
```python
path('polls/', include('polls.urls')),

```


- Run database migrations to create the poll models:
```bash
python manage.py migrate

```


- Start the development server and visit `[http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)` to create your first poll questions.
- Visit `[http://127.0.0.1:8000/polls/](http://127.0.0.1:8000/polls/)` to participate in the voting process.

---

## Tech Stack

* **Framework:** Python, Django
* **Packaging:** Setuptools (`setuptools`, `wheel`)
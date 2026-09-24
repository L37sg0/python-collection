# mysite (Django Base Project)

A standard foundational **Django** project container initialized to manage site-wide settings, URL routing, and custom administrative interface branding.

---

## Architecture & Core Features

* ⚙️ **Project Configuration (`mysite/`):**
    * Contains core setup files including `settings.py` for global configurations, root `urls.py` for request routing, and `wsgi.py` for deployment interfacing.


* 🎨 **Admin Customization (`templates/admin/`):**
    * Features a custom `base_site.html` template override, allowing personalized branding and styling across the built-in Django administration panel.


* 🗄️ **Data Persistence:**
    * Configured with a lightweight SQLite (`db.sqlite3`) database file for local development.



---

## Project Structure

```text
mysite/
├── db.sqlite3              # Local SQLite development database
├── manage.py               # Django command-line management utility
├── mysite/                 # Core project configuration package
│   ├── __init__.py         # Package initialization
│   ├── settings.py         # Global Django settings and installed apps
│   ├── urls.py             # Root URL declarations
│   └── wsgi.py             # WSGI deployment entry point
└── templates/              # Global project templates directory
    └── admin/              # Admin interface overrides
        └── base_site.html  # Custom branded Django admin site template

```

---

## Tech Stack

* **Framework:** Python, Django
* **Database:** SQLite
* **Environment:** Django Management CLI (`manage.py`)
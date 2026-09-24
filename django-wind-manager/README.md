# django-wind-manager (Wind Park Management Application)

A specialized Django web application adapted and evolved from a maritime fleet tracking template into an enterprise management dashboard tailored for wind parks and turbine maintenance operations.

---

## Architecture & Core Modules

* 🌬️ **Turbine Operations (`turbines/`):**
    * Manages wind turbine inventories, status tracking, and operational records via custom database models and iterative migrations (`0001` to `0009`).
    * Powers dedicated dashboard views and templates for **Home**, **Turbines**, **Meteorology**, **Schedules**, **Documents**, and **Contacts**.


* ⚓ **Legacy Fleet Remnants (`boats/`):**
    * Preserves historical database structures and migration histories from the original boat tracking template, iteratively refactored and adapted toward wind energy assets.


* 👤 **User Management & Authentication (`users/`):**
    * Handles user accounts, permissions, registration workflows (`signup.html`), and authentication pages (`login.html`).


* 🎨 **Dashboard UI & Styling (`static/`, `templates/`):**
    * Styled using **SB Admin 2** dashboard templates and Bootstrap, featuring interactive chart demonstration scripts (Area, Bar, Pie charts) and data table integrations.



---

## Project Structure

```text
django-wind-manager/
├── boats/                  # Legacy fleet tracking models and migration history
├── manage.py               # Django management command-line utility
├── media/                  # User uploads and media assets (wind.jpg)
├── static/                 # Stylesheets, JavaScript charts, and UI theme assets (SB Admin 2)
│   ├── css/                # Bootstrap and SB Admin 2 CSS bundles
│   ├── img/                # UI illustrations and wind media
│   └── js/                 # Bootstrap bundles and demo chart/table scripts
├── templates/              # HTML template hierarchy
│   ├── registration/       # Login and signup views
│   └── turbines/           # Management views (home, turbines, meteorology, schedules, etc.)
├── turbines/               # Core turbine domain (models, admin, views, migrations)
├── users/                  # User authentication and profile management module
└── WindManager/            # Central project settings, root routing, and WSGI configuration

```

---

## Tech Stack

* **Framework:** Python, Django
* **Frontend Admin Theme:** SB Admin 2, Bootstrap, jQuery
* **Data Visualization:** Chart.js (Area, Bar, Pie charts)
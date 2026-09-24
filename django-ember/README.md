# django-ember (My Library - Fullstack Application)

A full-stack library web application pairing a **Django** REST API backend with an **Ember.js** frontend, built following the popular tutorial *[ELI5 Full-Stack Basics: Breakthrough with Django & Ember.js](https://medium.freecodecamp.org/eli5-full-stack-basics-breakthrough-with-django-emberjs-402fc7af0e3?utm_source=gemini)*.

---

## Architecture & Core Features

* 🔌 **API-Driven Backend (`server/`):**
    * Powered by Django and structured around a dedicated `books` module.
    * Utilizes custom serializers, views, and dedicated API routing to expose endpoints for library management.
    * Uses SQLite (`db.sqlite3`) for lightweight data persistence during development.


* 💻 **Modern Frontend Client (`client/`):**
    * Built with Ember.js to deliver a reactive single-page application (SPA) experience communicating seamlessly with the Django backend API.



---

## Project Structure

```text
django-ember/
├── client/                 # Ember.js frontend client application
└── server/                 # Django backend application
    ├── books/              # Library domain app (models, serializers, API views, URLs)
    │   ├── api/            # API serializers, views, and routing endpoints
    │   ├── migrations/     # Database migration files
    │   ├── admin.py        # Django administration configurations
    │   ├── models.py       # Data models (e.g., Book entities)
    │   └── views.py        # Template/app views
    ├── server/             # Django project configuration (settings, WSGI, main URLs)
    ├── db.sqlite3          # Local SQLite development database
    └── manage.py           # Django command-line utility interface

```

---

## Tech Stack

* **Backend:** Python, Django, Django REST API patterns
* **Frontend:** Ember.js
* **Database:** SQLite
* **Reference Tutorial:** [ELI5 Full-Stack Basics: Breakthrough with Django & Ember.js](https://medium.freecodecamp.org/eli5-full-stack-basics-breakthrough-with-django-emberjs-402fc7af0e3?utm_source=gemini)
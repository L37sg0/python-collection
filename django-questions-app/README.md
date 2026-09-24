# django-questions-app (Questions API & Web Backend)

A full-stack quiz and question management application pairing a modular Django backend with a standalone Bootstrap-powered frontend client (`client-app-js`).

---

## Architecture & Core Layers

* 🗄️ **ORM & Data Layer (`questions/`):**
    * Manages question schemas, models, and comprehensive database migrations (`0001` through `0009`).
    * Implements dedicated API serializers and routers (`questions/api/`) to expose RESTful endpoints.


* ⚙️ **Middleware & Configuration (`root/`):**
    * Handles core Django settings, project-level routing, and WSGI deployment bindings.
    * Includes deployment configurations (`Procfile`, `Procfile.windows`, `runtime.txt`, `requirements.txt`) for cloud environments like Heroku.


* 🖥️ **UI & Frontend Layer (`frontend-url-app/` & `client-app-js/`):**
    * **`frontend-url-app/`**: Django-managed template views serving server-rendered HTML (`home.html`).
    * **`client-app-js/`**: A static standalone frontend client leveraging Bootstrap 5 and custom assets (`quest.jpg`, `index.html`) to interact with the backend services.



---

## Project Structure

```text
django-questions-app/
├── client-app-js/          # Standalone frontend client (Bootstrap 5, custom JS/assets)
├── db.sqlite3              # Local SQLite database
├── frontend-url-app/       # Django template/view layer for frontend routing
├── manage.py               # Django management CLI utility
├── Procfile                # Heroku deployment process file
├── Procfile.windows        # Windows process file configuration
├── questions/              # Core question domain & REST API serializers
│   ├── api/                # DRF serializers, views, and routing
│   └── migrations/         # Iterative database migration history
├── root/                   # Project configuration (settings, root URLs, WSGI)
├── requirements.txt        # Python dependency manifest
├── runtime.txt             # Python runtime specification
└── README.md               # Project description

```

---

## Tech Stack

* **Backend:** Python, Django, Django REST API patterns
* **Frontend / Client:** Vanilla JavaScript, HTML5, Bootstrap 5
* **Deployment & Tooling:** Heroku (`Procfile`), SQLite
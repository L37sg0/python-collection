# django-react (Full-Stack Django & React Application)

A full-stack web application integrating a **Django REST Framework (DRF)** backend with a **ReactJS** frontend client, featuring user authentication handled directly through the frontend interface.

---

## Architecture & Core Layers

* ⚙️ **Django DRF Backend (`backend/`):**
* **API Module (`backend/api/`):** Houses models, custom views, and URL routers to supply structured data to the frontend.
* **Project Core (`backend/backend/`):** Manages global settings, WSGI integration, and root URL routing.


* ⚛️ **Frontend Client (`frontend/`):**
    * Dedicated single-page application directory structured for React components and user authentication flows.



---

## Project Structure

```text
django-react/
├── backend/                # Django backend application
│   ├── api/                # API domain app (models, views, routers)
│   ├── backend/            # Project configuration (settings, URLs, WSGI)
│   └── manage.py           # Django management CLI utility
├── frontend/               # ReactJS frontend client application
├── npm-debug.log           # NPM error logging artifact
├── README.md               # Project documentation and starter template
└── requirements.txt        # Python backend dependencies

```

---

## Getting Started & Quick Start
- **Activate the environment** or install Python dependencies:
```bash
pip install -r requirements.txt

```


- **Run the backend development server**:
```bash
python backend/manage.py runserver

```


- **Access the application** by visiting `http://localhost:8000/` in your browser.

---

## Tech Stack

* **Backend:** Python, Django 2.1.3, Django REST Framework 3.9.0
* **Frontend:** ReactJS
* **Tooling:** Pip, NPM
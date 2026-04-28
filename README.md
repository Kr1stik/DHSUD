---
# DHSUD Tracker - Negros Island Region

A comprehensive web-based tracking system built for the Department of Human Settlements and Urban Development (DHSUD) Negros Island Region. This system manages project applications, Certificates of Registration (CR), Licenses to Sell (LS), and compliance records with built-in analytics and bulk processing features.

# 🏛️ DHSUD HOA Management System

A comprehensive, offline-ready Homeowners Association (HOA) Management System designed for the Department of Human Settlements and Urban Development (DHSUD). This system manages HOA profiles, compliance orders, legal workflows, and event scheduling, with a complete audit trail built specifically for LAN deployment.

## ✨ Features

* **📊 Interactive Dashboard**: Real-time statistics, active HOA counts, and a dynamic scheduling calendar.
* **📋 HOA Registry**: Complete HOA profile management (Location, Contact, Governance, Status).
* **⚖️ Legal Workflow Modules**: 
    * Notice of Violation (NOV)
    * Order to Perform (OTP)
    * Order for Investigation (OIAS)
* **🛑 Sanctions & Penalties**: Built-in 6-point severity scale management.
* **📦 Archive System**: Soft-delete functionality for all database entities ensures no data is accidentally destroyed.
* **🔌 Offline Capable**: Designed to run on a local government LAN without requiring internet access.

## 🛠️ Tech Stack

**Frontend:**
* Vue.js 3 (Composition API)
* TypeScript
* Vite (Bundler)
* Tailwind CSS v4 (Styling)
* Lucide Vue Next (Icons)

**Backend:**
* Python / Django
* Django REST Framework (DRF)
* SQLite (Offline Database)
* Django CORS Headers

* **Frontend:** React, TypeScript, Tailwind CSS, Vite, Recharts, SheetJS (XLSX)
* **Backend:** Python, Django, Django REST Framework
* **Database:** PostgreSQL

---

## 📋 Prerequisites

Before you begin, ensure you have the following installed on your local machine:
* [Python 3.10+](https://www.python.org/downloads/)
* [Node.js v18+](https://nodejs.org/) & npm
* [PostgreSQL](https://www.postgresql.org/download/)
* Git

---

## 🚀 Installation Guide (Windows)

### Prerequisites
Make sure you have the following installed on your machine:
* [Python 3.10+](https://www.python.org/downloads/)
* [Node.js (LTS)](https://nodejs.org/en/)

### 1. Backend Setup (Django API)

Open your terminal and navigate to the root directory of the project, then enter the `backend` folder:

```cmd
cd backend
Create and activate a Python virtual environment:

DOS
python -m venv venv
venv\Scripts\activate
Install the required Python packages:

DOS
pip install django djangorestframework django-cors-headers
Set up the SQLite database and run migrations:

DOS
python manage.py makemigrations
python manage.py migrate
Create an admin account (Superuser) to access the Django admin panel:

DOS
python manage.py createsuperuser
(Follow the prompts to set your username and password).

Start the backend server:

DOS
python manage.py runserver
The backend API is now running at http://127.0.0.1:8000/

2. Frontend Setup (Vue/Vite)
Open a new, separate terminal window (leave the backend running), navigate to the root directory, and enter the frontend folder:

DOS
cd frontend
Install the Node.js dependencies:

DOS
npm install
npm install lucide-vue-next
Start the Vite development server:

DOS
npm run dev
The frontend interface is now running at http://localhost:5173/

✨ Key Features
Interactive Dashboard: Real-time analytics using Recharts (Bar and Donut charts) to visualize project types and application statuses.

Bulk Processing: Select multiple records at once to batch archive, restore, or permanently delete projects.

Excel Import/Export: Seamlessly map and export database records to the exact DHSUD-formatted Excel template using SheetJS.

Search & Filter: Instantly filter records by status, project name, or location.

🤝 Contributing
Create your Feature Branch (git checkout -b feature/AmazingFeature)

Commit your Changes (git commit -m 'Add some AmazingFeature')

Push to the Branch (git push -u origin feature/AmazingFeature)

Open a Pull Request

📂 Project Structure
Plaintext
dhsud_system/
│
├── backend/                  # Django API & SQLite Database
│   ├── core/                 # Main Django settings & routing
│   ├── HoaRegistry/          # Database models, serializers, and views
│   ├── manage.py             # Django entry point
│   └── db.sqlite3            # Local Database file
│
└── frontend/                 # Vue 3 + TypeScript UI
    ├── src/
    │   ├── assets/           # Logos and static images
    │   ├── components/       # Reusable UI (Sidebar)
    │   ├── views/            # Main pages (Dashboard, HOA Registry)
    │   ├── App.vue           # Main layout wrapper
    │   └── main.ts           # Vue initialization
    ├── tailwind.config.js    # Tailwind configuration
    └── package.json          # Node dependencies
🌐 Offline LAN Deployment Note
To deploy this application to a local network server:

Update the fetch() API calls in the Vue frontend from http://127.0.0.1:8000/... to the server's static IP address (e.g., http://192.168.1.100:8000/...).

Build the frontend using npm run build.

Serve the resulting /dist folder using a static file server (like Nginx or Apache) on the host machine.

Run the Django backend on the host machine using Gunicorn or Waitress bound to 0.0.0.0:8000.

## 🛠️ Tech Stack

**Frontend:**
* Vue.js 3 (Composition API)
* TypeScript
* Vite (Bundler)
* Tailwind CSS v4 (Styling)
* Lucide Vue Next (Icons)

**Backend:**
* Python / Django
* Django REST Framework (DRF)
* SQLite (Offline Database)
* Django CORS Headers

---

## 🚀 Installation Guide (Windows)

### Prerequisites
Make sure you have the following installed on your machine:
* [Python 3.10+](https://www.python.org/downloads/)
* [Node.js (LTS)](https://nodejs.org/en/)

### 1. Backend Setup (Django API)

Open your terminal and navigate to the root directory of the project, then enter the `backend` folder:

```cmd
cd backend
Create and activate a Python virtual environment:

DOS
python -m venv venv
venv\Scripts\activate
Install the required Python packages:

DOS
pip install django djangorestframework django-cors-headers
Set up the SQLite database and run migrations:

DOS
python manage.py makemigrations
python manage.py migrate
Create an admin account (Superuser) to access the Django admin panel:

DOS
python manage.py createsuperuser
(Follow the prompts to set your username and password).

Start the backend server:

DOS
python manage.py runserver
The backend API is now running at http://127.0.0.1:8000/

2. Frontend Setup (Vue/Vite)
Open a new, separate terminal window (leave the backend running), navigate to the root directory, and enter the frontend folder:

DOS
cd frontend
Install the Node.js dependencies:

DOS
npm install
npm install lucide-vue-next
Start the Vite development server:

DOS
npm run dev
The frontend interface is now running at http://localhost:5173/

📂 Project Structure
Plaintext
dhsud_system/
│
├── backend/                  # Django API & SQLite Database
│   ├── core/                 # Main Django settings & routing
│   ├── HoaRegistry/          # Database models, serializers, and views
│   ├── manage.py             # Django entry point
│   └── db.sqlite3            # Local Database file
│
└── frontend/                 # Vue 3 + TypeScript UI
    ├── src/
    │   ├── assets/           # Logos and static images
    │   ├── components/       # Reusable UI (Sidebar)
    │   ├── views/            # Main pages (Dashboard, HOA Registry)
    │   ├── App.vue           # Main layout wrapper
    │   └── main.ts           # Vue initialization
    ├── tailwind.config.js    # Tailwind configuration
    └── package.json          # Node dependencies
🌐 Offline LAN Deployment Note
To deploy this application to a local network server:

Update the fetch() API calls in the Vue frontend from http://127.0.0.1:8000/... to the server's static IP address (e.g., http://192.168.1.100:8000/...).

Build the frontend using npm run build.

Serve the resulting /dist folder using a static file server (like Nginx or Apache) on the host machine.

Run the Django backend on the host machine using Gunicorn or Waitress bound to 0.0.0.0:8000.

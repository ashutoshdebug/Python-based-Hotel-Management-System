# Python-based Hotel Management System (PBHMS)

A complete Django-based Hotel Management System with guest management, room management, billing, services tracking, Tailwind CSS styling, and a clean UI.

### Live Deployment: Hosted on Render (Gunicorn + Whitenoise + Tailwind)

### Features
* Guest Management
* Check-In / Check-Out process
* Store guest details
* Automatic duration calculation
* Aadhaar & mobile validation
* Room Management
* Room type management (AC, Non-AC, Deluxe, Suite, etc.)
* Real-time availability
* Pricing integrations
* Billing System
* Generate automatic bills
* Food, bottles, services, room cost
* Error-free bill summary

### Extra Services

* Laundry
* Room services
* Food orders

### Frontend

* Styled using Tailwind CSS
* Custom theme located inside /theme


### Project Structure
```bash
pbhms/
│── billing/
│── dashboard/
│── guests/
│── rooms/
│── services/
│── static/
│── templates/
│── theme/
│── manage.py
│
└── pbhms/
    ├── settings.py
    ├── urls.py
    ├── wsgi.py
    └── asgi.py
```

- Standard Django project
- Tailwind CSS integrated under /theme/
- Static files served using Whitenoise

### Tech Stack
|Component 	  |  Technology                           |
|-------------|---------------------------------------|
|Backend	    |  Django 5.x                           |
|Frontend	    |  HTML, Tailwind CSS                   |
|DB	          |  SQLite (local) / PostgreSQL (Render) |
|Deployment	  |  Render Web Service                   |
|Static Files	|  Whitenoise                           |
|Server	      |  Gunicorn                             |


### Installation (Local Setup)
#### 1️⃣ Clone the repo
```bash
git clone https://github.com/ashutoshdebug/Python-based-Hotel-Management-System.git
cd Python-based-Hotel-Management-System/pbhms
```

#### 2️⃣ Create and activate a virtual environment
```bash
python -m venv venv
source venv/bin/activate         # Mac/Linux
venv\Scripts\activate            # Windows
```
#### 3️⃣ Install dependencies
```bash
pip install -r ../requirements.txt
```
#### 4️⃣ Run database migrations
```bash
python manage.py migrate
```

5️⃣ Start development server
```bash
python manage.py runserver
```

### Tailwind Setup

Tailwind is installed inside the theme app.
To rebuild Tailwind CSS:
```bash
cd theme
npm install
npm run dev
```

### Deployment (Render)
Build Command:
```bash
cd pbhms && pip install -r ../requirements.txt && python manage.py collectstatic --noinput
```

Start Command:
```bash
cd pbhms && gunicorn pbhms.wsgi:application
```

### Environment Variables
- Key	Value
- SECRET_KEY	(secure generated key)
- DEBUG	False
- RENDER	True
- PYTHON_VERSION	3.12

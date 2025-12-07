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
    ├── billing/
        ├── migrations/
            └── migration files...
        ├── templates/
            └── billing.html
        ├── __init__.py
        ├── admin.py
        ├── apps.py
        ├── forms.py
        ├── models.py
        ├── tests.py
        ├── urls.py
        └── views.py
    ├── dashboard/
        ├── migrations/
            └── migration files...
        ├── templates/
            └── dashboard.html
        ├── __init__.py
        ├── admin.py
        ├── apps.py
        ├── models.py
        ├── tests.py
        ├── urls.py
        └── views.py
    ├── guests/
        ├── migrations/
            └── migration files...
        ├── templates/
            ├── guesthandling/
                ├── checkin.html
                └── checkout.html
            └── guests.html
        ├── __init__.py
        ├── admin.py
        ├── apps.py
        ├── forms.py
        ├── models.py
        ├── tests.py
        ├── urls.py
        └── views.py
    ├── pbhms/
        ├── __init__.py
        ├── admin.py
        ├── asgi.py
        ├── settings.py
        ├── urls.py
        ├── views.py
        └── wsgi.py
    ├── rooms/
        ├── migrations/
            └── migration files...
        ├── templates/
            └── rooms.html
        ├── __init__.py
        ├── admin.py
        ├── apps.py
        ├── models.py
        ├── tests.py
        ├── urls.py
        └── views.py
    ├── services/
        ├── migrations/
            └── migration files...
        ├── templates/
            └── services.html
        ├── __init__.py
        ├── admin.py
        ├── apps.py
        ├── models.py
        ├── tests.py
        ├── urls.py
        └── views.py
    ├── static/
        ├── css/
            └── style.css
        ├── img/
            ├── AC.jpg
            ├── deluxe.jpg
            ├── Hero_img.png
            ├── image.png
            ├── Non-AC.jpg
            └── suite.jpg
        └── videos/
            └── hero_video.mp4
    ├── templates/
        └── website/
            └── index.html
    ├── theme/
        ├── static/
            └── css/
                └── dist/
                    └── styles.css
        ├── static_src/
            ├── src/
                └── styles.css
            ├── .gitignore
            ├── package-lock.json
            ├── package.json
            └── postcss.config.js
        ├── templates/
            └── base.html
        ├── __init__.py
        └── apps.py
    ├── manage.py
    └── requirements.txt
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

### Environment Variables
| Key | Value |
|---|-------|
| SECRET_KEY | (secure generated key)|
| DEBUG | False |
| RENDER | True |
| PYTHON_VERSION | 3.12 |

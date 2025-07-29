# Hotel Management System

A simple Python-based Room Management System that uses **MySQL** for backend data storage. This system allows you to:

- Create and manage a hotel room database.
- Add or delete tables and columns.
- Check-in and check-out guests.
- Manage guest details and billing.
- Initialize discounts and services.
- Add or delete individual table columns dynamically.

---

## Features

- Create and drop the database `ROOM_MANAGEMENT_SYSTEM`
- Create `CHECK_IN` and `CHECK_OUT` tables if they do not exist
- Delete specific tables or the entire database
- Add or delete columns dynamically from existing tables
- Modular and OOP-based design

---

## Technologies Used

- Python 3
- MySQL (via `mysql-connector-python`)

---

## Project structure
room-management-system/
│
├── Main_Program.py                    # Main control file
├── Create_database_Room_Managememt_System.py                 # Database creation file
├── ReadMe.md         # Project overview

---
## Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/your-username/room-management-system.git
cd room-management-system

---

## Install dependencies 
```bash
pip install mysql-connector-python

---

## Run the program 
```bash
python main.py

---


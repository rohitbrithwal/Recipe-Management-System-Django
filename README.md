# 🍽️ Django Recipe Management System

A Recipe Management Web Application built using Django with secure user authentication, recipe CRUD operations, image uploads, and OTP-based password reset via Gmail SMTP.

---

## 🚀 Features

- 👤 User Registration & Login
- 🔐 Secure Authentication
- 🚪 Logout Functionality
- 🍽️ Add Recipes
- ✏️ Update Recipes
- ❌ Delete Recipes
- 🖼️ Recipe Image Upload
- 👨‍🍳 User-specific Recipes (Each user can only view and manage their own recipes)
- 📧 Forgot Password using Gmail SMTP
- 🔢 OTP Verification
- ⏳ OTP Expiry (5 Minutes)
- 🔒 Secure Password Reset
- 💬 Bootstrap UI
- 🗂️ Session-based Authentication

---

## 🛠️ Tech Stack

- Python
- Django
- SQLite3
- HTML5
- Bootstrap 5
- Gmail SMTP

---

## 📂 Project Structure

```
core/
│
├── account/
├── vege/
├── home/
├── media/
├── templates/
├── db.sqlite3
├── manage.py
└── README.md
```

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/your-username/Django-Recipe-Management-System.git
```

Move into project directory

```bash
cd Django-Recipe-Management-System
```

Create virtual environment

```bash
python -m venv venv
```

Activate environment

Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run migrations

```bash
python manage.py migrate
```

Start server

```bash

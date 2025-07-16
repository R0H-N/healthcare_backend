
---

````markdown
````
# 🏥 Healthcare Backend API

A secure and scalable RESTful backend for managing patients, doctors, and their relationships. Built with Django, Django REST Framework (DRF), PostgreSQL, JWT Authentication, and containerized using Docker.

---

## 📦 Features

- ✅ **User registration and JWT authentication**
- ✅ **Secure CRUD APIs** for Patients and Doctors
- ✅ **Doctor-to-Patient assignment**
- ✅ **PostgreSQL for production-ready DB**
- ✅ **Environment variable support via `.env`**
- ✅ **Fully Dockerized**
- ✅ **Ready for CI/CD & DevOps**

---

## ⚙️ Tech Stack

| Layer        | Tech                     |
|--------------|--------------------------|
| Backend      | Django 5 + DRF           |
| Auth         | JWT via `djangorestframework-simplejwt` |
| Database     | PostgreSQL               |
| DevOps       | Docker, Docker Compose   |
| API Testing  | Postman                  |

---


## 🚀 Local Development Setup

### 1. Clone the repo

```bash
git clone https://github.com/your-username/healthcare-backend.git
cd healthcare-backend


### 2. Add a `.env` file

Create `.env` in the root:

```env
# .env
SECRET_KEY=your_super_secret_key
DEBUG=True

DB_NAME=healthcare_db
DB_USER=healthcare_user
DB_PASSWORD=strongpassword
DB_HOST=db
DB_PORT=5432
```

> ✅ Note: `.env` is excluded from Git tracking via `.gitignore`.

---

## 🐳 Docker-Based Setup

### 1. Build & Run containers

```bash
docker compose up --build
```

### 2. Apply Migrations

In a new terminal tab:

```bash
docker compose exec web python manage.py migrate
```

### 3. (Optional) Create Superuser

```bash
docker compose exec web python manage.py createsuperuser
```

---

## 🧪 API Testing via Postman

Base URL: `http://localhost:8000/api/`

---

## 🔐 Authentication APIs

### ➕ Register

**POST** `/auth/register/`

**Request Body**

```json
{
  "name": "John Doe",
  "email": "john@example.com",
  "password": "strongpassword123"
}
```

**Response**

```json
{
  "message": "User registered successfully"
}
```

---

### 🔐 Login

**POST** `/auth/login/`

**Request Body**

```json
{
  "email": "john@example.com",
  "password": "strongpassword123"
}
```

**Response**

```json
{
  "access": "JWT_TOKEN_HERE",
  "refresh": "REFRESH_TOKEN"
}
```

---

## 🧑‍⚕️ Patient APIs (JWT Required)

Add `Authorization: Bearer <access_token>` header.

### ➕ Create Patient

**POST** `/patients/`

```json
{
  "name": "John Doe",
  "age": 30,
  "address": "123 Main St"
}
```

---

### 📥 List Patients

**GET** `/patients/`

---

### 🔍 Retrieve Patient

**GET** `/patients/<id>/`

---

### ✏️ Update Patient

**PUT** `/patients/<id>/`

```json
{
  "name": "John Updated",
  "age": 35,
  "address": "456 New Ave"
}
```

---

### ❌ Delete Patient

**DELETE** `/patients/<id>/`

---

## 🩺 Doctor APIs (JWT Required)

### ➕ Create Doctor

**POST** `/doctors/`

```json
{
  "name": "Dr. Smith",
  "specialization": "Cardiologist"
}
```

---

### 📥 List Doctors

**GET** `/doctors/`

---

### 🔍 Retrieve Doctor

**GET** `/doctors/<id>/`

---

### ✏️ Update Doctor

**PUT** `/doctors/<id>/`

```json
{
  "name": "Dr. Updated",
  "specialization": "Neurologist"
}
```

---

### ❌ Delete Doctor

**DELETE** `/doctors/<id>/`

---

## 🔗 Patient-Doctor Mapping APIs

### ➕ Assign Doctor to Patient

**POST** `/mappings/`

```json
{
  "patient": 1,
  "doctor": 2
}
```

---

### 📥 List All Mappings

**GET** `/mappings/`

---

### 🔍 Get All Doctors for a Patient

**GET** `/mappings/<patient_id>/`

---

### ❌ Remove a Doctor from a Patient

**DELETE** `/mappings/<mapping_id>/`

---

## 📄 API Docs

Visit:

```bash
http://localhost:8000/api/
```

DRF browsable API is enabled for easy testing.

---

## 🛠️ Project Structure

```
healthcare_backend/
│
├── api/                    # Core app with views, models, serializers
├── config/                 # Settings & URLs
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .env
└── manage.py
```

---

## ✅ Dockerfile (Summary)

```dockerfile
FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt
COPY . .
CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000"]
```

---

## ✅ docker-compose.yml (Summary)

```yaml
services:
  db:
    image: postgres:15
    env_file:
      - .env
    volumes:
      - postgres_data:/var/lib/postgresql/data
    ports:
      - "5432:5432"

  web:
    build: .
    command: gunicorn config.wsgi:application --bind 0.0.0.0:8000
    volumes:
      - .:/app
    ports:
      - "8000:8000"
    env_file:
      - .env
    depends_on:
      - db

volumes:
  postgres_data:
```

---

## ✅ Best Practices Followed

* `.env` used for secrets (not in Git)
* Gunicorn for production-ready WSGI
* DRF Viewsets + Routers
* JWT auth and permissions
* Separated business logic using serializers
* Dockerized both DB and app
* Ready for CI/CD setup

---

## 📌 Future Improvements (Optional)

* Add Swagger/OpenAPI docs
* Add pagination & filtering
* Set up GitHub Actions CI
* Add rate limiting/throttling
* Deploy on Render/Heroku/AWS

---

## 👨‍💻 Author

Rohan Jangale
Backend Developer | DevOps Enthusiast

---

```


```

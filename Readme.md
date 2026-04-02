# Finance Data Processing Backend

## Overview

This project is a backend system built for managing financial data with role-based access control. It allows users to create and manage financial records (income and expenses) and provides summary insights for a dashboard.

The focus of this project is on clean API design, proper data handling, and enforcing access rules based on user roles.

---

## Tech Stack

* Python (Flask)
* MySQL
* SQLAlchemy (ORM)
* JWT (JSON Web Tokens) for authentication

---

## Features

### User Management

* Create users with different roles
* Roles supported: **admin**, **analyst**, **viewer**
* Access to APIs is controlled based on role

### Authentication

* Login using email
* JWT-based authentication
* Protected routes using token verification

### Financial Records

* Add income and expense entries
* View all records
* Filter records by type or category
* Get a specific record by ID
* Update and delete records

### Dashboard APIs

* Total income
* Total expenses
* Net balance
* Category-wise totals

---

## Role Permissions

* **Admin**

  * Full access (create, update, delete, manage users)

* **Analyst**

  * Can view records and dashboard data

* **Viewer**

  * Read-only access

---

## How to Run the Project

1. Install dependencies:

```id="6o5psq"
pip install flask flask_sqlalchemy pymysql flask-jwt-extended
```

2. Create a MySQL database:

```id="z6nd0h"
CREATE DATABASE finance_db;
```

3. Update database credentials in `config.py`

4. Run the application:

```id="r1i7jq"
python app.py
```

---

## Authentication Flow

1. Create a user (admin)
2. Login using email:

```id="kdpv1c"
POST /login
```

3. You will receive a JWT token

4. Use the token in headers for protected routes:

```id="t9v0tw"
Authorization: Bearer <your_token>
```

---

## API Endpoints

### User APIs

* `POST /users` → Create user
* `GET /users` → Get all users

### Auth

* `POST /login` → Generate JWT token

### Records

* `POST /records` → Create record
* `GET /records` → Get all records (with optional filters)
* `GET /records/<id>` → Get single record
* `PUT /records/<id>` → Update record
* `DELETE /records/<id>` → Delete record

### Dashboard

* `GET /dashboard/summary` → Income, expense, balance
* `GET /dashboard/category` → Category-wise totals

---

## Assumptions

* Authentication is simplified (no password) for this assignment
* Roles are predefined and stored with the user
* JWT is used to carry role information for access control

---

## Possible Improvements

* Add password-based authentication
* Use environment variables for configuration
* Add pagination for large datasets
* Add unit tests
* Deploy the backend to a cloud service

---

## Notes

This project was built as part of a backend assignment to demonstrate understanding of API design, database interaction, and access control. The implementation focuses on clarity and correctness rather than production-level complexity.

# Blog API

This is a simple django blog developed with django rest framework

# Blog API

## Overview

This is a simple Blog API built using Django and Django REST Framework (DRF). The API provides endpoints for managing blog posts, categories, comments, and user authentication.

## Features

- **User authentication** (Register, Login, JWT token support)
- **Blog post management** (Create, Read, Update, Delete)
- **Category management** (Create, List, Retrieve, Update, Delete)
- **Comment system** (Users can comment on blog posts)
- **Pagination & Filtering** for posts
- **Admin panel** for managing users, posts, categories, and comments
- **Dockerized** for easy deployment
- **Swagger API documentation**

## Technologies Used

- **Backend**: Django 4.2, Django REST Framework
- **Database**: PostgreSQL
- **Authentication**: JWT Authentication
- **Cache**: Redis
- **Containerization**: Docker & Docker Compose
- **Web Server**: Gunicorn

---

## Installation

### Prerequisites

- **Python 3.11+**
- **Docker & Docker Compose**

### Setup Instructions

#### 1. Clone the Repository

```sh
git clone https://github.com/your-username/blog-api.git
cd blog-api
```

#### 2. Create a Virtual Environment (Optional)

```sh
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

#### 3. Install Dependencies

```sh
pip install -r requirements.txt
```

#### 4. Set Up Environment Variables

Copy `.env-sample` to `.env` and update the required values.

```sh
cp .env-sample .env
```

#### 5. Run Migrations

```sh
python manage.py migrate
```

#### 6. Create a Superuser (Optional)

```sh
python manage.py createsuperuser
```

#### 7. Run the Development Server

```sh
python manage.py runserver
```

---

## Running with Docker

1. **Build & Start Containers**

```sh
docker-compose up --build
```

2. **Access the API**

- API runs on: [http://127.0.0.1:8000](http://127.0.0.1:8000)
- Admin Panel: [http://127.0.0.1:8000/admin](http://127.0.0.1:8000)
- Swagger Docs: [http://127.0.0.1:8000/api/v1/swagger](http://127.0.0.1:8000/api/v1/swagger)

---

## API Endpoints

### Authentication

| Method | Endpoint               | Description           |
|--------|------------------------|-----------------------|
| POST   | `/api/v1/user/register/` | Register a new user  |
| POST   | `/api/v1/token/`        | Obtain JWT token     |
| POST   | `/api/v1/token/refresh/` | Refresh JWT token   |

### Blog Posts

| Method | Endpoint                | Description                  |
|--------|-------------------------|------------------------------|
| GET    | `/api/v1/post/`         | List all posts               |
| POST   | `/api/v1/post/create/`  | Create a new post            |
| GET    | `/api/v1/post/<slug>/`  | Retrieve post details        |
| PUT    | `/api/v1/post/<slug>/`  | Update a post                |
| DELETE | `/api/v1/post/<slug>/`  | Delete a post                |

### Comments

| Method | Endpoint                                      | Description                        |
|--------|----------------------------------------------|------------------------------------|
| GET    | `/api/v1/post/<slug>/comment/`              | List all comments on a post       |
| POST   | `/api/v1/post/<slug>/comment/create/`       | Add a comment to a post           |
| GET    | `/api/v1/post/<slug>/comment/<id>/`         | Retrieve a specific comment       |
| PUT    | `/api/v1/post/<slug>/comment/<id>/`         | Update a comment                  |
| DELETE | `/api/v1/post/<slug>/comment/<id>/`         | Delete a comment                  |

### Categories

| Method | Endpoint                          | Description                  |
|--------|----------------------------------|------------------------------|
| GET    | `/api/v1/category/<slug>`       | List posts under a category  |
| POST   | `/api/v1/category/create/`      | Create a new category        |
| GET    | `/api/v1/category/detail/<slug>` | Retrieve category details    |
| PUT    | `/api/v1/category/detail/<slug>` | Update a category            |
| DELETE | `/api/v1/category/detail/<slug>` | Delete a category            |

---

## Running Tests

To run the test suite, use:

```sh
python manage.py test
```

---

## Deployment

1. **Prepare your environment**
   - Ensure your `.env` file is correctly configured.
   - Ensure all dependencies are installed.

2. **Build and start the Docker container**

```sh
docker-compose up --build -d
```

3. **Run database migrations**

```sh
docker exec -it <container_id> python manage.py migrate
```

---

## License

This project is licensed under the **MIT License**.

---

## Author

**ArshA**  
Contact: [a_sh1379@yahoo.com](mailto:a_sh1379@yahoo.com)

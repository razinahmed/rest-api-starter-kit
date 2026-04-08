# REST API Starter Kit

<div align="center">

![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-336791?style=for-the-badge&logo=postgresql&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![JWT](https://img.shields.io/badge/JWT-000000?style=for-the-badge&logo=json-web-tokens&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-d82633?style=for-the-badge&logo=sqlalchemy&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

**A production-ready REST API boilerplate with FastAPI, JWT authentication, SQLAlchemy ORM, and Docker support**

Built by [Abdul Rasak V](https://github.com/razinahmed)

</div>

---

## API Architecture Overview

```
┌─────────────────────────────────────────────────────────────┐
│                    CLIENT APPLICATION                       │
│              (Web, Mobile, Desktop)                          │
└──────────────────────┬──────────────────────────────────────┘
                       │ HTTP/REST Requests
                       ▼
        ┌──────────────────────────────┐
        │     FastAPI Application      │
        │  • Route Handlers            │
        │  • Input Validation          │
        │  • Error Responses           │
        └──────────┬───────────────────┘
                   │
        ┌──────────▼──────────┐
        │ JWT Authentication  │
        │ & Authorization     │
        │ (Role-Based Access) │
        └──────────┬──────────┘
                   │
        ┌──────────▼──────────┐
        │   Business Logic    │
        │   (Service Layer)   │
        │   • User Management │
        │   • Item Operations │
        └──────────┬──────────┘
                   │
        ┌──────────▼──────────────────┐
        │   SQLAlchemy ORM            │
        │   • Model Definitions       │
        │   • Query Building          │
        │   • Data Relationships      │
        └──────────┬──────────────────┘
                   │
        ┌──────────▼──────────────────┐
        │    PostgreSQL Database      │
        │  • User Accounts            │
        │  • Items & Data Storage     │
        │  • Persistent State         │
        └─────────────────────────────┘
```

---

## Features

| Feature | Description |
|---------|-------------|
| 🔐 **JWT Authentication** | Secure token-based auth with refresh tokens and role-based access control (RBAC) |
| ⚡ **Async/Await** | Built on async FastAPI for high-performance concurrent request handling |
| 🗄️ **SQLAlchemy ORM** | Modern async ORM with database migrations via Alembic |
| 📚 **Auto-Generated Docs** | Swagger UI and ReDoc documentation automatically generated from code |
| 🐳 **Docker Ready** | Production-ready Docker and Docker Compose configuration |
| ✅ **Comprehensive Testing** | Unit and integration test suite with pytest |
| 🔑 **Environment Config** | 12-factor app configuration with environment-based settings |
| 🛡️ **Input Validation** | Type-safe validation with Pydantic v2 |
| ⚠️ **Error Handling** | Comprehensive exception handling with consistent API responses |
| 📦 **RBAC** | Role-based access control for granular permissions |

---

## Tech Stack

<div align="center">

| Component | Technology | Version |
|-----------|-----------|---------|
| **Framework** | FastAPI | Latest |
| **Language** | Python | 3.9+ |
| **Database** | PostgreSQL | 13+ |
| **ORM** | SQLAlchemy | 2.0+ |
| **Migrations** | Alembic | Latest |
| **Auth** | PyJWT | Latest |
| **Validation** | Pydantic | v2 |
| **Testing** | Pytest | Latest |
| **Container** | Docker & Compose | Latest |
| **Server** | Uvicorn | Latest |

</div>

---

## Project Structure

```
rest-api-starter-kit/
│
├── app/
│   ├── api/
│   │   ├── __init__.py
│   │   ├── routes/
│   │   │   ├── auth.py          # Authentication endpoints
│   │   │   ├── users.py         # User management endpoints
│   │   │   └── items.py         # Item management endpoints
│   │   └── dependencies.py      # Common dependencies
│   │
│   ├── core/
│   │   ├── config.py            # Configuration management
│   │   ├── security.py          # JWT and auth logic
│   │   └── constants.py         # App constants
│   │
│   ├── models/
│   │   ├── user.py              # User database model
│   │   └── item.py              # Item database model
│   │
│   ├── schemas/
│   │   ├── user.py              # User Pydantic schemas
│   │   └── item.py              # Item Pydantic schemas
│   │
│   ├── database.py              # Database connection & session
│   └── main.py                  # Application entry point
│
├── tests/
│   ├── test_auth.py             # Authentication tests
│   ├── test_users.py            # User endpoint tests
│   └── test_items.py            # Item endpoint tests
│
├── migrations/                  # Alembic database migrations
│   ├── versions/
│   └── env.py
│
├── Dockerfile                   # Docker image definition
├── docker-compose.yml           # Docker Compose services
├── requirements.txt             # Python dependencies
├── .env.example                 # Example environment variables
├── pytest.ini                   # Pytest configuration
└── README.md                    # This file
```

---

## Quick Start

### Prerequisites

- Python 3.9 or higher
- PostgreSQL 13 or higher
- Docker & Docker Compose (optional)

### Option 1: Local Development

#### 1. Clone the Repository

```bash
git clone https://github.com/razinahmed/rest-api-starter-kit.git
cd rest-api-starter-kit
```

#### 2. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

#### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

#### 4. Configure Environment

```bash
cp .env.example .env
# Edit .env with your configuration
```

#### 5. Run Database Migrations

```bash
alembic upgrade head
```

#### 6. Start the Development Server

```bash
uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`

---

### Option 2: Docker Compose (Recommended)

#### 1. Clone the Repository

```bash
git clone https://github.com/razinahmed/rest-api-starter-kit.git
cd rest-api-starter-kit
```

#### 2. Start Services

```bash
docker-compose up -d
```

This will:
- Build the API container
- Start PostgreSQL database
- Run database migrations automatically
- Expose the API on port 8000

#### 3. View Logs

```bash
docker-compose logs -f api
```

#### 4. Stop Services

```bash
docker-compose down
```

---

## API Documentation

Once the application is running, access the interactive API documentation:

| Platform | URL |
|----------|-----|
| **Swagger UI** | [http://localhost:8000/docs](http://localhost:8000/docs) |
| **ReDoc** | [http://localhost:8000/redoc](http://localhost:8000/redoc) |
| **OpenAPI Schema** | [http://localhost:8000/openapi.json](http://localhost:8000/openapi.json) |

---

## API Endpoints Reference

### Authentication Endpoints

| Method | Endpoint | Description | Auth |
|--------|----------|-------------|------|
| `POST` | `/api/v1/auth/register` | Register a new user | ❌ |
| `POST` | `/api/v1/auth/login` | Login and get access token | ❌ |
| `POST` | `/api/v1/auth/refresh` | Refresh access token | ✅ |
| `POST` | `/api/v1/auth/logout` | Logout (blacklist token) | ✅ |

### User Management Endpoints

| Method | Endpoint | Description | Auth | Role |
|--------|----------|-------------|------|------|
| `GET` | `/api/v1/users` | List all users | ✅ | Admin |
| `GET` | `/api/v1/users/{user_id}` | Get user by ID | ✅ | User/Admin |
| `PUT` | `/api/v1/users/{user_id}` | Update user profile | ✅ | User/Admin |
| `DELETE` | `/api/v1/users/{user_id}` | Delete user | ✅ | Admin |
| `GET` | `/api/v1/users/me` | Get current user | ✅ | User |

### Item Management Endpoints

| Method | Endpoint | Description | Auth | Role |
|--------|----------|-------------|------|------|
| `GET` | `/api/v1/items` | List all items | ✅ | User |
| `GET` | `/api/v1/items/{item_id}` | Get item by ID | ✅ | User |
| `POST` | `/api/v1/items` | Create new item | ✅ | User |
| `PUT` | `/api/v1/items/{item_id}` | Update item | ✅ | Owner/Admin |
| `DELETE` | `/api/v1/items/{item_id}` | Delete item | ✅ | Owner/Admin |

---

## Environment Variables

Configure these variables in your `.env` file:

| Variable | Type | Default | Description |
|----------|------|---------|-------------|
| `PROJECT_NAME` | String | `API` | Application name |
| `PROJECT_VERSION` | String | `1.0.0` | API version |
| `ENVIRONMENT` | String | `development` | Environment (development/staging/production) |
| `DEBUG` | Boolean | `true` | Debug mode |
| `DATABASE_URL` | String | `postgresql://...` | PostgreSQL connection string |
| `SECRET_KEY` | String | *Required* | JWT secret key (generate with `openssl rand -hex 32`) |
| `ALGORITHM` | String | `HS256` | JWT algorithm |
| `ACCESS_TOKEN_EXPIRE_MINUTES` | Integer | `30` | Access token expiration time |
| `REFRESH_TOKEN_EXPIRE_DAYS` | Integer | `7` | Refresh token expiration time |
| `ALLOWED_ORIGINS` | String | `*` | CORS allowed origins |
| `API_V1_PREFIX` | String | `/api/v1` | API version prefix |
| `LOG_LEVEL` | String | `INFO` | Logging level |

### Example .env File

```env
PROJECT_NAME=REST API Starter Kit
PROJECT_VERSION=1.0.0
ENVIRONMENT=development
DEBUG=true

DATABASE_URL=postgresql://user:password@localhost:5432/api_db
SECRET_KEY=your-super-secret-key-change-this-in-production
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
REFRESH_TOKEN_EXPIRE_DAYS=7

ALLOWED_ORIGINS=http://localhost:3000,http://localhost:8000
API_V1_PREFIX=/api/v1
LOG_LEVEL=INFO
```

---

## Database Migrations

Manage database schema changes with Alembic:

### Create a New Migration

```bash
alembic revision --autogenerate -m "Description of changes"
```

### Apply Migrations

```bash
# Apply all pending migrations
alembic upgrade head

# Apply specific number of migrations
alembic upgrade +2

# Rollback to specific revision
alembic downgrade -1
```

### View Migration History

```bash
alembic history
```

### Current Database Version

```bash
alembic current
```

---

## Testing

Run the comprehensive test suite:

### Run All Tests

```bash
pytest
```

### Run Tests with Coverage

```bash
pytest --cov=app tests/
```

### Run Specific Test File

```bash
pytest tests/test_auth.py
```

### Run Tests Matching Pattern

```bash
pytest -k "test_login"
```

### Run Tests with Verbose Output

```bash
pytest -v
```

### Generate Coverage Report

```bash
pytest --cov=app --cov-report=html tests/
# Open htmlcov/index.html in your browser
```

---

## Development Workflow

### Install Development Dependencies

```bash
pip install -r requirements-dev.txt
```

### Code Formatting

```bash
black app/ tests/
isort app/ tests/
```

### Linting

```bash
flake8 app/ tests/
pylint app/
```

### Type Checking

```bash
mypy app/
```

### Security Checks

```bash
bandit -r app/
```

---

## Production Deployment

### Build Docker Image

```bash
docker build -t rest-api-starter-kit:latest .
```

### Run in Production

```bash
docker run -d \
  --name api \
  -p 8000:8000 \
  --env-file .env.production \
  rest-api-starter-kit:latest
```

### Docker Compose Production

```bash
docker-compose -f docker-compose.prod.yml up -d
```

### Environment-Specific Configuration

Create separate `.env` files:
- `.env.development` - Local development
- `.env.staging` - Staging environment
- `.env.production` - Production environment

---

## Security Best Practices

### Implemented Security Features

- ✅ JWT token-based authentication
- ✅ Password hashing with bcrypt
- ✅ CORS protection
- ✅ SQL injection prevention (via SQLAlchemy ORM)
- ✅ Input validation (Pydantic)
- ✅ Rate limiting (ready to configure)
- ✅ HTTPS support (in Docker)
- ✅ Environment variable secrets management

### Recommended Additional Steps

1. **Use HTTPS** in production
2. **Rotate JWT secrets** regularly
3. **Enable rate limiting** on sensitive endpoints
4. **Implement API key rotation** for service-to-service communication
5. **Monitor logs** for suspicious activity
6. **Use strong passwords** for database and admin accounts
7. **Keep dependencies updated** regularly

---

## Troubleshooting

### Database Connection Errors

```bash
# Check PostgreSQL is running
docker-compose logs postgres

# Verify DATABASE_URL in .env
echo $DATABASE_URL
```

### JWT Token Errors

```bash
# Ensure SECRET_KEY is set and consistent
# Regenerate if needed: openssl rand -hex 32

# Check token expiration time settings in .env
```

### Port Already in Use

```bash
# Kill existing process
lsof -i :8000
kill -9 <PID>

# Or change port in docker-compose.yml
```

### Permission Errors

```bash
# Fix file permissions
chmod +x docker-entrypoint.sh
```

---

## Contributing

Contributions are welcome! Please follow these steps:

1. **Fork** the repository
2. **Create** a feature branch: `git checkout -b feature/amazing-feature`
3. **Commit** your changes: `git commit -m 'Add amazing feature'`
4. **Push** to the branch: `git push origin feature/amazing-feature`
5. **Open** a Pull Request

### Code Standards

- Follow PEP 8 style guide
- Add tests for new features
- Update documentation
- Run tests before submitting PR

---

## License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

MIT License grants permission to:
- ✅ Use commercially
- ✅ Modify the source code
- ✅ Distribute the software
- ✅ Use privately

With the conditions:
- ℹ️ License and copyright notice must be included

---

## Support

Need help? Check out these resources:

- **FastAPI Docs:** https://fastapi.tiangolo.com/
- **SQLAlchemy Docs:** https://docs.sqlalchemy.org/
- **JWT Docs:** https://tools.ietf.org/html/rfc7519
- **Pydantic Docs:** https://docs.pydantic.dev/

---

<div align="center">

### Made with love by [Abdul Rasak V](https://github.com/razinahmed)

If you find this project helpful, please consider giving it a star!

**Happy coding!**

</div>

# REST API Starter Kit

A production-ready REST API boilerplate with FastAPI, JWT auth, SQLAlchemy ORM, Docker support & auto-generated docs.

## Features

- JWT Authentication with refresh tokens
- SQLAlchemy ORM with async support
- Auto-generated Swagger & ReDoc documentation
- Role-based access control (RBAC)
- Database migrations with Alembic
- Docker & Docker Compose setup
- Environment-based configuration
- Input validation with Pydantic
- Comprehensive error handling
- Unit & integration test suite

## Tech Stack

- **Framework:** FastAPI (Python)
- **ORM:** SQLAlchemy + Alembic
- **Auth:** JWT (PyJWT)
- **Database:** PostgreSQL
- **Validation:** Pydantic v2
- **Testing:** Pytest
- **Containerization:** Docker

## Getting Started

```bash
git clone https://github.com/razinahmed/rest-api-starter-kit.git
cd rest-api-starter-kit
docker-compose up -d
```

Or without Docker:

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## API Docs

Once running, visit:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Project Structure

```
rest-api-starter-kit/
├── app/
│   ├── api/
│   ├── core/
│   ├── models/
│   ├── schemas/
│   └── main.py
├── tests/
├── docker-compose.yml
├── Dockerfile
└── requirements.txt
```

## License

MIT License

---

Made with passion by [Abdul Rasak V](https://github.com/razinahmed)


# **`FastAPI` REST API template**

![python](https://img.shields.io/badge/-Python-yellow?style=for-the-badge&logo=python&logoColor=white)
![JWT](https://img.shields.io/badge/JWT-black?style=for-the-badge&logo=JSON%20web%20tokens)
![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)
![Swagger](https://img.shields.io/badge/-Swagger-%23Clojure?style=for-the-badge&logo=swagger&logoColor=white)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)

## Rest API boilerplate written on Python3.13 + FastAPI + SQLAlchemy + Alembic

### Endpoints

- `POST:/api/v1/users` - registrates new user
- `POST:/api/v1/auth` - authorizes user, generates JWT token.
- `GET:/api/v1/users/:id` - get user profile by ID *(requires token in Bearer header)*
- `GET:/api/v1/users/me` - returns current user profile *(requires token in Bearer header)*

- Visit <http://localhost:8000/docs> to see `Swagger` specification

---

### Launch guide

- To launch webapp run:

```Shell
docker build .
docker run {image}
```

- To run by [poetry](https://python-poetry.org/):

```Shell
poetry install
poetry exec python3 -m src
```

---

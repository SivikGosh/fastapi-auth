<img src='https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white'><img src='https://img.shields.io/badge/3.12-23283d?style=flat-square'>
<img src='https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white'>
<img src='https://img.shields.io/badge/JWT-000000?style=flat-square&logo=jsonwebtokens&logoColor=white'>
<img src='https://img.shields.io/badge/SQLAlchemy-D71F00?style=flat-square&logo=sqlalchemy&logoColor=white'>
<img src='https://img.shields.io/badge/PostgreSQL-4169E1?style=flat-square&logo=postgresql&logoColor=white'>
<img src='https://img.shields.io/badge/Gunicorn-499848?style=flat-square&logo=gunicorn&logoColor=white'>
<img src='https://img.shields.io/badge/NGINX-009639?style=flat-square&logo=nginx&logoColor=white'>
<img src='https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white'>

# FastAPI Auth Service
FastAPI auth service. Demo available **[here](http://inviters.eventfun.ru)**. Also: [Swagger](http://inviters.eventfun.ru/docs), [ReDoc](http://inviters.eventfun.ru/redoc).

Superuser credentials:
- username: **admin**
- password: **admin**
- email: **admin@admin.admin**

<br>

## ! Warning
- **username** in user credentials for login is an user email, actually, not username.
- When you login, received HTTP status "No content". It's normal, because token saving in cookies.

<br>

## Local build

Clone the repo and enter into the root folder
```bash
git clone git@github.com:SivikGosh/fastapi-auth.git
cd fastapi-auth/
```

Copy environments
```bash
cp .env.example .env
```

Change **DB_HOST** value from *localhost* to *db*

Start building
```bash
docker compose up -d
```

Service will be available on http://localhost.

<br>

## 🛠 Develop Mode

### Install and use
Clone the repo and enter into the root folder
```bash
git clone git@github.com:SivikGosh/fastapi-auth.git
cd fastapi-auth/
```

Create an environment
```bash
python3.12 -m venv venv
source venv/bin/activate
```

Install dependencies
```bash
pip3 install .[dev]
```

Start
```bash
uvicorn src.main:app --reload
```

Build DB container (optional)
```bash
cp .env.example .env
docker compose -f docker-compose.db.yaml up -d
```

### URLs

| url                  | description          |
| -------------------- | -----------          |
| localhost:8000       | Check DB connection. |
| localhost:8000/docs  | Swagger UI.          |
| localhost:8000/redoc | ReDoc.               |
<!-- |                      |                      | -->

### Commands
| command            | description                          |
| ------------------ | ------------------------------------ |
| pre-commit install | Install pre-commit hooks file.       |
| pipdeptree         | Show dependency tree.                |
<!-- |                    |                                      | -->

<br>

<div align="right">

## Author's contact
<a href='https://t.me/sivikgosh' target='_blank'><img src='https://img.shields.io/badge/SivikGosh-white?style=flat-square&logo=Telegram&logoColor=26A5E4'></a>

</div>

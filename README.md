# FastAPI Auth Service
FastAPI auth service. Python 3.12.

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

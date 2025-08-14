FROM python:3.12-slim

WORKDIR /app

COPY src/ ./src/
COPY alembic/ ./alembic/
COPY alembic.ini .
COPY pyproject.toml .
COPY .env .

# RUN ls -a && sleep 600

RUN pip install .

COPY entrypoint.sh /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh

ENTRYPOINT ["/app/entrypoint.sh"]

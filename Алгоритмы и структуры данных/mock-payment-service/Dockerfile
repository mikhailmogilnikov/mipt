FROM python:3.10

WORKDIR /app
COPY pyproject.toml poetry.lock ./
RUN pip install poetry
RUN poetry install --no-root

COPY . .
CMD ["poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

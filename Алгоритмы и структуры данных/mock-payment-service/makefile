POETRY = poetry
PYTHON = $(POETRY) run python
UVICORN = $(POETRY) run uvicorn
PYTEST = $(POETRY) run pytest
DOCKER_COMPOSE = docker-compose

install:
	$(POETRY) install

run:
	$(UVICORN) app.main:app --reload --host 0.0.0.0 --port 8000

lint:
	$(POETRY) run flake8 .

test:
	$(PYTEST)

migrate:
	$(POETRY) run alembic upgrade head

up:
	$(DOCKER_COMPOSE) up -d

down:
	$(DOCKER_COMPOSE) down

logs:
	$(DOCKER_COMPOSE) logs -f

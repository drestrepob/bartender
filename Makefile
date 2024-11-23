include .env

# Alias
awslocal=aws --endpoint-url http://localhost:4566
clean-flags=--volumes --rmi all --remove-orphans
dc=docker compose
django-project-path=bartender/infrastructure/frameworks/django

build:
	$(dc) up --build --watch

start:
	$(dc) up --watch

down:
	$(dc) down

bash:
	$(dc) exec -it backend bash

clean:
	$(dc) down $(clean-flags)

db-shell:
	$(dc) exec -it db psql -U postgres -d $(DB_NAME)

make-migrations:
	$(dc) exec backend manage makemigrations

make-migrations-app:
	$(dc) exec backend manage makemigrations $(app)

migrate:
	$(dc) exec backend manage migrate

migrate-app:
	$(dc) exec backend manage migrate $(app)

show-migrations:
	$(dc) exec backend manage showmigrations

test:
	uv run pytest -x --ds=bartender.infrastructure.settings.test

test-parallel:
	uv run pytest -n auto --ds=bartender.infrastructure.settings.test

test-directory:
	uv run pytest $(directory) -x --ds=bartender.infrastructure.settings.test

coverage:
	uv run pytest -x --ds=bartender.infrastructure.settings.test --no-cov-on-fail --cov=. --no-header

coverage-html:
	uv run pytest -x --ds=bartender.infrastructure.settings.test --no-cov-on-fail --cov=. --cov-report=html --no-header

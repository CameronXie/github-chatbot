pluginsDir=${PWD}/plugins

# Docker
up: create-dev-env create-dev-bot-config
	@docker compose up --build -d

down:
	@docker compose down -v

create-dev-env:
	@test -e .env || cp .env.example .env

create-dev-bot-config:
	@test -e config.py || cp config.py.template config.py

# CI

ci-test:
	@docker compose exec python sh -c 'make bot-test'

# bot
bot-test:
	@make bot-type
	@make bot-unit

bot-unit:
	@pytest

bot-type:
	@mypy ${pluginsDir}
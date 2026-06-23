.PHONY: help
help:
	@echo ""
	@echo "Usage: make [target]"
	@echo ""
	@echo "PUCKCURL! Project Makefile"
	@echo ""
	@echo "Targets:"
	@echo "  help                Show this help message"
	@echo "  run                 Bring up the local dev stack"
	@echo "  stop                Stop the local dev stack"
	@echo "  makemigrations      Generate django migrations"
	@echo "  migrate             Apply django migrations"
	@echo "  createsuperuser     Create a django superuser"
	@echo "  manage              Run an arbitrary manage.py command, e.g. make manage ARGS=\"createsuperuser\""
	@echo "  lint-be             Lint and type-check the backend (ruff + ty)"
	@echo "  format-be           Format the backend (ruff)"
	@echo "  lint-fe             Lint the frontend (eslint)"
	@echo "  format-fe           Format the frontend (prettier)"
	@echo "  secrets-hide        Encrypt secret files with git-secret"
	@echo "  secrets-reveal      Reveal secret files with git-secret"
	@echo "  deploy-staging      Rsync the repo to staging, then rebuild and restart the stack"
	@echo ""

# --- Dev -------------------------------------------------------------------

DOCKERRUN := docker compose run --rm backend
DOCKERRUNFE := docker compose run --rm --no-deps frontend
MANAGEPY := $(DOCKERRUN) uv run python manage.py

.PHONY: secrets-hide
secrets-hide:
	git-secret hide -v -m

.PHONY: secrets-reveal
secrets-reveal:
	git-secret reveal -f

.PHONY: run
run:
	docker compose up --build

.PHONY: stop
stop:
	docker compose down

.PHONY: makemigrations
makemigrations:
	$(MANAGEPY) makemigrations

.PHONY: migrate
migrate:
	$(MANAGEPY) migrate

.PHONY: createsuperuser
createsuperuser:
	$(MANAGEPY) createsuperuser

.PHONY: manage
manage:
	$(MANAGEPY) $(ARGS)

.PHONY: lint-be
lint-be:
	$(DOCKERRUN) sh -c "uv run ruff check . && uv run ruff format --check . && uv run ty check"

.PHONY: format-be
format-be:
	$(DOCKERRUN) uv run ruff format .

.PHONY: lint-fe
lint-fe:
	$(DOCKERRUNFE) npm run lint

.PHONY: format-fe
format-fe:
	$(DOCKERRUNFE) npm run format

# --- Staging ---------------------------------------------------------------

STAGING_HOST := ares
STAGING_DIR  := /opt/puckcurl_staging
STAGING_COMPOSE := docker compose -f docker-compose.staging.yml --env-file .env.staging

.PHONY: deploy-staging
deploy-staging:
	rsync -avz --delete \
		--exclude .venv \
		--exclude .ropeproject \
		--exclude .ruff_cache \
		--exclude .claude \
		--exclude docs \
		--exclude private_media \
		--exclude node_modules \
		--exclude __pycache__ \
		--exclude .git \
		--exclude .gitsecret \
		--exclude .env \
		. "$(STAGING_HOST):$(STAGING_DIR)/"
	ssh $(STAGING_HOST) "cd $(STAGING_DIR) && \
		$(STAGING_COMPOSE) build && \
		$(STAGING_COMPOSE) up -d && \
		$(STAGING_COMPOSE) restart scheduler"

.PHONY: install
install:
	poetry install

.PHONY: run
run:
	poetry run python manage.py runserver

.PHONY: migrate
migrate:
	peotry run python manage.py migrate

.PHONY: makemigration
makemigration:
	peotry run python manage.py makemigration

.PHONY: createsuperuser
createsuperuser:
	peotry run python manage.py createsuperuser


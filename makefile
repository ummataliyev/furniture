build:
	docker compose build

up:
	docker compose up

up-d:
	docker compose up -d

down:
	docker compose down

db:
	docker compose exec db sh

restart:
	docker compose restart

makemigrations:
	docker compose exec web python manage.py makemigrations

migrate:
	docker compose exec web python manage.py migrate

logs:
	docker compose logs -f web

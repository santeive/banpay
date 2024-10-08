build:
	docker compose build
	
up:
	docker compose up

down: 
	docker compose down

migrate:
	docker compose exec web python manage.py migrate

makemigrations:
	docker compose exec web python manage.py makemigrations

createsuperuser:
	docker compose exec web python manage.py createsuperuser

show_urls:
	docker compose exec web python manage.py show_urls

tests:
	docker compose exec web python manage.py test
init:
	bun install
	make tailwind
	poetry config virtualenvs.in-project true
	poetry install
	poetry shell

run:
	# example: make run command="createsuperuser"
	poetry run python app/manage.py $(command)

dev:
	poetry run python app/manage.py runserver

prod:
	make tailwind
	make collectstatic
	cd app && DEBUG=False poetry run granian --interface asgi app.asgi:application 

tailwind:
	 bunx tailwindcss -i ./app/home/static/home/css/base.css -o ./app/home/static/home/css/style.min.css --minify

tailwind-watch:
	 bunx tailwindcss -i ./app/home/static/home/css/base.css -o ./app/home/static/home/css/style.min.css --watch

migrate:
	poetry run python app/manage.py migrate

collectstatic:
	poetry run python app/manage.py collectstatic --noinput

test-unit:
	cd app && poetry run python manage.py test

test-docs:
	cd app && poetry run interrogate -vvv

check:
	poetry run ruff check app

format:
	poetry run ruff format app
	poetry run djhtml app

update:
	poetry update
	bun update

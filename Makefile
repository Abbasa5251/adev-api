up:
	docker-compose up -d

down:
	docker-compose down 

migrate:
	python manage.py migrate

makemigrations:
	python manage.py makemigrations

flake8:
	flake8 .

black-check:
	black --check .

black-diff:
	black --diff .

black:
	black .

isort-check:
	isort . --check-only --skip venv --skip .venv --skip migrations

isort-diff:
	isort . --diff --skip venv --skip .venv --skip migrations

isort:
	isort . --skip venv --skip .venv --skip migrations	

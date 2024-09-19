migrations:
	python manage.py makemigrations
migrate:
	python manage.py makemigrations && python manage.py migrate_schemas
run:
	python manage.py runserver
pull:
	git checkout main && git pull origin main
install:
	pip install -r requirements.txt
test:
	export DJANGO_SETTINGS_MODULE=mysite.settings && pytest -vv

migrations:
	python manage.py makemigrations
migrate:
	python manage.py makemigrations && python manage.py migrate_schemas
run:
	python manage.py runserver

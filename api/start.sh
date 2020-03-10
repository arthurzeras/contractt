#!/bin/sh

echo "Collect static files"
python manage.py collectstatic --noinput

echo "Apply database migrations"
python manage.py makemigrations
python manage.py migrate

echo "Starting server"
gunicorn --bind 0.0.0.0:8000 --workers 1 --log-level INFO contractt.wsgi:application

#!/bin/sh

python manage.py migrate --no-input
python manage.py collectstatic --no-input

gunicorn ecommerce.wsgi:application -b 0:8000 -w 4

#!/bin/sh

# Database set up
    python manage.py makemigrations
    python manage.py migrate


# Snippets
    # python manage.py flush --no-input

# Run server
    # python manage.py collectstatic --no-input 
    # gunicorn --workers=2 --bind=0.0.0.0:8000 events.wsgi:application
    python manage.py runserver 0.0.0.0:8000

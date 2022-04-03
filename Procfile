release: python manage.py migrate
web: gunicorn config.wsgi:application -b 0.0.0.0:80

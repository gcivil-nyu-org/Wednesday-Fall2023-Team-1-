web: gunicorn --bind :8000 --workers 3 --threads 2 vibecheck.wsgi:application
websocket: daphne -b :: -p 5000 vibecheck.asgi:application
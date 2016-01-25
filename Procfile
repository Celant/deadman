web: gunicorn deadman.wsgi --log-file -
worker: celery worker --app=deadman.celery:app

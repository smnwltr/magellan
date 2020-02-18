release: python magellan/manage.py migrate
web: gunicorn --pythonpath magellan magellan.wsgi --log-file -

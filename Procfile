release: python magellan/manage.py migrate
release: python magellan/manage.py compilescss
release: python magellan/manage.py collectstatic --noinput
web: gunicorn --pythonpath magellan magellan.wsgi --log-file -

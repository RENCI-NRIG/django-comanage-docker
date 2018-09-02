#!/usr/bin/env bash

python manage.py makemigrations
python manage.py showmigrations
python manage.py migrate
python manage.py collectstatic --noinput

if [[ "${USE_DOT_VENV}" -eq 1 ]]; then
    uwsgi --uid ${UWSGI_UID:-1000} --gid ${UWSGI_GID:-1000}  --virtualenv ./.venv --ini core_uwsgi.ini
else
    uwsgi --uid ${UWSGI_UID:-1000} --gid ${UWSGI_GID:-1000}  --virtualenv ./venv --ini core_uwsgi.ini
fi

#!/bin/bash

# This is a simple development script to start the Invenio application.

LOGFILE="run.log"

# Check if the application is already running
if pgrep -f "uwsgi" > /dev/null; then
    echo "Already running:"
    pgrep -fl "uwsgi"

    echo
    read -p "Do you want to restart? [y/N] "

    if [[ $REPLY =~ ^[Yy]$ ]]; then
        source .venv/bin/activate
        pip install uwsgi
        pkill uwsgi
        echo -en "Restarting"
        while pgrep -f "uwsgi" > /dev/null; do
            echo -n "."
            sleep 1;
        done
        echo
    else
        echo "Leaving it running."
        exit 0
    fi
fi

# Start the application
if [ -d ".venv" ]; then
    source .venv/bin/activate
    pip install uwsgi
    truncate -s 0 $LOGFILE
    export FLASK_DEBUG=1
    uwsgi docker/uwsgi.ini --daemonize run.log
    echo "Started Invenio using uWSGI."
    tail -f run.log
else
    # initial setup
    export PYTHON=/usr/bin/python3.12
    ./nrp upgrade
    source .venv/bin/activate
    pip install uwsgi nrp-invenio-client
    ./nrp develop
fi

: '
# reset database

source .venv/bin/activate

invenio db destroy --yes-i-know || true
invenio db init create
invenio index destroy --force --yes-i-know || true
invenio index init
invenio oarepo cf init
invenio files location create --default default s3://default

invenio oarepo fixtures load
invenio users create -a -c test@test.com
'

: '
# start from scratch

rm -rf .nrp .pdm-build .venv
find . -name "__pycache__" -type d -exec rm -rf {} +
'


: '
# rebuild UI

source .venv/bin/activate

invenio webpack clean create
invenio webpack install --legacy-peer-deps
invenio webpack build --production
'

#!/bin/bash

# This is a simple development script to start the Invenio application.

LOGFILE="run.log"

# Check if the application is already running
if pgrep -f "uwsgi docker/uwsgi.ini" > /dev/null; then
    echo "Already running:"
    pgrep -fl "uwsgi docker/uwsgi.ini"

    echo
    read -p "Do you want to restart? [y/N] "

    if [[ $REPLY =~ ^[Yy]$ ]]; then
        source .venv/bin/activate
        uwsgi --stop docker/.uwsgi.pid
        echo -en "Restarting"
        while pgrep -f "uwsgi docker/uwsgi.ini" > /dev/null; do
            echo -n "."
            sleep 1;
        done
    else
        echo "Leaving it running."
        exit 0
    fi
fi

# Start the application
if [ -d ".venv" ]; then
    source .venv/bin/activate
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
source .venv/bin/activate

invenio db destroy --yes-i-know || true                                                                                                                                                                                                       
invenio db init create
invenio index destroy --force --yes-i-know || true
invenio index init
invenio oarepo cf init
invenio files location create --default default s3://default

invenio users create -a -c test@test.com
invenio oarepo fixtures load
'

: '
rm -rf .nrp .pdm-build .venv
find . -name "__pycache__" -type d -exec rm -rf {} +
'

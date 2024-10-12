#!/bin/bash

# This is a simple development script to start the Invenio application.

LOGFILE="run.log"

# Check if the application is already running
if pgrep -f "invenio run" > /dev/null; then
    echo "Already running:"
    pgrep -fl "invenio run"

    echo
    read -p "Do you want to restart? [y/N] "

    if [[ $REPLY =~ ^[Yy]$ ]]; then
        pkill -f "invenio run"
        echo -e "Restarting...\n"
    else
        echo "Leaving it running."
        exit 0
    fi
fi

# Start the application
if [ -d ".venv" ]; then
    truncate -s 0 $LOGFILE
    source .venv/bin/activate
    export FLASK_DEBUG=1
    nohup invenio run -h 127.0.0.1 -p 5000 >>$LOGFILE 2>&1 &
    echo "Invenio application started as background job with PID $!"
    disown
else
    # initial setup
    export PYTHON=/usr/bin/python3.12
    ./nrp upgrade
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

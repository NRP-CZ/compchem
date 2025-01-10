#!/bin/bash

source .venv/bin/activate

cd ui/experiments/semantic-ui || exit 1
rm -f node_modules || true

trap 'ln -s ../../../.venv/var/instance/assets/node_modules node_modules' EXIT

(
    invenio webpack clean create &&
    invenio webpack install --legacy-peer-deps &&
    invenio webpack build --production
) || true

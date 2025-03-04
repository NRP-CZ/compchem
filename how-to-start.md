# Pre-install

- Node 21
- Python 3.12
- Docker


# Prepare the environment

- run `./nrp upgrade` (should fail on *webpack install*)
- edit `.nrp/devtools/lib/python3.12/site-packages/nrp_devtools/commands/ui/assets.py`
  - in the `install_npm_packages` function, add `--legacy-peer-deps` to the `webpack install` command
- run `./nrp develop`
- kill the develop process after it finishes
- run:
  ```
  source .venv/bin/activate

  invenio oarepo fixtures load
  invenio users create -a -c test@test.com
  ```
- provide a password for the user


# Run app

- run `./run.sh`
- app should be available at `https://localhost:8443/` (ignore the certificate warning)


# Other useful commands

## Rebuild UI when necessary

```
source .venv/bin/activate

invenio webpack clean create
invenio webpack install --legacy-peer-deps
invenio webpack build --production
```

## Reset database

```
source .venv/bin/activate

invenio db destroy --yes-i-know || true
invenio db init create
invenio index destroy --force --yes-i-know || true
invenio index init
invenio oarepo cf init
invenio files location create --default default s3://default

invenio oarepo fixtures load
invenio users create -a -c test@test.com
```

## clean the environment

```
rm -rf .nrp .pdm-build .venv
find . -name "__pycache__" -type d -exec rm -rf {} +
docker compose -f docker/docker-compose.yml down
```

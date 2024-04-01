# Repository of Computational Chemistry Experiments

## Starting up in development mode

Run `./nrp develop` to start the development server. If the server does not start with
message such as "opensearch could not be contacted", wait for a couple of minutes and 
then run `./nrp develop` again. The reason is that the initial setup of opensearch
can take a long time, depending on the speed of your connection and CPU power.

Later on, you might call `./nrp develop --skip-checks` for a faster start up time.

## Removing all the data and starting from scratch

To remove all the data and start from scratch, run:

```bash
source .venv/bin/activate

invenio db destroy --yes-i-know || true
invenio db init create
invenio index destroy --force --yes-i-know || true
invenio index init
invenio oarepo cf init
invenio files location create --default default s3://default
```

## Changing the model

After changing the model inside `models` folder, run:

```bash
./nrp model compile experiments
```

Then follow the "starting from scratch" section above to clean the repository
and start using your updated model.

## Using nrp client

### Creating a test user

At first create a test user (orcid integration later):

```bash
invenio users create -a -c test@test.com
```

### Install the client

You can install the both inside the repository venv (local development) or in your own venv:

```bash
source .venv/bin/activate

pip install nrp-invenio-client
```

Then configure it (while the repository is running):

```bash
nrp-cmd add alias --default --no-verify https://127.0.0.1:5000 compchem
```

To check that the alias was added correctly, run:

```bash
nrp-cmd describe repository
nrp-cmd describe models
```

### Create a sample record

```bash
nrp-cmd create record experiments '{"metadata": {"name": "blah"}}'
```

From file (you can use yaml or json file):

```bash
nrp-cmd create record experiments ./sample_data/starter.yaml
```


### Upload tpr file

### Check the status of the record to see, if the metadata have been filled
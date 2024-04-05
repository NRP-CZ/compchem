# Repository of Computational Chemistry Experiments

## Starting up in development mode

Run `./nrp develop` to start the development server. If the server does not start with
message such as "opensearch could not be contacted", wait for a couple of minutes and 
then run `./nrp develop` again. The reason is that the initial setup of opensearch
can take a long time, depending on the speed of your connection and CPU power.

Later on, you might call `./nrp develop --skip-checks` for a faster start up time.

## Initial setup

### Creating a test user

After the server has been started at least once, create a test user (orcid integration later):

```bash
source .venv/bin/activate

invenio users create -a -c test@test.com
```

### Importing vocabularies

```bash
source .venv/bin/activate

invenio oarepo fixtures load --verbose
```

### Importing sample data

```bash
source .venv/bin/activate

invenio oarepo fixtures load --no-system-fixtures sample_data --identity test@test.com --verbose
```

## Using nrp client

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
nrp-cmd create record experiments '{"metadata": {"name": "blah"}}' @rec
```

From file (you can use yaml or json file):

```bash
nrp-cmd create record experiments ./sample_data/starter.yaml @rec
```

The `@rec` is a name of a variable where the id record will be saved.
This can be used later for getting the record, updating it, uploading
files etc.

### Upload tpr file

Run the following command to upload a file to the record:

```bash
nrp-cmd upload file @rec ~/Downloads/7.tpr '{"caption": "blah"}'
```

The first parameter is the record to which the file should be uploaded.
The second parameter is the path to the file on your local machine and 
an optional last one are file metadata.


### Check the status of the record to see, if the metadata have been filled

```bash
nrp-cmd get record @rec

nrp-cmd list files @rec
```


## Troubleshooting & model development


### Removing all the data and starting from scratch

To remove all the data and start from scratch, run:

```bash
source .venv/bin/activate

invenio db destroy --yes-i-know || true
invenio db init create
invenio index destroy --force --yes-i-know || true
invenio index init
invenio oarepo cf init
invenio files location create --default default s3://default
invenio users create -a -c test@test.com
invenio oarepo fixtures load --verbose
```

### Changing the model

After changing the model inside `models` folder, run:

```bash
./nrp model compile experiments
```

Then follow the "starting from scratch" section above to clean the repository
and start using your updated model.


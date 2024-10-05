# Invenio API

- set up the api endpoint
```bash
#export INVENIO_API_URL="https://inveniordm.web.cern.ch/api"
export INVENIO_API_URL="https://127.0.0.1:5000/api"
```

## Login

- endpoint: `/login`
- method: `POST`
- data:
  - `email`: email
  - `password`: password

```bash
curl -X POST $INVENIO_API_URL/login -c cookies.txt -k  \
    --data "email=test@test.com&password=123456"

session_cookie=$(grep 'session' cookies.txt | awk '{print $7}')
echo "Session cookie: $session_cookie"
```


## Search

- endpoint: `/records`
- method: `GET`
- params:
  - `q`: query string
  - `size`: number of results to return per page (default: 25)
  - `page`: page number (default: 1)
  - `prettyprint`: format the json response (default: 0)

```bash
curl -X GET "$INVENIO_API_URL/records?q=test&size=5" -k
```


## Create record

- endpoint: `/records`
- method: `POST`
- headers:
  - `Referer`: the referer url
  - `X-CSRFToken`: the csrf token
- cookies:
  - `csrftoken`: the csrf token
  - `session`: the session cookie
- data:
  - `access`: access control settings
  - `metadata`: metadata of the record

**⚠️User must be [logged in](#login) to create a record**

```bash
curl -X POST "$INVENIO_API_URL/records" \
    -H "Content-Type: application/json" \
    -H "Referer: $INVENIO_API_URL" \
    -H "X-CSRFToken: $csrf_token" \
    -b "csrftoken=$csrf_token; session=$session_cookie" \
    -d '{
        "access": {
            "record": "public",
            "files": "public"
        },
        "metadata": {
            "title": "Super Cool Title",
            "publication_date": "2024-08-16",
            "publisher": "MUNI",
            "resource_type": {
                "id": "dataset"
            },
            "creators": [
                {
                    "person_or_org": {
                        "family_name": "Doe",
                        "given_name": "John",
                        "type": "personal"
                    }
                }
            ]
        }
    }'
```


## View record

- endpoint: `/records/<record_id>`
- method: `GET`

```bash
curl -X GET "$INVENIO_API_URL/records/my3h4-b7n49"
```

## List files of a record

- endpoint: `/records/<record_id>/files`
- method: `GET`

```bash
curl -X GET "$INVENIO_API_URL/records/my3h4-b7n49/files"
```

## Upload file to record

- uploading a file has multiple steps

### Step 1: Create a new file in the record

- endpoint: `/records/<record_id>/files`
- method: `POST`
- headers:
  - `Referer`: the referer url
  - `X-CSRFToken`: the csrf token
- cookies:
  - `csrftoken`: the csrf token
  - `session`: the session cookie
- data:
  - `[{"key": "file_name"}]`

```bash
curl -X POST "$INVENIO_API_URL/records/my3h4-b7n49/files" \
    -H "Referer: $INVENIO_API_URL" \
    -H "X-CSRFToken: $csrf_token" \
    -b "csrftoken=$csrf_token; session=$session_cookie" \
    -d '[{"key": "20240802_151338.jpg"}]'
```

### Step 2: Upload the file to the record

- endpoint: `/records/<record_id>/files/<file_name>/content`
- method: `PUT`
- headers:
  - `Referer`: the referer url
  - `X-CSRFToken`: the csrf token
- cookies:
  - `csrftoken`: the csrf token
  - `session`: the session cookie
- data:
  - the file content

```bash
curl -X PUT "$INVENIO_API_URL/records/my3h4-b7n49/files/20240802_151338.jpg/content" \
    -H "Referer: $INVENIO_API_URL" \
    -H "X-CSRFToken: $csrf_token" \
    -b "csrftoken=$csrf_token; session=$session_cookie" \
    --data-binary @image.jpg
```

### Step 3: Commit the file to the record

- endpoint: `/records/<record_id>/draft/files/<file_name>/commit`
- method: `POST`
- headers:
  - `Referer`: the referer url
  - `X-CSRFToken`: the csrf token
- cookies:
  - `csrftoken`: the csrf token
  - `session`: the session cookie

```bash
curl -X POST "$INVENIO_API_URL/records/my3h4-b7n49/draft/files/20240802_151338.jpg/commit" \
    -H "Referer: $INVENIO_API_URL" \
    -H "X-CSRFToken: $csrf_token" \
    -b "csrftoken=$csrf_token; session=$session_cookie"
```


## Download file from record

- endpoint: `/records/<record_id>/files/<file_name>/content`
- method: `GET`

```bash
curl -X GET "$INVENIO_API_URL/records/my3h4-b7n49/files/20240802_151338.jpg/content" -o image.png
```


## Publish record

- endpoint: `/records/<record_id>/draft/actions/publish`
- method: `POST`
- headers:
  - `Referer`: the referer url
  - `X-CSRFToken`: the csrf token
- cookies:
  - `csrftoken`: the csrf token
  - `session`: the session cookie

```bash
curl -X POST "$INVENIO_API_URL/records/my3h4-b7n49/draft/actions/publish" \
    -H "Referer: $INVENIO_API_URL" \
    -H "X-CSRFToken: $csrf_token" \
    -b "csrftoken=$csrf_token; session=$session_cookie"
```

# PyTorch REST API

## Getting started

- export environment variables 

```
export FLASK_APP=torch_api
export FLASK_ENV=development
```

- install requirements and requirements

```
pip install -e .
flask run
```

## Using Docker :whale:

Build the container.

`docker build -t pytorch-flask-api .`

Run container on localhost.

`docker run -d -p 5000:5000 pytorch-flask-api:latest`

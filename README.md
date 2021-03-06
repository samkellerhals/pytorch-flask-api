# PyTorch REST API
Flask REST API with a PyTorch backend that consumes image URLs in a POST request, and classifies the image using the pretrained DenseNet network from the PyTorch model library.

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

Alternatively simply download the image from Dockerhub and run locally.

```
docker pull sakell/flask-api-torch:first-release

docker run -d -p 5000:5000 sakell/flask-api-torch:first-release
```  

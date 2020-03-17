FROM ubuntu:18.04

RUN apt-get update
RUN apt-get install -y python3 python3-pip

COPY . /pytorch-flask-api

WORKDIR /pytorch-flask-api

ENV FLASK_APP=torch_api

ENV FLASK_ENV=development

ENV LC_ALL=C.UTF-8

ENV LANG=C.UTF-8

RUN pip3 install -e .

EXPOSE 5000

CMD flask run --host=0.0.0.0
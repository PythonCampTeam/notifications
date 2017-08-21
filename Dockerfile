FROM python:3.5.3

ADD . /notifications

WORKDIR /notifications

RUN chmod +x /notifications/run.sh

RUN apt-get update && apt-get install -y \
  netcat

RUN /bin/bash -c "pip3 install -r /notifications/requirements/base.txt"

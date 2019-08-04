FROM python:3

RUN pip install -U pip
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . /var/app/
WORKDIR /var/app/
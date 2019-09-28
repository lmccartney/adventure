FROM python:3.7

RUN pip install pipenv==2018.11.26
COPY Pipfile.lock .
RUN pipenv sync --dev

COPY . /var/app
WORKDIR /var/app

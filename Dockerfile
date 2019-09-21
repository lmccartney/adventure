FROM python:3.7

RUN pip install pipenv
COPY Pipfile.lock .
RUN pipenv sync --dev

COPY . /var/app
WORKDIR /var/app

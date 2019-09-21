FROM python

RUN pip install pipenv
COPY . /app
WORKDIR /app
RUN pipenv sync --dev

FROM python:3.10-bullseye as develop

WORKDIR /tmp/dev

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

FROM python:3.10-slim as final

WORKDIR /var/bot

COPY plugins plugins
COPY config.py config.py
COPY requirements.txt prod-requirements.txt

RUN mkdir -p data \
    && pip install --no-cache-dir -r requirements.txt \
    && rm requirements.txt

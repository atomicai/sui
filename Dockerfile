FROM python:3.10.2

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install dotmap mmh3

COPY ./sui sui
COPY ./hypercorn.toml .

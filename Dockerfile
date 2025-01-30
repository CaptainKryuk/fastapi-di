FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app
COPY . .

RUN apt-get update && apt-get -y install gcc

RUN pip3 install poetry
RUN poetry self add poetry-plugin-export
RUN poetry export --without-hashes --format=requirements.txt > requirements.txt
RUN pip3 install -r requirements.txt

EXPOSE 8000
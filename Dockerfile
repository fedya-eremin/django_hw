FROM python:3.12

WORKDIR /app

COPY pyproject.toml pyproject.toml

RUN pip install -e .

COPY . .

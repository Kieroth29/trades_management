# syntax=docker/dockerfile:1
FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /trades_management
COPY requirements.txt /trades_management/
RUN pip install -r requirements.txt
COPY . /trades_management/
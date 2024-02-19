FROM python:3.12.2-slim-bullseye
ENV PIP_DIABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


WORKDIR /code/

# Allows docker to cache installed dependencies between builds
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt


# Adds our application code to the image
WORKDIR /code/app
COPY . /code/app


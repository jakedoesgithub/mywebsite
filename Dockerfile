FROM python:3.8
ENV PIP_DIABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


WORKDIR /code/

# Allows docker to cache installed dependencies between builds
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Install gettext in order to use Django's Translation system for internationalization support
RUN apt-get update

# Adds our application code to the image
WORKDIR /code/app
COPY . /code/app

EXPOSE 8000
#test
FROM python:3.9-slim-buster
WORKDIR /backend
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1
# install system dependencies
RUN apt-get update \
    && apt-get -y install netcat gcc build-essential default-libmysqlclient-dev\
    && apt-get clean
# install python dependencies
RUN pip install --upgrade pip
RUN pip install poetry==1.1.12 setuptools
COPY ./poetry.lock ./pyproject.toml /backend/
# RUN poetry export -f requirements.txt --without-hashes | pip install -r /dev/stdin
RUN poetry install
COPY . /backend
CMD ["poetry", "run", "python", "app.py"]
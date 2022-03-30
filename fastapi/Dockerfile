FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9
USER root

RUN apt-get update && apt-get -y upgrade
RUN apt install -y default-mysql-client

# Install pip library.
RUN mkdir -p /root/src
COPY ./requirements.txt /root/src
WORKDIR /root/src

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy pre start shell file.
COPY ./prestart.sh /root/src

# Copy database migration files.
COPY ./db /db

# Copy app files.
COPY ./app /app
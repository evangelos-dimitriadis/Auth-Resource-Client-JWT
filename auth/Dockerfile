FROM python:3.11-bullseye

RUN apt-get -y update && apt-get -y upgrade

RUN useradd -m auth
WORKDIR /home/auth

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt


CMD ["/usr/local/bin/uwsgi", "--ini", "uwsgi.ini" , "--honour-std"]

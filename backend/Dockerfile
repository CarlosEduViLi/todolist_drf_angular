FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

#Compiler and OS libraries
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
       build-essential python3-dev gcc nano \
       libmariadb3 libmariadb-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /usr/src/app

RUN pip3 install --upgrade pip

ADD . /usr/src/app

RUN pip3 install -r requirements.txt

EXPOSE 8082

# Comando CMD para executar os comandos Django ao iniciar o contêiner
CMD ["bash", "-c", "\
    python manage.py collectstatic --noinput && \
    python manage.py makemigrations && \
    python manage.py migrate && \
    python manage.py runserver 0.0.0.0:8082 \
"]
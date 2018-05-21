FROM python:3
RUN apt-get update && apt-get install -y python-dev libldap2-dev libsasl2-dev libssl-dev
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code
RUN pip install -r requirements.txt
ADD . /code/
CMD gunicorn "app:create_app()"

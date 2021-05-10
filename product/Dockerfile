FROM quay.io/jdiazvera/flask-gunicorn

COPY requirements.txt /
RUN pip3 install -r /requirements.txt

COPY . /app
WORKDIR /app

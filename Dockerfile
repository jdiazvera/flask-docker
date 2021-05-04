FROM python:alpine

COPY requirements.txt /
RUN pip3 install -r /requirements.txt

COPY . /app
WORKDIR /app

RUN chmod +x entrypoint.sh
ENTRYPOINT ["./gunicorn.sh"]

FROM python:3.7.3-stretch

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/

RUN pip3 install --no-cache-dir -r requirements.txt

COPY . /usr/src/app

EXPOSE 5200

ENTRYPOINT ["python3"]

CMD ["-m", "swagger_server"]
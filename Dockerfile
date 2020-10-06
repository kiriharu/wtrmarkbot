FROM python:3.8-alpine3.12
RUN apk add build-base libffi-dev zlib-dev g++ freetype-dev jpeg-dev gcc musl-dev openssl-dev && rm -rf /var/cache/apk/*
WORKDIR /src/
COPY . /src/
RUN pip3 install -r requirements.txt

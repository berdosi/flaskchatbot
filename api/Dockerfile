FROM alpine

WORKDIR /

RUN apk add python3
RUN apk add py3-pip

RUN pip3 install flask

COPY . /api

EXPOSE 5001

CMD [ "python3", "/api/app.py" ]

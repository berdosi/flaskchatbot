FROM alpine

WORKDIR /

RUN apk add python3
RUN apk add py3-pip

RUN pip3 install flask

COPY interface /interface

EXPOSE 5000

CMD [ "python3", "/interface/app.py" ]
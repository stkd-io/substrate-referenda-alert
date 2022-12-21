FROM ubuntu:22.04

ENV TZ=
ENV SLACK_API=
ENV SLACK_CHANNEL_NAME=
ENV ACCOUNT=
ENV WSS_URL=
ENV PYTHONUNBUFFERED=true

ARG DEBIAN_FRONTEND=noninteractive

LABEL Maintainer="@frazzled_dazzle"
LABEL Company="stkd.io"


#Setup env
RUN apt update;\
    apt install -y python;\
    apt install -y  pip;\
    apt install -y tzdata;\
    apt autoremove

RUN pip install substrate-interface;\
    pip install pycryptodome;\
    pip install os;\
    pip install slack_sdk

RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN mkdir /data;

COPY ./app/main.py /data/ref_alert.py

CMD [ "python3", "/data/ref_alert.py"]


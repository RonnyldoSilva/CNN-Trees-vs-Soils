FROM python:3.8-slim

RUN apt-get update && apt-get install -y libglib2.0-0
RUN apt-get install libgl1-mesa-glx -y

WORKDIR /workspace
COPY ./requirements.txt /workspace/requirements.txt
RUN pip3 install -r requirements.txt
COPY . /workspace
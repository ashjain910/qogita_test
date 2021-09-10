# syntax=docker/dockerfile:1
FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/

## Set environment variables
ENV LANG=C.UTF-8 LC_ALL=C.UTF-8

RUN apt-get update --fix-missing
RUN apt-get install -y wget \
	bzip2 \
	ca-certificates \
	build-essential \
	curl \
	git-core \
	pkg-config \
	python3-dev \
	python3-pip \
	python3-setuptools \
	python3-virtualenv \
	unzip \
	software-properties-common \
	llvm

RUN apt install -y gdal-bin python-gdal python3-gdal
RUN pip3 install --upgrade pip
RUN pip install -r requirements.txt
RUN ls

COPY . /code/

#RUN chmod +x /code/entrypoint.sh

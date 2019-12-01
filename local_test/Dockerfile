FROM ubuntu:18.04

MAINTAINER Pranav N "npranav10@gmail.com"

RUN mkdir flasky
RUN cd flasky 
RUN apt-get update 
RUN apt-get install -y python-pip
RUN apt-get clean && rm -rf /var/lib/apt/lists/*
RUN pip install --upgrade pip
RUN apt-get update 
RUN apt-get install -y software-properties-common
RUN apt-get update 
RUN add-apt-repository "deb http://archive.ubuntu.com/ubuntu $(lsb_release -sc) universe"
RUN apt-get update 
RUN apt-get install -y tesseract-ocr
RUN pip install flask pytesseract js2py
COPY app.py /app.py
CMD ["python","app.py"]
EXPOSE 5000





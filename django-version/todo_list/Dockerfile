FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD docker_setup.txt /code/
RUN pip install -r docker_setup.txt
ADD . /code/

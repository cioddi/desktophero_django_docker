FROM python:3
ENV PYTHONUNBUFFERED 1
RUN apt-get update \
  && apt-get install -y build-essential python-dev librsync-dev  
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
RUN PATH=$HOME/.local/bin:$PATH
#ADD . /code/

FROM python:3.11-slim-buster

RUN mkdir /project-api
WORKDIR /project-api

RUN apt-get update && apt-get install -y \
    cmake \
    build-essential \
    libopencv-dev

COPY requirements.txt /project-api
RUN pip install --no-cache-dir -r requirements.txt

COPY . /project-api


EXPOSE 5000

CMD ["python", "api.py"]
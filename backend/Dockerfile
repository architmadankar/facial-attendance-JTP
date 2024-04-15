FROM python:3.11-slim-buster

WORKDIR /app

ADD . /app

RUN apt-get update && apt-get install -y \
    cmake \
    build-essential \
    libopencv-dev
    
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["python", "api.py"]
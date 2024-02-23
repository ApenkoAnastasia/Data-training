FROM python:3.10

COPY ./ /app

WORKDIR /app

RUN apt-get update && \
    apt-get upgrade -y && \
    pip3 install --no-cache-dir -r requirements.txt && \
    apt-get clean

CMD ["bash"]

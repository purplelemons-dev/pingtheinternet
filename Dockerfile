FROM python:3.12.4-bookworm

RUN apt update -y && apt upgrade -y
RUN apt install iputils-ping -y

WORKDIR /app

COPY src .

CMD [ "python", "./app.py"]

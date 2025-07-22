FROM python:3.13-slim

WORKDIR /parking-spot

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt update
RUN apt install -y gconf-service libasound2 libatk1.0-0 libcairo2 libcups2 libfontconfig1 libgdk-pixbuf2.0-0 libgtk-3-0 libnspr4 libpango-1.0-0 libxss1 fonts-liberation libappindicator1 libnss3 lsb-release xdg-utils

COPY . .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN playwright install

EXPOSE 8000
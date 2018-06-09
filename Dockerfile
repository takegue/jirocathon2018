FROM library/python:3.6-slim

ADD /src /app
WORKDIR /app

RUN pip install -r requirements.txt
RUN python app.py

EXPOSE 80

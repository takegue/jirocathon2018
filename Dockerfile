FROM library/python:3.6-slim

ADD /src /app
WORKDIR /app

RUN pip install -r requirements.txt

EXPOSE 80
ENTRYPOINT ["python", "/app/app.py"]

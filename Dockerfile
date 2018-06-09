FROM library/python:3.6-slim

ADD ./src/requirements.txt /app/
WORKDIR /app

RUN pip install -r requirements.txt

ADD ./src /app
ENV FLASK_DEBUG=1

EXPOSE 80
ENTRYPOINT ["flask", "run", "--host=0.0.0.0", "--port=80"]

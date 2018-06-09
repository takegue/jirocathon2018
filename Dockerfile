FROM library/python:3.6-slim

ADD /src /app
WORKDIR /app

RUN pip install -r requirements.txt
ENV FLASK_DEBUG=1

EXPOSE 80
ENTRYPOINT ["flask", "run"]

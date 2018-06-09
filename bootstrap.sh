#!/bin/bash

docker-compose build
docker-compose up -d

url=$(docker-compose port ngrok 4040)
curl -sq $url/status | grep -o '\w\+.ap.ngrok.io' | uniq


#!/bin/bash

docker-compose build
docker-compose up -d

url=$(docker-compose port ngrok 4040)
public=''
while [[ $public -eq '' ]];do
  public=$(curl -sq $url/status | grep -o '\w\+.ap.ngrok.io' | uniq)
done


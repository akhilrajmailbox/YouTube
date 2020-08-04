#!/bin/bash
# docker run -it -v /path/to/YouTube:/opt/ --name youtuber --hostname youtuber python:3.7.8 /bin/bash
# run this commands inside this docker container
# create OAuth Client ID "API yt-secret.json" from https://console.cloud.google.com/apis/credentials
# https://github.com/youtube/api-samples/

# python3 needed
apt install python-pip
pip install google-auth-oauthlib
pip install --upgrade google-api-python-client



# sudo apt-get install screen

# screen -S name
# python vid-cmnt.py
# Press keys Ctrl-A followed by Ctrl-D
# screen -ls
# screen -r name


## kill screen
# screen -ls
# screen -X -S [session # you want to kill] kill

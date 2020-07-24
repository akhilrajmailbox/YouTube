#!/bin/bash
# docker run -it -v /path/to/YouTube:/opt/ --name youtuber --hostname youtuber python:3.7.8 /bin/bash
# run this commands inside this docker container
# create OAuth Client ID "API yt-secret.json" from https://console.cloud.google.com/apis/credentials
# https://github.com/youtube/api-samples/

pip install google-auth-oauthlib
pip install --upgrade google-api-python-client

python3 vid-cmnt.py
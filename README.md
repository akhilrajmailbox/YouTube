# YouTube Data API

## OAuth Client ID

create OAuth Client ID "API yt-secret.json" from [console.cloud.google.com](https://console.cloud.google.com/apis/credentials)


## Install the following Dependencies

**Note :** `python` should be `python3` (alias name)

```bash
apt install python-pip
pip install google-auth-oauthlib
pip install --upgrade google-api-python-client
```


## Live Rename With Views and Channel Name of Last Commenter

**Note :** Update the following in the script before running

* `ytvid_id` : your video ID
* `mychannelid` : your channel ID
* `client_secrets_file` : your OAuth Client ID json file name


```bash
python vid-cmnt.py
```



## Comment Reply on Others Channel Videos

**Note :** Update the following in the script before running

* `maxrespond` : maximum respond comment (by defaut it is 20)

**Note :** Run the Script with following parameters

* `ytvid_id` : your video ID
* `mychannelid` : your channel ID
* `google_user` : Google user (between 0 and 9), the secret file name will be `[0-9]-yt-secret.json` under folder `secrets`
* `-f` : option is for confirm whether it is featured channel or not

```bash
python cmnt-reply.py -c <mychannelid> -v <ytvid_id> -u <google_user> -f <yes or no>
```


## Auto Pilot for comments on Others Channel Video's Comments as Reply

**Note :** Update the following in the script before running

* `maxresult` : maximum result of comment (by defaut it is 50)
* `maxrespond` : maximum respond comment (by defaut it is 20)
* `waittime` : time to wait before going to next video for comment (by defaut it is 4 hr)

**Note :** Run the Script with following parameters

* `ytvid_id` : your video ID
* `mychannelid` : your channel ID
* `google_user` : Google user (between 0 and 9), the secret file name will be `[0-9]-yt-secret.json` under folder `secrets`
* `-f` : option is for confirm whether it is featured channel or not

```bash
python auto-pilot.py -c <mychannelid> -v <ytvid_id> -u <google_user> -f <yes or no>
```




## Install Screen For run in BG

If you want to install and run the script in bg, then follow this steps


```bash
apt-get install screen -y
```

Run the script inside screen with name `screen_name`

```bash
screen -S screen_name
python vid-cmnt.py
```

Press keys Ctrl-A followed by Ctrl-D

```bash
screen -ls
screen -r screen_name
```


### Kill Screen

```bash
screen -ls
screen -X -S screen_name kill
```





[reference](https://github.com/youtube/api-samples/)
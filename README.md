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

**Note :** Run the Script with following parameters

* `ytvid_id` : your video ID
* `google_user` : Google user (between 0 and 9), the secret file name will be `[0-9]-yt-secret.json` under folder `secrets`


```bash
python vid-cmnt.py -v <ytvid_id> -u <google_user>
```



## Comment Reply on Others Channel Videos

**Note :** Update the following in the script before running

* `maxrespond` : maximum respond comment (by defaut it is 20)

**Note :** Run the Script with following parameters

* `ytvid_id` : your video ID
* `google_user` : Google user (between 0 and 9), the secret file name will be `[0-9]-yt-secret.json` under folder `secrets`

```bash
python cmnt-reply.py -v <ytvid_id> -u <google_user>
```



## Auto Pilot for comments on Others Channel Video's Comments as Reply

**Note :** Update the following in the script before running

* `targetsub_maxcount` : maximum subscribers count can be for the channel going to comment (by defaut it is 10000)
* `targetsub_mincount` : minimum subscribers count can be for the channel going to comment (by defaut it is 50)
* `cmnt_maxresult` : maximum result of comment (by defaut it is 20)
* `cmnt_maxrespond` : maximum respond comment (by defaut it is 6)
* `maxsmiles` : maximum number of smiles (by defaut it is 3)
* `waittime` : time to wait before going to next video for comment (by defaut it is 40 min)

**Note :** Run the Script with following parameters

* `ytvid_id` : your video ID
* `google_user` : Google user (between 0 and 9), the secret file name will be `[0-9]-yt-secret.json` under folder `secrets`

```bash
python auto-reply.py -v <ytvid_id> -u <google_user>
```



## Auto Pilot for subscribe on Others Channel and comment

**Note :** Update the following in the script before running

* `targetsub_maxcount` : maximum subscribers count can be for the channel going to comment (by defaut it is 10000)
* `mysub_maxcount` : maximum subscribed channels by my channel (by defaut it is 500)
* `mysub_delcount` : minimum subscribed channels by my channel (by defaut it is 50)
* `cmnt_maxresult` : maximum result of comment (by defaut it is 50)
* `cmnt_minresult` : maximum respond comment (by defaut it is 30)
* `maxsmiles` : maximum number of smiles (by defaut it is 3)
* `waittime` : time to wait before going to next video for comment (by defaut it is 3 hr)

**Note :** Run the Script with following parameters

* `ytvid_id` : your video ID
* `google_user` : Google user (between 0 and 9), the secret file name will be `[0-9]-yt-secret.json` under folder `secrets`

```bash
python auto-sub.py -v <ytvid_id> -u <google_user>
```




## Auto Pilot for subscribe on Others Channel and reply to comments

**Note :** Update the following in the script before running

* `targetsub_maxcount` : maximum subscribers count can be for the channel going to comment (by defaut it is 10000)
* `targetsub_mincount` : minimum subscribers count can be for the channel going to comment (by defaut it is 50)
* `mysub_maxcount` : maximum subscribed channels by my channel (by defaut it is 500)
* `mysub_delcount` : minimum subscribed channels by my channel (by defaut it is 50)
* `cmnt_maxresult` : maximum result of comment (by defaut it is 20)
* `cmnt_maxrespond` : maximum respond comment (by defaut it is 5)
* `maxsmiles` : maximum number of smiles (by defaut it is 3)
* `waittime` : time to wait before going to next video for comment (by defaut it is 30 mins)

**Note :** Run the Script with following parameters

* `ytvid_id` : your video ID
* `google_user` : Google user (between 0 and 9), the secret file name will be `[0-9]-yt-secret.json` under folder `secrets`

```bash
python auto-pilot.py -v <ytvid_id> -u <google_user>
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
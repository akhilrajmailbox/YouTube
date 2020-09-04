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


## Live Rename With Views and Channel Name of Last Commenter (auto)

**Note :** Run the Script with following parameters

* `ytvid_id` : your video ID
* `google_user` : Google user (between 0 and 9), the secret file name will be `[0-9]-yt-secret.json` under folder `secrets`


```bash
python vid-cmnt.py -v <ytvid_id> -u <google_user>
```



## Comment Reply on Others Channel Videos (manual)

**Note :** Update the following in the script before running

* `maxrespond` : maximum respond comment (by defaut it is 20)

**Note :** Run the Script with following parameters

* `ytvid_id` : your video ID
* `google_user` : Google user (between 0 and 9), the secret file name will be `[0-9]-yt-secret.json` under folder `secrets`

```bash
python cmnt-reply.py -v <ytvid_id> -u <google_user>
```



## Auto Pilot for comments on Others Channel Video's Comments as Reply (auto)

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
python auto-cmnt-reply.py -v <ytvid_id> -u <google_user>
```



## Auto Pilot for subscribe on Others Channel and comment (auto)

**Note :** Update the following in the script before running

* `targetsub_maxcount` : maximum subscribers count can be for the channel going to comment (by defaut it is 10000)
* `mysub_maxcount` : maximum subscribed channels by my channel (by defaut it is 500)
* `mysub_delcount` : minimum subscribed channels by my channel (by defaut it is 50)
* `cmnt_maxresult` : maximum result of comment (by defaut it is 50)
* `cmnt_minresult` : maximum respond comment (by defaut it is 30)
* `maxsmiles` : maximum number of smiles (by defaut it is 3)
* `waittime` : time to wait before going to next video for comment (by defaut it is 120 mins)

**Note :** Run the Script with following parameters

* `ytvid_id` : your video ID
* `google_user` : Google user (between 0 and 9), the secret file name will be `[0-9]-yt-secret.json` under folder `secrets`

```bash
python auto-sub.py -v <ytvid_id> -u <google_user>
```




## Auto Pilot for subscribe on Others Channel with pre defined messages and reply to comments (auto)

**Note :** Update the following in the script before running

* `targetsub_maxcount` : maximum subscribers count can be for the channel going to comment (by defaut it is 10000)
* `targetsub_mincount` : minimum subscribers count can be for the channel going to comment (by defaut it is 50)
* `mysub_maxcount` : maximum subscribed channels by my channel (by defaut it is 500)
* `mysub_delcount` : minimum subscribed channels by my channel (by defaut it is 20)
* `cmnt_maxresult` : maximum result of comment (by defaut it is 20)
* `cmnt_maxrespond` : maximum respond comment (by defaut it is 5)
* `maxsmiles` : maximum number of smiles (by defaut it is 3)
* `waittime` : time to wait before going to next video for comment (by defaut it is 120 mins)

**Note :** Run the Script with following parameters

* `ytvid_id` : your video ID
* `google_user` : Google user (between 0 and 9), the secret file name will be `[0-9]-yt-secret.json` under folder `secrets`

```bash
python auto-sub-precmnt-reply.py -v <ytvid_id> -u <google_user>
```




## Auto Pilot for subscribe on Others Channel with Ramdom / Predefined messages and reply to comments (auto)

**Note :** Update the following in the script before running

* `targetsub_maxcount` : maximum subscribers count can be for the channel going to comment (by defaut it is 10000)
* `targetsub_mincount` : minimum subscribers count can be for the channel going to comment (by defaut it is 50)
* `mysub_maxcount` : maximum subscribed channels by my channel (by defaut it is 500)
* `mysub_delcount` : minimum subscribed channels by my channel (by defaut it is 20)
* `cmnt_maxresult` : maximum result of comment (by defaut it is 20)
* `cmnt_maxrespond` : maximum respond comment (by defaut it is 10)
* `loopsub_maxcount` : number of subscription in a single loop before waittime (by defaut it is 10)
* `waittime` : time to wait before going to next video for comment (by defaut it is 240 mins)
* `reply_to_comment` : Enable this for reply to comment, If enabled, reply to comments when `loopsub_count = 0` (by default it is `True`)
* `subcmnt_random` : Enable this for use Random comments otherwise it will choose predefined comments (by default it is `True`)


**Note :** Run the Script with following parameters

* `ytvid_id` : your video ID
* `google_users` : Google user (between 0 and 9), the secret file name will be `[0-9]-yt-secret.json` under folder `secrets`

```bash
python auto-sub-allcmnt-reply.py -v <ytvid_id> -u <google_user>
```




## Delete the Subscribers from your channel (auto)

**Note :** Run the Script with following parameters

* `mysub_maxcount` : Maximum Subscribers Counts need to persist on your channel
* `mysub_delcount` : Maximum Subscribers need to Remove from your Channel which you Subscribed
* `google_user` : Google user (between 0 and 9), the secret file name will be `[0-9]-yt-secret.json` under folder `secrets`
* `waittime` : time to wait before going to next video for comment (by defaut it is 720 mins)


```bash
python auto-sub-del.py -s <max sub number persist> -d <max sub number to delete> -u <google user>
```





## Get the Video Url for New comments and Subscribe (manual)

**Note :** Update the following in the script before running

* `targetsub_maxcount` : maximum subscribers count can be for the channel going to comment (by defaut it is 10000)
* `targetsub_mincount` : minimum subscribers count can be for the channel going to comment (by defaut it is 50)
* `mysub_maxcount` : maximum subscribed channels by my channel (by defaut it is 500)
* `mysub_delcount` : minimum subscribed channels by my channel (by defaut it is 50)
* `cmnt_maxresult` : maximum result of comment (by defaut it is 20)
* `subcmnt_random` : Enable this for use Random comments otherwise it will choose predefined comments (by default it is `True`)


**Note :** Run the Script with following parameters

* `ytvid_id` : your video ID
* `google_user` : Google user (between 0 and 9), the secret file name will be `[0-9]-yt-secret.json` under folder `secrets`
* `number of result` : Number of Result you need from this Script in a Single run


```bash
python get-url.py -v <ytvid_id> -u <google user> -c <number of result>
```





## Repling to the video's comments on your channel (manual)


**Note :** Update the following in the script before running

* `waittime` : time to wait before going to next video for comment (by defaut it is 10 sec)
* `cmnt_maxrespond` : maximum respond comment (by defaut it is 99)


**Note :** Run the Script with following parameters

* `vid_id` : Video ID for check the comments and replying (if you want to check all comments give : `myallvideos`)
* `google_user` : Google user (between 0 and 9), the secret file name will be `[0-9]-yt-secret.json` under folder `secrets`


```bash
python myvid-reply.py -v <vid_id> -u <google user>
```





## Delete the Subscribers from your channel (manual)

**Note :** Run the Script with following parameters

* `mysub_maxcount` : Maximum Subscribers Counts need to persist on your channel
* `mysub_delcount` : Maximum Subscribers need to Remove from your Channel which you Subscribed
* `google_user` : Google user (between 0 and 9), the secret file name will be `[0-9]-yt-secret.json` under folder `secrets`


```bash
python sub-del.py -s <max sub number persist> -d <max sub number to delete> -u <google user>
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



### Scrolling Screen to Top

Press keys Ctrl-A followed by esc

scroll up and down or use up / down arrow



[reference](https://github.com/youtube/api-samples/)
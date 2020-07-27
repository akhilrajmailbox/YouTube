import os
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
import pprint
import time
import array as arr
from random import randint
import sys, getopt


my_wishes = [
    "Hello ",
    "Hey ",
    "My Friend ",
    "Dude ",
    "Hi ",
    "Heyy ",
    "Hooi ",
    "Hey dude ",
    "Hellowww ",
    "Hiiii "
]


my_eng_support_replies = [
    "Be My Friend, and Grow Together... I am Also new here",
    "I will share nice videos, Support Everyone, add me as a friend I will also add you",
    "Friends ?, Support Together and can succeeedddd",
    "Add me as a new friend, I will also add you...",
    "Come to my channel and support me, i will also support you",
    "If you love awesome videos, please check my channel and help me  to grow",
    "Check my channel and support me here, i will also do the same to your channel",
    "Support me and I am happy to support you also",
    "Check my videos and support me plzzzz if you like it, i will also check your channel.",
    "Be my Friend and support each other...",
    "Let be friends and grow here together",
    "plz support me to grow in yt, plzzz",
    "Check my new videos and plz support if you like",
    "Support plz, then you can also expect support from meeeee",
    "I am trying to grow in y0utube, but its hard, plz support"
]


my_coc_support_replies = [
    "COC Gamer ?, plz check my channel and support me plz",
    "clash of clans gaming channel started... please support",
    "plz check my channe for new coc gaming videos",
    "I have started one gaming channel, plz support me",
    "Support my new channe, it's a gaming channel",
    "Clash  of clans, nice game right ?, plz support me to grow with my channel",
    "expecting  your support for my channel, plz",
    "recently I started one youtube channel for coc, plz take a look",
    "check my recent coc video uploaded, if you like it then plz support me..",
    "support me gusy to live in youtube",
    "Clash of Clans is an awesome game, Plz check my channel and support me",
    "for ncie COC gaming  videos and news, please support me  and check my channel",
    "Please have a look into my new video and channel, help me to grow",
    "new gaming channel, check it and support me if my channel seems good to you",
    "Clash of Clans channel started by me, I haven't uploaded more videos, but will do, please support me"
]


my_mallu_support_replies = [
    "കൂട്ടുകാരാ, സപ്പോർട്ട് ചെയ്യാമോ ?",
    "എന്റെ ചാനൽ ഒന്ന് നോക്കാമോ ?, ഒന്ന് ഹെല്പ് ചെയ്‌തു, സപ്പോർട്ട് please",
    "എന്നെ സപ്പോർട്ട് ചെയ്യാമോ ?, എന്റെ ചാനൽ ഒന്ന് നോക്കണേ",
    "ചാനൽ grow ചെയ്യാൻ help cheyaneeee, plz",
    "ഞാൻ പുതിയ ചാനൽ start ചെയ്തു, സപ്പോർട്ട് ചെയ്യണേ",
    "എന്റെ ചാനൽ ഒന്ന് നോക്കണേ",
    "പുതിയ ചാനൽ ആണ്, സപ്പോർട്ട് ചെയ്യണേ",
    "എന്റെ പുതിയ യൂട്യൂബ് ചാനൽ ആണ് ഇത്‌, ഒന്ന് സപ്പോർട്ട് ചെയ്യണേ",
    "ന്യൂ ചാനൽ, ഒരു സബ്സ്ക്രൈബ് പ്രതീഷിക്കുന്നു",
    "ഒന്ന് സബ്സ്ക്രൈബ് ചെയ്തു ഹെല്പ് ചെയ്യാമോ",
    "എന്റെ ചാനലിൽ കേറി ഒന്ന് നോക്കണേ, ഒന്ന് സബ്സ്ക്രൈബ് ചെയ്യാമോ ?",
    "മൈ ന്യൂ യൂട്യൂബ് ചാനൽ, സബ്സ്ക്രൈബ് ചെയ്യാമോ ?",
    "ചാനൽ സ്റ്റാർട്ട് ചെയ്‌തൂട്ടോ, ഒന്ന് ഹെല്പ് ചെയ്യണേ, സബ്സ്ക്രൈബ്",
    "പുതിയ ചാനൽ ആണ്, ഒരുപാട് വീഡിയോസ് ഒന്നും ഇല്ലാ, സപ്പോർട്ട് ചെയ്യാമോ ?",
    "എന്റെ ഈ ചാനലിൽ ഒന്ന് കേറി നോക്കണേ"
]




scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]



def main(argv):
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    # os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    mychannelid = "" # no need to change anything here
    ytvid_id = "" # no need to change anything here
    reply_opts = "" # no need to change anything here
    google_user = "" # no need to change anything here
    params_validation="\n\npython cmnt-reply.py -c <mychannelid> -v <ytvid_id> -u <google user> -r <reply options> \nreply options : eng or mal or or coc or com or coe or mix\ngoogle user : choose between 0 and 9\n"
    api_service_name = "youtube"
    api_version = "v3"

    try:
        opts, args = getopt.getopt(argv,"hc:v:u:r:")
    except getopt.GetoptError:
        print(params_validation)
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print(params_validation)
            sys.exit()
        elif opt in ("-c"):
            mychannelid = arg
        elif opt in ("-v"):
            ytvid_id = arg
        elif opt in ("-u"):
            google_user = arg
        elif opt in ("-r"):
            reply_opts = arg


    if mychannelid and len(mychannelid) >= 3:
        print("Your Channel ID is ", mychannelid)
    else:
        print(params_validation)
        sys.exit(2)

    if ytvid_id and len(ytvid_id) >= 3:
        print ("Video ID is ", ytvid_id)
    else:
        print(params_validation)
        sys.exit(2)

    if google_user and len(google_user) >= 1:
        print ("Google User is ", google_user)
    else:
        print(params_validation)
        sys.exit(2)

    if reply_opts and len(reply_opts) == 3:
        print ("Reply Option is ", reply_opts)
    else:
        print(params_validation)
        sys.exit(2)



    if google_user == "0":
        client_secrets_file = "secrets/0-yt-secret.json"
    elif google_user == "1":
        client_secrets_file = "secrets/1-yt-secret.json"
    elif google_user == "2":
        client_secrets_file = "secrets/2-yt-secret.json"
    elif google_user == "3":
        client_secrets_file = "secrets/3-yt-secret.json"
    elif google_user == "4":
        client_secrets_file = "secrets/4-yt-secret.json"
    elif google_user == "5":
        client_secrets_file = "secrets/5-yt-secret.json"
    elif google_user == "6":
        client_secrets_file = "secrets/6-yt-secret.json"
    elif google_user == "7":
        client_secrets_file = "secrets/7-yt-secret.json"
    elif google_user == "8":
        client_secrets_file = "secrets/8-yt-secret.json"
    elif google_user == "9":
        client_secrets_file = "secrets/9-yt-secret.json"
    else:
        print("google_user need to pass...!")
        sys.exit(2)


    # Get credentials and create an API client
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, scopes)
    credentials = flow.run_console()
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials)



    ## Check the non-spam comments
    cmnt_request = youtube.commentThreads().list(
        part="snippet,replies",
        maxResults=100,
        order="time",
        videoId=ytvid_id
    )
    cmnt_response = cmnt_request.execute()


    comment_count = 0
    for item in cmnt_response["items"]:
        repliesrandom = randint(0,14)
        wishsrandom = randint(0,9)

        if reply_opts == "eng":
            my_replies = my_eng_support_replies
        elif reply_opts == "mal":
            my_replies = my_mallu_support_replies
        elif reply_opts == "coc":
            my_replies = my_coc_support_replies
        elif reply_opts == "mix":
            repliesrandom = randint(0,44)
            my_replies = my_eng_support_replies + my_mallu_support_replies + my_coc_support_replies
        elif reply_opts == "col":
            repliesrandom = randint(0,29)
            my_replies = my_mallu_support_replies + my_coc_support_replies
        elif reply_opts == "coe":
            repliesrandom = randint(0,29)
            my_replies = my_eng_support_replies + my_coc_support_replies
        else:
            print("reply_opts need to pass...!")
            sys.exit(2)

        cmnt_commentid = item["id"];
        cmnt_commentown = item["snippet"]["topLevelComment"]["snippet"]["authorDisplayName"]


        ## vaidate reply
        reply_check = "null"
        if "replies" in item:
            replies_data = item["replies"];
            for reply in replies_data["comments"]:
                reply_check = "null"
                reply_own = reply["snippet"]["authorChannelId"]["value"]
                print(reply_own)
                contain = (mychannelid in reply_own)
                if(contain):
                    print(mychannelid + " already response to the comment")
                    reply_check = "found"
                    break;
                else:
                    print(mychannelid + " going to respond to the latest comment")
        else:
            print("No one Replied to This Comment yet...!")


        ## reply to the comment
        if reply_check == 'null':
            comment_count = comment_count + 1
            print("Replying to Comment : " + str(comment_count))
            cmnt_reply = youtube.comments().insert(
                part="snippet",
                body=dict(
                snippet=dict(
                    parentId=cmnt_commentid,
                    textOriginal= my_wishes[wishsrandom] + cmnt_commentown + ",  " + my_replies[repliesrandom]
                )
                )
            )
            cmnt_response = cmnt_reply.execute()
            print("Successfully Send the reply to " + cmnt_commentown)

        print("Sleeping for 3 sec")
        time.sleep(3)


    print("Total Reply : " + str(comment_count))
    print("Worked...!");



if __name__ == "__main__":
    main(sys.argv[1:])
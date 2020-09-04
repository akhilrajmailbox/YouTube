import os
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
import pprint
import time
import array as arr
from random import randint
import sys, getopt
from datetime import datetime, timedelta, timezone


##################################################################
params_validation="\n\n python myvid-reply.py -v <vid_id> -u <google user>\n google user : choose between 0 and 9\n vid_id : choose : myallvideos , if you want to look for all comments\n"

waittime = 10
cmnt_maxrespond = 99
api_service_name = "youtube"
api_version = "v3"
scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]


##################################################################


vid_replies = [
    "Thank you",
    "Thanks",
    "thank U",
    "Thanks for the visit",
    "thank you too",
    "I appreciate it",
    "thanks for visiting",
    "stay connected",
    "Thank you 👍",
    "👍👍",
    "👍",
    "Thanks for coming",
    "Thanks and welcome",
    "Yes for sure",
    "So nice of you",
    "Welcome",
    "Yes, thank you",
    "Thank you! Cheers!",
    "Cheers 👍",
    "Thanks 😊",
    "So nice",
    "Good",
    "Thanks for liking",
    "Thank you so much",
    "🤞",
    "💕",
    "Many many thanks",
    "Ok thank you",
    "Wow, thank you",
    "👍🔔",
    "😊😊",
    "im happy",
    "tthanks",
    "tthank y0u",
    "thank_U",
    "wecome here",
    "be happy😊",
    "great you are here",
    "kind of you😊😊",
    "so nicee"
]


########### function main
def main(argv):

    vid_id = "" # no need to change anything here
    google_user = "" # no need to change anything here

    try:
        opts, args = getopt.getopt(argv,"hv:u:")
    except getopt.GetoptError:
        print(params_validation)
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print(params_validation)
            sys.exit()
        elif opt in ("-v"):
            vid_id = arg
        elif opt in ("-u"):
            google_user = arg

    if vid_id and len(vid_id) >= 1:
        print ("Video ID is ", vid_id)
    else:
        print(params_validation)
        sys.exit(2)

    if google_user and len(google_user) >= 1:
        print ("Google User is ", google_user)
    else:
        print(params_validation)
        sys.exit(2)

    client_secrets_file = "secrets/" + google_user + "-yt-secret.json"

    # Get credentials and create an API client
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, scopes)
    credentials = flow.run_console()
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials)

    comment_count = 0
    print("Going to run the loop with waittime = " + str(waittime) + " sec)")
    

    ## Get My channel ID
    mychannel_request = youtube.channels().list(
        part="statistics",
        mine=True
    )
    mychannel_response = mychannel_request.execute()
    mychannelid = mychannel_response["items"][0]["id"]


    ## Get Video channel ID
    if not vid_id == "myallvideos":
        chkchannel_request = youtube.videos().list(
            part="snippet",
            id=vid_id
        )
        chk_response = chkchannel_request.execute()
        chkchannelid = chk_response["items"][0]["snippet"]["channelId"]

        if not mychannelid == chkchannelid:
            print("You are not the owner for this video : " + vid_id)
            sys.exit(2)



######################################################
    vid_cmnt = []
    list_cmnt = ""
    arr_cmnt = ""
    next_pagetoken = ""

    while 1:
        ## Check the non-spam comments
        if vid_id == "myallvideos":
            cmnt_request = youtube.commentThreads().list(
                part="snippet,replies",
                maxResults=100,
                order="time",
                allThreadsRelatedToChannelId=mychannelid,
                pageToken=next_pagetoken
            )
        else:
            cmnt_request = youtube.commentThreads().list(
                part="snippet,replies",
                maxResults=100,
                order="time",
                videoId=vid_id,
                pageToken=next_pagetoken
            )

        cmnt_response = cmnt_request.execute()

        vid_cmnt += cmnt_response["items"]
        next_pagetoken = cmnt_response.get("nextPageToken")

        if "nextPageToken" not in cmnt_response or len(vid_cmnt) >= cmnt_maxrespond:
            break

    print("Number comments : " + str(len(vid_cmnt)))

    ## Counting the unreplied comments
    unreplied_cmnt = 0
    for mycmnt in vid_cmnt:
        if "replies" not in mycmnt:
            unreplied_cmnt = unreplied_cmnt + 1
    print("Total unreplied Comments greater than : " + str(unreplied_cmnt))


    ## commenting to unreplied comments
    for mycmnt in vid_cmnt[:cmnt_maxrespond]:

        if "replies" in mycmnt:
            replies_data = mycmnt["replies"]
            for reply in replies_data["comments"]:
                reply_own = reply["snippet"]["authorChannelId"]["value"]
                # print(reply_own)
                if reply_own == mychannelid:
                    print("You already responded to the comment")
                    break

        else:
            print("No one Replied to This Comment yet...!")

            mycmnt_id = mycmnt["id"]
            comment_count = comment_count + 1
            print("Replying to Comment : " + str(comment_count))

            random_replies = randint(0,39)
            my_replies = vid_replies[random_replies]

            reply = youtube.comments().insert(
                part="snippet",
                body=dict(
                snippet=dict(
                    parentId=mycmnt_id,
                    textOriginal=my_replies
                )
                )
            )
            reply_response = reply.execute()
            print("Successfully Send the reply to comment ID " + mycmnt_id + " with my_replies : " + my_replies)
            print("Sleeping for " + str(waittime) + " sec")
            time.sleep(waittime)

    print("Total Reply : " + str(comment_count))




if __name__ == "__main__":
    main(sys.argv[1:])
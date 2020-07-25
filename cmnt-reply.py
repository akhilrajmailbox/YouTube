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
    "Hi "
    ]


my_replies = [
    "Be My Friend, and Grow Together... I am Also new here",
    "I will share nice videos, Support Everyone, add me as a friend i will also add you",
    "Friends ?, Support Together and can succeeedddd",
    "Add me as a new friend, i will also add you...",
    "come to my channel and support me, i will also support you"
    ]


scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]



def main(argv):
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    mychannelid = ""
    ytvid_id = ""
    params_validation="python cmnt-reply.py -c <mychannelid> -v <ytvid_id>"
    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = "yt-secret.json"

    try:
        opts, args = getopt.getopt(argv,"hc:v:")
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


    # Get credentials and create an API client
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, scopes)
    credentials = flow.run_console()
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials)



    ## Check the non-spam comments
    cmnt_request = youtube.commentThreads().list(
        part="snippet,replies",
        maxResults=1000,
        order="time",
        videoId=ytvid_id
    )
    cmnt_response = cmnt_request.execute()



    for item in cmnt_response["items"]:
        randomnum = randint(0,4)
        cmnt_commentid = item["id"];
        cmnt_commentown = item["snippet"]["topLevelComment"]["snippet"]["authorDisplayName"]

        
        print(cmnt_commentid + " and " + cmnt_commentown);


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
            cmnt_reply = youtube.comments().insert(
                part="snippet",
                body=dict(
                snippet=dict(
                    parentId=cmnt_commentid,
                    textOriginal= my_wishes[randomnum] + cmnt_commentown + ",  " + my_replies[randomnum]
                )
                )
            )
            cmnt_response = cmnt_reply.execute()
            print("Successfully Send the reply to " + cmnt_commentown)


    print("Worked...!");



if __name__ == "__main__":
    main(sys.argv[1:])
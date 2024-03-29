import os
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
import pprint
import time
import array as arr
from random import randint
import sys, getopt



##################################################################
my_replies = [
    "This Message is to Inform you that Video Name has Updated with your Channel name, Pease have a look into the video Name before its expired",
    "Thanks For Participate on My Promotion Programs, Your Channel Name is in My Video, Its Awesome, Right ????",
    "Wow... Congratzzzz, Your Channel Name promoted on my video... You can watch the video again and comment something to promote again..!",
    "Thanks for watching my video, your channel name updated on My video Name",
    "Hey dude, your channel has promoted, Please have a look into the video name before its expired...!",
    "Happy to inform you that your channel name added in this Video name",
    "Awesome...., Your channel name looks stunning on my video Name...",
    "Please have a look into the Name and be happy",
    "hey, Check this out, My Video updated with your channel name..!",
    "Are you happy ?, Your Channel name Promoted, have a look into the video name"
    ]

my_subs = [
    "If you Like this, then support Me by Subscibing My Channel..!",
    "Support My Channel Please",
    "Please Subscribe and Like This Video If you loves my Work",
    "Help Me to Reach Subscribers",
    "Do you Like My Work..., Subscribe My Channel..",
    "Support me My Friend..!",
    "Add Me as a new Friend if you like this work",
    "Be My Friend by Subscribe My channel if you like my work",
    "Nice Work ???, Support Me by just click on the Subscribe Button",
    "Help Plzzz, Subscribe and share this video with your friends"
]


##################################################################
params_validation="\n\npython auto-reply.py -v <ytvid_id> -u <google user>\n google user : choose between 0 and 9\n"
api_service_name = "youtube"
api_version = "v3"
scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]



##################################################################

def main(argv):
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    # os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    ytvid_id = "" # no need to change anything here
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
            ytvid_id = arg
        elif opt in ("-u"):
            google_user = arg

    if ytvid_id and len(ytvid_id) >= 3:
        print ("Video ID is ", ytvid_id)
        ytvid_id = ytvid_id
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


    ## Get channel ID
    mychannel_request = youtube.channels().list(
        part="statistics",
        mine=True
    )
    mychannel_response = mychannel_request.execute()
    mychannelid = mychannel_response["items"][0]["id"]


    while 1:
        randomnum_1 = randint(0,9)
        randomnum_2 = randint(0,9)

        ## Check the non-spam comments
        cmnt_request = youtube.commentThreads().list(
            part="snippet,replies",
            videoId=ytvid_id
        )
        cmnt_response = cmnt_request.execute()

        cmnt_data = cmnt_response["items"][0];
        cmnt_commentid = cmnt_data["id"];
        cmnt_commentown = cmnt_data["snippet"]["topLevelComment"]["snippet"]["authorDisplayName"]
        cmnt_ytchannel = cmnt_commentown.replace(" ", "")


        ## get views and video name
        vidname_request = youtube.videos().list(
            part="snippet,contentDetails,statistics",
            id=ytvid_id
        )
        vidname_response = vidname_request.execute()

        vidname_data = vidname_response["items"][0];
        vidname_snippet = vidname_data["snippet"];
        vidname_title = vidname_snippet["title"];
        vidname_views = str(vidname_data["statistics"]["viewCount"]);

        print("Current video Name : " + vidname_title)
        print(vidname_views)



        ## updating the video name
        change = (vidname_views not in vidname_title)

        if(change):
            vidname_title = "This Video Has " + vidname_views + " Views, Promotion Channel : #" + cmnt_ytchannel;
            vidname_snippet["title"] = vidname_title

            change_request = youtube.videos().update(
                part="snippet",
                body={
                    "id": ytvid_id,
                    "snippet": vidname_snippet
                }
            )
            change_response = change_request.execute()


            ## vaidate reply
            reply_check = "null"
            if "replies" in cmnt_data:
                replies_data = cmnt_data["replies"];
                for reply in replies_data["comments"]:
                    reply_check = "null"
                    reply_own = reply["snippet"]["authorChannelId"]["value"]
                    # print(reply_own)
                    contain = (reply_own in mychannelid)
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
                        textOriginal=my_replies[randomnum_1] + "\n\n" + my_subs[randomnum_2]
                    )
                    )
                )
                cmnt_response = cmnt_reply.execute()


        print("Worked...!");
        time.sleep(600)




if __name__ == "__main__":
    main(sys.argv[1:])
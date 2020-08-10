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
params_validation="\n\npython auto-sub.py -v <ytvid_id> -u <google user>\n google user : choose between 0 and 9\n"
cmnt_maxresult = 50
cmnt_minresult = 30
mysub_maxcount = 500
mysub_delcount = 90
targetsub_maxcount = 10000
waittime = 20
maxsmiles = 3
api_service_name = "youtube"
api_version = "v3"
scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]



##################################################################

smile_replies = [
    "😍",
    "😊",
    "😃",
    "😁",
    "❤️",
    "💞",
    "💖",
    "💫",
    "🎶",
    "🙏",
    "💃",
    "😻",
    "👀",
    "❄️",
    "🐥",
    "🌷",
    "🌹",
    "🍁",
    "🌺",
    "🌲",
    "🌝",
    "💝",
    "🎁",
    "🔔",
    "📣",
    "🔈",
    "🎭",
    "💎",
    "🔥",
    "👋",
    "👌",
    "😽",
    "🌟",
    "💘",
    "💗",
    "😁",
    "🍀",
    "🌼",
    "💐",
    "🌞"
]



##################################################################

support_replies_0 = [
    "വീഡിയോ",
    "ഈവീഡിയോ",
    "വീഡിയോസ്",
    "ചാനൽ",
    "_വീഡിയോ",
    "ഈവീഡിയോ_സ്",
    "കോൺടെന്റ്",
    "_ഈവീഡി_യോ",
    " ചാന_ൽ",
    "വിഡിയോസൊക്കെ",
    "ടോപ്പിക്ക്",
    "വീ_ഡിയോസ്",
    "ഇ_വീഡിയോ",
    "ദൃശ്യ സൂപ്പറാണ്,",
    "വീഡിയോ_ടോപ്പിക്ക്",
    "_വീഡിയോയോ",
    "ഇ_ദൃശ്യ",
    "വിഡിയോ_യോ",
    "ഈ_വീഡിയോ_",
    "തന്റെ_വീഡിയോ"
]


support_replies_1 = [
    "കൊള്ളാട്ടോ,",
    "നന്നായിട്ടുണ്ടെ",
    "അടിപൊളി",
    "സൂപ്പർ",
    "കിടു",
    "അടിപൊളിയായി",
    "കൊള്ളാമെ,",
    "കൊള്ളാ_ട്ടോ",
    "കൊള്ളാമല്ലൊ",
    "കണ്ടൂട്ടോ",
    "കൊള്ളാമല്ലോ",
    "സൂപ്പറായി",
    "സൂപ്പര്,",
    "സൂപ്പറാണ്",
    "സൂപ്പറാ_ണ്",
    "കൊള്ളാ",
    "കൊള്ളാ_മേ,",
    "കിടുക്കി",
    "കിടുക്കിയിട്ടുണ്ടേ",
    "സൂപ്പറായിട്ടു_ഉണ്ടേ"
]


support_replies_2 = [
    "ഞാൻ",
    "കൂട്ട്",
    "ഞാനും",
    "കൂട്ടായി",
    "ഞനും",
    "ഫ്രണ്ട്",
    "പുതിയ_കൂട്ട്",
    "ഞാന്_കൂട്ടായിട്ടു",
    "ഞാനങ്,",
    "ഞാ_ൻ",
    "_ഞാനും",
    "നമ്മൾ",
    "നമ്മളും",
    "നമ്മൽ_",
    "നമ്മള്",
    "ഞാനിങ്ങു",
    "ഞാൻ_ഓടി",
    "ഞാനും_കൂട്ടായിട്ടു",
    "ഞാനങ്_",
    "ഞാൻ_കൂട്ട്കൂടാൻ_"
]


support_replies_3 = [
    "എത്തീ",
    "കൂടി",
    "വന്നു",
    "വന്നേ,",
    "എത്തിയെ",
    "ആയിട്ടുണ്ട്",
    "എത്തിപ്പോയി,",
    "വന്നൂട്ടോ",
    "വന്നേ_",
    "കൂട്ടാ_യ്",
    "എത്തി_പ്പോയി",
    "എത്തി_ട്ടോ,",
    "കമ്പനി_ആയി",
    "എത്തി_പ്പോയെന്നേ",
    "വന്നേന്നേ,",
    "പോന്നു",
    "എത്തിട്ടുണ്ടേ",
    "എത്തിട്ടൊന്നെ,",
    "കൂടായിട്ടു_ണ്ടെ",
    "ഓടി_എത്തിയെ"
]


support_replies_4 = [
    "അങ്ങോട്ടും",
    "എന്റെ_എടുത്തേക്കും",
    "ഇങ്ങു",
    "അങ്ങ്",
    "തിരിച്ചു",
    "അങ്ങോട്ടുമ്മ്",
    "അങ്ങോ_ട്ടു",
    "അങ്ങും_",
    "എന്റെ_ചാനലിലും",
    "തിരി_ച്ചും",
    "അങ്ങോട്ടെ_ക്കും",
    "എന്റെ_ചാനലിൽ",
    "തിരിച്ചും_",
    "തിരിചു",
    "അങ്ങ്ങ്ങ്",
    "_അങ്ങ്ങ്ങ്",
    "തിരിച്ചു_വേഗം",
    "തിരിച്ചും_കൂട്ടായിട്ടു",
    "എന്റെ_yt_ചാനലിൽ",
    "തിരിച്ചു_വേഗം"
]


support_replies_5 = [
    "വരണേ",
    "വരൂ",
    "വാ",
    "പോരെ",
    "വായോ",
    "പൊരേറ്റൊന്നെ",
    "പോര്",
    "പോരെന്ന്",
    "പോരെ_",
    "പോരെ_ന്ന്",
    "വരാമോ?",
    "വാരാണാ_റ്റോ",
    "പ്രേതീഷിക്കുന്നു",
    "വരുമെന്ന്",
    "പോരെന്നെ_",
    "പോരാമോ?",
    "പോരേരേ",
    "വരാമോ_വേഗം?",
    "_വരണേ?",
    "വരുന്നേ"
]


########### function main
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
        print ("Initial Video ID : " + ytvid_id)
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

    subscribe_count = 0
    waittime_sec = waittime * 60
    print("Going to run the loop with waittime = " + str(waittime) + " mins (" + str(waittime_sec) + " sec)")


    ## Get channel ID
    mychannel_request = youtube.channels().list(
        part="statistics",
        mine=True
    )
    mychannel_response = mychannel_request.execute()
    mychannelid = mychannel_response["items"][0]["id"]

##################################################################
    while 1:
        ## Check Subscriber Count
        checksubdel_request = youtube.subscriptions().list(
            part="snippet",
            maxResults=50,
            mine=True,
            order="relevance"
        )
        checksubdel_response = checksubdel_request.execute()
        mysubcount = checksubdel_response["pageInfo"]["totalResults"]

        ## Delete `mysub_delcount` Subscribers 
        if int(mysubcount) >= mysub_maxcount:
            print("Your Channel : " + mychannelid + " subscribed to " + str(mysubcount) + "\nNeed to Delete " + str(mysub_delcount) + " Subscribed channels")
            subdel_channel = []
            list_subdel = ""
            arr_subdel = ""
            subdel_pagetoken = ""

            while 1:
                subdel_request = youtube.subscriptions().list(
                    part="snippet",
                    maxResults=50,
                    mine=True,
                    order="relevance",
                    pageToken=subdel_pagetoken
                )
                subdel_response = subdel_request.execute()

                subdel_channel += subdel_response["items"]
                subdel_pagetoken = subdel_response.get("nextPageToken")

                if subdel_pagetoken == "" or len(subdel_channel) >= mysub_delcount:
                    break

            for delchannels in subdel_channel:
                list_subdel += delchannels["id"] + ","

            arr_subdel = list_subdel.split(',')
            print("Number subscribers listed for delete : " + str(len(arr_subdel)))

            for subremove in arr_subdel[:-1]:
                subremove_request = youtube.subscriptions().delete(
                    id=subremove
                )
                print("Removing subscription ID : " + subremove)
                subremove_response = subremove_request.execute()


##################################################################

        prev_ytvid_id = ytvid_id
        getsub_request = youtube.videos().list(
            part="snippet",
            id=ytvid_id
        )
        getsub_response = getsub_request.execute()

        subchannelid = getsub_response["items"][0]["snippet"]["channelId"]


        random_support_replies_0 = randint(0,19)
        random_support_replies_1 = randint(0,19)
        random_support_replies_2 = randint(0,19)
        random_support_replies_3 = randint(0,19)
        random_support_replies_4 = randint(0,19)
        random_support_replies_5 = randint(0,19)

        ## Smiles 
        my_smile_num = 0
        # mid smiles
        mid_smile_reply = ""
        mid_smile_num = randint(1,maxsmiles)
        while my_smile_num < mid_smile_num:
            random_smile_replies = randint(0,39)
            mid_smile_reply += smile_replies[random_smile_replies]
            my_smile_num = my_smile_num + 1

        my_smile_num = 0
        # end smiles
        end_smile_reply = ""
        end_smile_num = randint(1,maxsmiles)
        while my_smile_num < end_smile_num:
            random_smile_replies = randint(0,39)
            end_smile_reply += smile_replies[random_smile_replies]
            my_smile_num = my_smile_num + 1


        my_replies = support_replies_0[random_support_replies_0] + " " + support_replies_1[random_support_replies_1] + " " + mid_smile_reply + " " + support_replies_2[random_support_replies_2] + " " + support_replies_3[random_support_replies_3] + " " + support_replies_4[random_support_replies_4] + " " + support_replies_5[random_support_replies_5] + " " + end_smile_reply
        print("my_replies is : " + my_replies)

        ## commenting on the channel
        mycmnt_request = youtube.commentThreads().insert(
            part="snippet",
            body=dict(
                snippet=dict(
                    videoId=ytvid_id,
                    topLevelComment=dict(
                        snippet=dict(
                            textOriginal=my_replies
                        )
                    )
                )
            )
        )
        mycmnt_response = mycmnt_request.execute()

        ## subscribe
        print(mychannelid + " Going to subscribe the channel : " + subchannelid + " by commenting on the video : " + ytvid_id)
        subadd_request = youtube.subscriptions().insert(
            part="contentDetails,snippet",
            body=dict(
                snippet=dict(
                    resourceId=dict(
                    channelId=subchannelid,
                    kind="youtube#channel"
                    )
                )
            )
        )
        subadd_response = subadd_request.execute()

        subscribe_count = subscribe_count + 1
        print("Total Subscribed Channel in this loop : " + str(subscribe_count))


##################################################################

        nextcmnt_request = youtube.commentThreads().list(
            part="snippet,replies",
            maxResults=cmnt_maxresult,
            order="relevance",
            videoId=ytvid_id
        )
        nextcmnt_response = nextcmnt_request.execute()


        for nextcmntitem in nextcmnt_response["items"][2:]:
            nextchannelid = nextcmntitem["snippet"]["topLevelComment"]["snippet"]["authorChannelId"]["value"]

            if nextchannelid == mychannelid:
                print("This is my channel ID, Looking for another channel ID")
            else:
                ## Check Subscribers Count
                validsub_request = youtube.channels().list(
                    part="statistics",
                    id=nextchannelid
                )
                validsub_response = validsub_request.execute()
                validhiddensub_status = validsub_response["items"][0]["statistics"]["hiddenSubscriberCount"]
                validsub_count = validsub_response["items"][0]["statistics"]["subscriberCount"]

                if int(validsub_count) > targetsub_maxcount and validhiddensub_status == False:
                    print("Subscribers count is greater than " + str(targetsub_maxcount) + " for channel : " + nextchannelid)
                else:
                    ## Check Subscription
                    subcheck_request = youtube.subscriptions().list(
                        part="snippet,contentDetails",
                        channelId=mychannelid,
                        forChannelId=nextchannelid
                    )
                    subcheck_response = subcheck_request.execute()

                    if len(subcheck_response["items"]) >= 1:
                        print(mychannelid + " Already Subscribed to this channel")
                        sub_check = "found"
                    else:
                        sub_check = "null"

                        ## Take Uploads Playlist ID
                        nextcontent_request = youtube.channels().list(
                            part="contentDetails",
                            id=nextchannelid
                        )
                        nextcontent_response = nextcontent_request.execute()

                        if len(nextcontent_response["items"]) < 1:
                            print(nextchannelid + " has no playlist")
                        else:
                            uploads_id = nextcontent_response["items"][0]["contentDetails"]["relatedPlaylists"]["uploads"]

                            ## New Video ID
                            nextplvid_request = youtube.playlistItems().list(
                                playlistId=uploads_id,
                                part="snippet",
                                maxResults=1
                            )
                            nextplvid_response = nextplvid_request.execute()

                            if len(nextplvid_response["items"]) < 1:
                                print(nextchannelid + " Hasn't any video")
                            else:
                                nextytvid_id = nextplvid_response["items"][0]["snippet"]["resourceId"]["videoId"]

                                ## Validate comments are turned on or off
                                nextcmntoffon_request = youtube.videos().list(
                                    part="statistics",
                                    id=nextytvid_id
                                )
                                nextcmntoffon_response = nextcmntoffon_request.execute()

                                cmntkey_to_ckeck = 'commentCount'
                                if cmntkey_to_ckeck not in nextcmntoffon_response['items'][0]['statistics']:
                                    print("Comments are turned off for this video : " + nextytvid_id)
                                else:
                                    ## Check comments
                                    nextcheckcmnt_request = youtube.commentThreads().list(
                                        part="snippet,replies",
                                        maxResults=cmnt_maxresult,
                                        order="relevance",
                                        videoId=nextytvid_id
                                    )
                                    nextcheckcmnt_response = nextcheckcmnt_request.execute()

                                    nextcmnt_count = len(nextcheckcmnt_response["items"])

                                    if nextcmnt_count < cmnt_minresult:
                                        print("The new channel : " + nextchannelid + " , video : " + nextytvid_id + " has not enough comments : " + str(nextcmnt_count))
                                    else:
                                        print("The new channel : " + nextchannelid + " , video : " + nextytvid_id + " has enough comments : " + str(nextcmnt_count))

                                        if len(nextcheckcmnt_response["items"]) < 1:
                                            print("On Channel " + nextchannelid + ", no one commented yet")
                                        else:
                                            cmnt_check = ""
                                            for nextcheckcmnt in nextcheckcmnt_response["items"][:2]:
                                                cmnt_commentown = nextcheckcmnt["snippet"]["topLevelComment"]["snippet"]["authorDisplayName"]
                                                cmnt_channelid = nextcheckcmnt["snippet"]["topLevelComment"]["snippet"]["authorChannelId"]["value"]

                                                ## Check I commented or not
                                                if mychannelid == cmnt_channelid:
                                                    cmnt_check = "found"
                                                    print(mychannelid + " already commented on this video : " + nextytvid_id)
                                                    break
                                                else:
                                                    cmnt_check = "null"

                                            if cmnt_check == 'null':
                                                ytvid_id = nextytvid_id
                                                print("Previous Video ID : " + prev_ytvid_id + "\n Next Video ID : " + ytvid_id + "\n")
                                                now = datetime.now(timezone.utc)
                                                nextexe = (now + timedelta(minutes=waittime)).astimezone()
                                                print("Sleeping for " + str(waittime) + " mins (" + str(waittime_sec) + " sec). Next exe at : {nextexe:%I:%M %p}".format(**vars()))
                                                time.sleep(waittime_sec)
                                                break

if __name__ == "__main__":
    main(sys.argv[1:])
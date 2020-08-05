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
params_validation="\n\npython cmnt-reply.py -c <mychannelid> -v <ytvid_id> -u <google user> -f <yes or no>\n google user : choose between 0 and 9\n -f option is for confirm whether it is featured channel or not"
maxresult = 50
maxrespond = 20
waittime = 4
api_service_name = "youtube"
api_version = "v3"
scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]




##################################################################

support_replies_f = [
    "feature",
    "_feature",
    "feature_",
    "ഫീച്ചർ_ർ",
    "featurre",
    "ffeature",
    "featuree,",
    "_featuree",
    "featuree_,",
    "ഫീച്ചർർ",
    "featured,",
    "featured_",
    "_featured",
    "_ഫീച്ചർ",
    "featuredd.,",
    "ffeatured",
    "featurred",
    "ഫീച്ചർ_",
    "yt_ഫീച്ചർ",
    "ഫീച്ചർ"
]

support_replies_0 = [
    "എന്റെ",
    "പുതിയ‌",
    "ഏതുനമ്മുടെ",
    "എന്റെ_ഈ",
    "എന്റെഈ",
    "എന്റെ_",
    "നമ്മുടെ‌",
    "എന്റെയും",
    "യൂട്യൂബിൽഎന്റെ",
    "എന്റെഗെ",
    "എന്നെ",
    "എന്റെ,,",
    "എന്റെന്റെ,",
    "എന്റെയൂട്യൂബ്",
    "എന്റേത്",
    "എന്റെcoc",
    "_എന്റെഈ",
    "എന്റെപുതിയ",
    "നന്മുടെ",
    "എന്എന്റെ"
]

support_replies_1 = [
    "ചാനൽൽ",
    "_ചാനൽ_",
    "ചാനല്",
    "ചാനലിൽ",
    "യൂട്യൂബ്ചാനലിൽ",
    "യൂട്യൂബ്ചാനൽ",
    "യൂട്യൂബ്_ചാനൽ,",
    "yt_ചാനലിൽ",
    "ചാനൽ,",
    "ചാനനൽ",
    "ചാനൽ_,",
    "_ചാനൽ",
    "ചാ_നൽ",
    "ചാന_ൽ",
    "ചാനൽ.,",
    "ചാനൽs",
    "(ചാനൽ",
    "ചാനൽ_)",
    "yt_ചാനൽ_",
    "ചാനൽ_ൽ"
]

support_replies_2 = [
    "ഒന്ന്നോക്കാമോ",
    "ആണ്ഇത്‌",
    "ഗെയിമിംഗ്_ആണേ",
    "കേറി_നോക്കണേ",
    "നോക്കണേ",
    "സ്റ്റാർട്ട്ചെയ്തു",
    "ആണ്_ഇത്‌",
    "കേറിഒന്ന്നോക്കണേ",
    "തുടങ്ങിയിട്_കൂട്ടുകാരെ",
    "ആണ്എന്റെ",
    "തുടങ്ങി_",
    "തുടങ്ങിയിട്ടോ",
    "കേറി_നോക്കൂ",
    "നോക്കാമോ",
    "കേറിനോക്കണേ",
    "അനാട്ടോഎന്റേത്",
    "കൊള്ളാമോ",
    "എങ്ങനെഉണ്ട്",
    "ഗെയിമിംഗ്ചാനൽ_കൊള്ളാമോ",
    "വീഡിയോസ്ഒന്ന്_കാണാമോ"
]



##################################################################
friends_replies_0 = [
    "എങ്ങോട്ടു",
    "എങ്ങോ_ട്ടു",
    "ഇങ്ങോട്ടു",
    "ഇ_ങ്ങോട്ടു",
    "ഇങ്ങു",
    "എന്റെ",
    "ഇങ്",
    "എന്റെ",
    "എൻറെ",
    "എൻ്റെ",
    "ഏന്റെന്റ",
    "എങ്ങു",
    "ഇവിടേക്കു",
    "നമ്മുടേ",
    "നമ്മുടെ",
    "ഇവിടെ",
    "നമ്മടെ",
    "നമ്മടേ",
    "എന്റ",
    "ഇവിടേക്ക്"
]

friends_replies_1 = [
    "കൂട്ടാകാൻ",
    "കൂട്ടാ_കാൻ",
    "ഫ്രണ്ട്",
    "കൂട്ടായിട്ടു",
    "കൂ_ട്ടായിട്ടു",
    "കൂട്ടായി",
    "കൂട്ടായിയി",
    "കൂട്ടായ്",
    "ഫ്രണ്ട്ആയി",
    "കൂട്ടായ്ട്ടു",
    "കമ്പനിയായി",
    "കൂട്ടുകൂടാൻ",
    "കൂട്ടു_കൂടാനും",
    "കൂട്ടുകൂടാന്",
    "ഫ്രണ്ട്ആയിട്ടു",
    "ഫ്രണ്ട്_അകാൻ",
    "സുഹൃത്",
    "സുഹൃത്_അകാൻ",
    "കൂടെ_കൂടാൻ",
    "കൂടെകൂടാനയി"
]

friends_replies_2 = [
    "വരുമോ?",
    "ആകാമോ?",
    "വരുന്നോ",
    "_വരാമോ",
    "ആയിക്കോ",
    "ആകു",
    "പോരെ",
    "വരു?",
    "വരണേ",
    "ചെയ്യണേ",
    "വരുന്നേ",
    "ആയിവന്നേ",
    "ഓടിപോരെ",
    "എങ്ങു_പോരെന്നെ",
    "സ്വാഗതം",
    "വരുവോ",
    "വാ",
    "വായോ?",
    "പോരെന്നെ?",
    "വ_രാമോ?"
]

friends_replies_3 = [
    "അങ്ങോട്ടും",
    "അങ്ങും",
    "തിരിച്ചും",
    "അങ്ങോ_ട്ടും",
    "അവിടെ",
    "ഞാനും",
    "അവിടെക്ക്",
    "അവിടേ_ക്കും",
    "അവിടെത്തെക്ക്",
    "അ_വിടെത്തെക്ക്",
    "അവിടെത്തെക്കും",
    "അനോട്ടു",
    "ആങ്ങും",
    "അങോട്ടും",
    "അങോ_ട്ടും",
    "അ_നോട്ടു",
    "തന്റെ",
    "തന്റെ",
    "അങ്ങോട്ടേക്",
    "അവിടെത്തെ_ക്കും"
]

friends_replies_4 = [
    "കൂട്ടാകാൻ വരാം",
    "വരാമേ",
    "ഞാൻ വരാം",
    "ഞാൻവരാം_ കൂട്ടാകാൻ..",
    "ഞാൻ_ഫ്രണ്ട്ആയി വരാമേ",
    "കൂട്ടായേക്കാം",
    "ഉടൻ കൂട്ടായി വന്നേക്കാം",
    "എപ്പോൾതന്നെ വരാം",
    "ഫ്രണ്ട്_ആകാം",
    "ഫുൾ സപ്പോട്ട്_ഉണ്ടാകും",
    "വരാമേ_ഫ്രണ്ട് ആയിട്ട്യ്",
    "പെട്ടെന്ന് വന്നേക്കാം",
    "വന്നേക്കാം അനോട്ടേക്കു",
    "കേറി വന്നേക്കാം",
    "വരാ_മേ",
    "കൂട്ടാകാം",
    "ചാനലിലൊട്ടും കൂട്ടായേക്കാം",
    "ചാനൽ_ഫ്രണ്ട് ആയേക്കാമെ",
    "ഏതോയേക്കാം",
    "എത്താം"
]


########### function main
def main(argv):
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    # os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    mychannelid = "" # no need to change anything here
    ytvid_id = "" # no need to change anything here
    google_user = "" # no need to change anything here
    feature_channel = "" # no need to change anything here

    try:
        opts, args = getopt.getopt(argv,"hc:v:u:")
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
        elif opt in ("-f"):
            feature_channel = arg

    if mychannelid and len(mychannelid) >= 3:
        print("Your Channel ID is ", mychannelid)
        mychannelid = mychannelid
    else:
        print(params_validation)
        sys.exit(2)

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

    if feature_channel == "yes":
        print ("This channel is for promote featured channel")
    elif feature_channel == "no":
        print ("This is your Actual Channel")
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


    waittime_sec = waittime * 60 * 60
    comment_count = 0
    print("Going to run the loop with waittime = " + str(waittime) + " hrs (" + str(waittime_sec) + " sec)")

    while 1:

        prev_ytvid_id = ytvid_id
        ## Check the non-spam comments
        cmnt_request = youtube.commentThreads().list(
            part="snippet,replies",
            maxResults=maxresult,
            order="time",
            videoId=ytvid_id
        )
        cmnt_response = cmnt_request.execute()

        for item in cmnt_response["items"][1:maxrespond]:

            random_support_replies_f = randint(0,19)
            random_support_replies_0 = randint(0,19)
            random_support_replies_1 = randint(0,19)
            random_support_replies_2 = randint(0,19)
            random_friends_replies_0 = randint(0,19)
            random_friends_replies_1 = randint(0,19)
            random_friends_replies_2 = randint(0,19)
            random_friends_replies_3 = randint(0,19)
            random_friends_replies_4 = randint(0,19)

            if feature_channel == "no":
                my_replies = support_replies_0[random_support_replies_0] + " " + support_replies_1[random_support_replies_1] + " " +  support_replies_2[random_support_replies_2] + ", " + friends_replies_0[random_friends_replies_0] + " " + friends_replies_1[random_friends_replies_1] + " " + friends_replies_2[random_friends_replies_2] + " " + friends_replies_3[random_friends_replies_3] + " " + friends_replies_4[random_friends_replies_4]
            elif feature_channel == "yes":
                my_replies = support_replies_0[random_support_replies_0] + " " + support_replies_f[random_support_replies_f] + " " + support_replies_1[random_support_replies_1] + " " +  support_replies_2[random_support_replies_2] + ", " + friends_replies_0[random_friends_replies_0] + " " + friends_replies_1[random_friends_replies_1] + " " + friends_replies_2[random_friends_replies_2] + " " + friends_replies_3[random_friends_replies_3] + " " + friends_replies_4[random_friends_replies_4]
            else:
                sys.exit(2)

            cmnt_commentid = item["id"];
            cmnt_commentown = item["snippet"]["topLevelComment"]["snippet"]["authorDisplayName"]


            ## vaidate reply
            arr_mychannelid = mychannelid.split(',')
            reply_check = "null"
            if "replies" in item:
                replies_data = item["replies"];
                for reply in replies_data["comments"]:
                    reply_check = "null"
                    reply_own = reply["snippet"]["authorChannelId"]["value"]
                    # print(reply_own)
                    contain = (reply_own in arr_mychannelid)
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
                reply = youtube.comments().insert(
                    part="snippet",
                    body=dict(
                    snippet=dict(
                        parentId=cmnt_commentid,
                        textOriginal=my_replies
                    )
                    )
                )
                reply_response = reply.execute()
                print("Successfully Send the reply to " + cmnt_commentown)

            print("Sleeping for 10 sec")
            time.sleep(10)


        print("Total Reply : " + str(comment_count))

######################################################

        for cmntitem in cmnt_response["items"][1:maxresult]:
            cmnt_commentownid = cmntitem["snippet"]["topLevelComment"]["snippet"]["authorChannelId"]["value"]

            ## Check Subscribers Count
            sub_request = youtube.channels().list(
                part="statistics",
                id=cmnt_commentownid
            )
            sub_response = sub_request.execute()
            sub_count = sub_response["items"][0]["statistics"]["subscriberCount"]

            if int(sub_count) < maxresult:
                print("Subscribers count is less than " + str(maxresult) + " for channel : " + cmnt_commentown)
            else:
                print(cmnt_commentown + "Has Subscribers count : " + sub_count)


                ## Take Uploads Playlist ID
                content_request = youtube.channels().list(
                    part="contentDetails",
                    id=cmnt_commentownid
                )
                content_response = content_request.execute()
                uploads_id = content_response["items"][0]["contentDetails"]["relatedPlaylists"]["uploads"]
                print("uploads Playlist's ID :" + uploads_id)


                ## New Video ID
                plvid_request = youtube.playlistItems().list(
                    playlistId=uploads_id,
                    part="snippet",
                    maxResults=1
                )
                plvid_response = plvid_request.execute()
                ytvid_id = plvid_response["items"][0]["snippet"]["resourceId"]["videoId"]


                ## Check Comments length
                newcmnt_request = youtube.commentThreads().list(
                    part="snippet,replies",
                    maxResults=maxresult,
                    order="time",
                    videoId=ytvid_id
                )
                newcmnt_response = newcmnt_request.execute()

                cmnt_count = len(newcmnt_response["items"])
                if cmnt_count < maxrespond:
                    print("The new video has not enough comments : " + str(cmnt_count))
                else:
                    now = datetime.now(timezone.utc)
                    nextexe = (now + timedelta(hours=waittime)).astimezone()

                    print("Previous Video ID : " + prev_ytvid_id + "\n")
                    print("The new video : " + ytvid_id + "has " + str(cmnt_count) + " comments \n")
                    print("Sleeping for " + str(waittime) + " hrs (" + str(waittime_sec) + " sec). Next exe at : {nextexe:%I:%M %p}".format(**vars()))
                    time.sleep(waittime_sec)
                    break






if __name__ == "__main__":
    main(sys.argv[1:])
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
params_validation="\n\npython auto-sub-precmnt-reply.py -v <ytvid_id> -u <google user>\n google user : choose between 0 and 9\n"

targetsub_maxcount = 10000
targetsub_mincount = 50
mysub_maxcount = 500
mysub_delcount = 20
cmnt_maxresult = 20
cmnt_maxrespond = 5

# maxsmiles = 3
waittime = 120
api_service_name = "youtube"
api_version = "v3"
scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]



# ##################################################################

# smile_replies = [
#     "😍",
#     "😊",
#     "😃",
#     "😁",
#     "❤️",
#     "💞",
#     "💖",
#     "💫",
#     "🎶",
#     "🙏",
#     "💃",
#     "😻",
#     "👀",
#     "❄️",
#     "🐥",
#     "🌷",
#     "🌹",
#     "🍁",
#     "🌺",
#     "🌲",
#     "🌝",
#     "💝",
#     "🎁",
#     "🔔",
#     "📣",
#     "🔈",
#     "🎭",
#     "💎",
#     "🔥",
#     "👋",
#     "👌",
#     "😽",
#     "🌟",
#     "💘",
#     "💗",
#     "😁",
#     "🍀",
#     "🌼",
#     "💐",
#     "🌞"
# ]



##################################################################


support_replies_0 = [
    "_എന്റെ",
    "പു_തിയ‌",
    "ഏതു_നമ്മുടെ",
    "എ_ന്റെഈ",
    "എന്റെ_ഈ_",
    "എന്റെ_.",
    "ന_മ്മുടെ‌",
    "എന്റെ_യും",
    "യൂട്യൂബിൽ_എന്റെ",
    "എന്റെ_ഗെ",
    "എ_ന്നെ",
    "എ_ന്റെ,,",
    "എന്റെ_ന്റെ,",
    "എന്റെ_യൂട്യൂബ്",
    "എന്റേ_ത്",
    "എന്റെ_c",
    "_എന്റെ_ഈ",
    "എന്റെ_പുതിയ",
    "നന്മു_ടെ",
    "എന്_എന്റെ"
]

support_replies_1 = [
    "ചാനൽ_ൽ",
    "_ചാന_ൽ_",
    "ചാനല്",
    "ചാനലി_ൽ",
    "യൂട്യൂബ്_ചാനലിൽ",
    "യൂട്യൂബ്_ചാനൽ",
    "_യൂട്യൂബ്ചാനൽ,",
    "_yt_ചാനലിൽ",
    "_ചാന_ൽ,",
    "ചാനന_ൽ_",
    "ചാനൽ_,",
    "_ചാനൽ",
    "ചാ_നൽ",
    "ചാന_ൽ",
    "_ചാനൽ.,",
    "_ചാനൽs",
    "_(ചാനൽ",
    "ചാനൽ_)",
    "yt_ചാനൽ_",
    "_ചാനൽ_ൽ"
]

support_replies_2 = [
    "ഒന്ന്_നോക്കാമോ",
    "ആണ്_ഇത്‌",
    "_ആണേ_",
    "കേറി_നോ_ക്കണേ",
    "നോക്ക_ണേ",
    "സ്റ്റാർട്ട്_ചെയ്തു",
    "ആണ്_ഇത്‌_",
    "കേറിഒന്ന്_നോക്കണേ",
    "_തുടങ്ങിയിട്_കൂട്ടുകാരെ",
    "_ആണ്_എന്റെ",
    "_തുടങ്ങി_",
    "_തുടങ്ങി_യിട്ടോ",
    "കേറി_നോക്കൂ_",
    "നോ_ക്കാമോ_",
    "കേറി_നോക്കണേ_",
    "അനാട്ടോ_എന്റേത്_",
    "കൊള്ളാ_മോ_",
    "എങ്ങനെ_ഉണ്ട്",
    "ഗെ ചാനൽ_കൊള്ളാമോ",
    "വീഡിയോസ്_ഒന്ന്_കാണാമോ"
]



##################################################################
friends_replies_0 = [
    "_എങ്ങോട്ടു",
    "എ_ങ്ങോ_ട്ടു",
    "_ഇങ്ങോട്ടു",
    "_ഇ_ങ്ങോട്ടു",
    "ഇ_ങ്ങു",
    "എന്റെ_",
    "ഇങ്_",
    "എ_ന്റെ",
    "_എൻറെ",
    "എ_ൻ്റെ",
    "_ഏന്റെന്റ",
    "എ_ങ്ങു",
    "ഇവി_ടേക്കു",
    "നമ്മുടേ_",
    "ന_മ്മുടെ",
    "_ഇവി_ടെ",
    "_നമ്മടെ_",
    "ന_മ്മടേ_",
    "എ_ന്റ",
    "ഇവിടേക്ക്_"
]

friends_replies_1 = [
    "കൂട്ടാകാൻ_",
    "കൂട്ടാ_കാൻ_",
    "_ഫ്രണ്ട്_",
    "കൂട്ടാ_യിട്ടു",
    "കൂ_ട്ടായിട്ടു_",
    "കൂ_ട്ടായി_",
    "കൂട്ടാ_യിയി",
    "കൂ_ട്ടായ്_",
    "_ഫ്രണ്ട്ആയി",
    "കൂട്ടാ_യ്ട്ടു",
    "കമ്പനി_യായി",
    "കൂട്ടു_കൂടാൻ",
    "കൂട്ടു_കൂടാനും_",
    "കൂട്ടുകൂടാന്_",
    "_ഫ്ര_ണ്ട്ആയിട്ടു",
    "ഫ്രണ്ട്_അകാൻ",
    "സുഹൃ_ത്",
    "സുഹൃത്_അകാൻ_",
    "കൂടെ_കൂടാ_ൻ",
    "കൂടെ_കൂടാനയി_"
]

friends_replies_2 = [
    "വരു_മോ?",
    "ആകാമോ_?",
    "വരുന്നോ_",
    "_വ_രാമോ",
    "ആയി_ക്കോ",
    "ആകു_",
    "പോ_രെ",
    "വരു_?",
    "വര_ണേ",
    "ചെയ്യ_ണേ",
    "വ_രുന്നേ",
    "ആയി_വന്നേ",
    "ഓടി_പോരെ",
    "എ_ങ്ങു_പോരെന്നെ",
    "സ്വാ_ഗതം",
    "വരുവോ_",
    "വാ_.",
    "വാ_യോ?",
    "പോരെ_ന്നെ?",
    "വ_രാ_മോ?"
]

friends_replies_3 = [
    "അ_ങ്ങോട്ടും",
    "അങ്_ങും",
    "തിരിച്_ചും",
    "അങ്ങോ_ട്ടും_",
    "_അവിടെ_",
    "ഞാ_നും",
    "അവി_ടെക്ക്",
    "അ_വിടേ_ക്കും",
    "അവി_ടെത്തെ_ക്ക്",
    "അ_വിടെ_ത്തെക്ക്",
    "അവി_ടെത്തെ_ക്കും",
    "അനോ_ട്ടു",
    "ആ_ങ്ങും_",
    "അ_ങോട്ടും_",
    "അങോ_ട്ടും",
    "അ_നോട്ടു_",
    "ത_ന്റെ_",
    "_തന്റെ",
    "അ_ങ്ങോട്ടേക്",
    "അവി_ടെത്തെ_ക്കും"
]

friends_replies_4 = [
    "കൂ_ട്ടാകാൻ വരാം",
    "വരാ_മേ",
    "ഞാൻ-വരാം_",
    "ഞാൻവരാം_ കൂട്ടാ_കാൻ..",
    "ഞാൻ_ഫ്രണ്ട്_ആയി-വരാമേ",
    "കൂട്ടായേ_ക്കാം",
    "ഉടൻ കൂ_ട്ടായി വന്നേക്കാം",
    "എപ്പോൾത_ന്നെ വരാം",
    "ഫ്രണ്ട്_ആ_കാം",
    "ഫുൾ_സപ്പോട്ട്_ഉണ്ടാകും",
    "വ_രാമേ_ഫ്രണ്ട് ആയിട്ട്യ്",
    "പെ_ട്ടെന്ന് വ_ന്നേക്കാം",
    "വന്നേക്കാം അനോട്ടേ_ക്കു",
    "കേറി വന്നേ_ക്കാം",
    "വരാ_മേ",
    "കൂട്ടാകാം_",
    "ചാനലിലൊട്_ടും കൂ_ട്ടായേക്കാം",
    "ചാനൽ_ഫ്രണ്ട്_ ആ_യേക്കാമെ",
    "ഏതോയേ_ക്കാം",
    "എ_ത്താം"
]


##################################################################

sub_replies_0 = [
    "വീ_ഡിയോ",
    "ഈവീ_ഡിയോ",
    "വീഡിയോ_സ്",
    "ചാനൽ_",
    "_വീ_ഡിയോ",
    "ഈവീഡി_യോ_സ്",
    "കോൺടെ_ന്റ്",
    "_ഈവീ_ഡി_യോ",
    " ചാന_ൽ_",
    "വിഡിയോസൊ_ക്കെ",
    "ടോപ്പി_ക്ക്",
    "വീ_ഡിയോ_സ്",
    "ഇ_വീഡിയോ_",
    "ദൃശ്യ സൂ_പ്പറാണ്,",
    "വീഡിയോ_ടോപ്പി_ക്ക്",
    "_വീ_ഡിയോയോ",
    "ഇ_ദൃശ്യ_",
    "വിഡിയോ_യോ_",
    "ഈ_വീ_ഡിയോ_",
    "തന്റെ_വീഡിയോ_"
]


sub_replies_1 = [
    "കൊ_ള്ളാട്ടോ,",
    "നന്നാ_യിട്ടുണ്ടെ",
    "അടിപൊളി_",
    "സൂപ്പർ_",
    "കി_ടു",
    "അടി_പൊളിയായി",
    "കൊള്ളാ_മെ,",
    "കൊള്ളാ_ട്ടോ_",
    "കൊ_ള്ളാമല്ലൊ",
    "കണ്ടൂ_ട്ടോ",
    "കൊള്ളാമ_ല്ലോ",
    "സൂപ്പ_റായി",
    "സൂപ്പര്_,",
    "സൂ_പ്പറാണ്",
    "_സൂപ്പറാ_ണ്",
    "കൊ_ള്ളാ",
    "കൊ_ള്ളാ_മേ,",
    "കിടു_ക്കി_",
    "കിടുക്കിയിട്ടു_ണ്ടേ",
    "സൂപ്പ_റായിട്ടു_ഉണ്ടേ"
]


sub_replies_2 = [
    "_ഞാൻ",
    "കൂ_ട്ട്",
    "ഞാനും_",
    "കൂ_ട്ടായി",
    "ഞ_നും",
    "ഫ്ര_ണ്ട്",
    "പുതി_യ_കൂട്ട്",
    "ഞാ_ന്_കൂട്ടായിട്ടു",
    "ഞാന_ങ്,",
    "ഞാ_ൻ_",
    "_ഞാനും_",
    "നമ്മ_ൾ",
    "നമ്മ_ളും",
    "_നമ്മൽ_",
    "ന_മ്മള്",
    "ഞാനി_ങ്ങു",
    "ഞാൻ_ഓടി_",
    "ഞാനും_കൂട്ടാ_യിട്ടു",
    "ഞാ_നങ്_",
    "ഞാ_ൻ_കൂട്ട്കൂടാൻ_"
]


sub_replies_3 = [
    "_എത്തീ",
    "കൂ_ടി",
    "വന്നു_",
    "വന്നേ_,",
    "എ_ത്തിയെ",
    "ആയി_ട്ടുണ്ട്",
    "എത്തി_പ്പോയി,",
    "വന്നൂട്ടോ_",
    "വ_ന്നേ_",
    "കൂ_ട്ടാ_യ്",
    "എ_ത്തി_പ്പോയി",
    "_എത്തി_ട്ടോ,",
    "ക_മ്പനി_ആയി",
    "എ_ത്തി_പ്പോയെന്നേ",
    "വന്നേ_ന്നേ,",
    "പോന്നു_",
    "എത്തി_ട്ടുണ്ടേ",
    "എത്തി_ട്ടൊന്നെ,",
    "കൂ_ടായിട്ടു_ണ്ടെ",
    "_ഓടി_എത്തിയെ"
]


sub_replies_4 = [
    "_അങ്ങോട്ടും",
    "എ_ന്റെ_എടുത്തേക്കും",
    "ഇങ്ങു_",
    "അങ്ങ്_",
    "തി_രിച്ചു",
    "അ_ങ്ങോട്ടുമ്മ്",
    "അ_ങ്ങോ_ട്ടു",
    "_അങ്ങും_",
    "_എന്റെ_ചാനലിലും",
    "_തിരി_ച്ചും",
    "അ_ങ്ങോട്ടെ_ക്കും",
    "_എന്റെ_ചാനലിൽ",
    "തി_രിച്ചും_",
    "തിരി_ചു",
    "അ_ങ്ങ്ങ്ങ്",
    "_അ_ങ്ങ്ങ്ങ്",
    "തി_രിച്ചു_വേഗം",
    "തിരി_ച്ചും_കൂട്ടായിട്ടു",
    "എ_ന്റെ_yt_ചാനലിൽ",
    "തി_രിച്ചു_വേഗം"
]


sub_replies_5 = [
    "_വരണേ",
    "വ_രൂ",
    "വാ_",
    "പോ_രെ",
    "വാ_യോ",
    "പൊരേ_റ്റൊന്നെ",
    "പോര്_",
    "പോരെ_ന്ന്",
    "_പോരെ_",
    "പോ_രെ_ന്ന്",
    "വരാ_മോ?",
    "വാ_രാണാ_റ്റോ",
    "പ്രേതീഷി_ക്കുന്നു",
    "വരുമെ_ന്ന്",
    "പോ_രെന്നെ_",
    "പോരാ_മോ?",
    "പോരേരേ_",
    "വരാ_മോ_വേഗം?",
    "_വര_ണേ?",
    "വരുന്നേ_"
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

    waittime_sec = waittime * 60
    subscribe_count = 0
    comment_count = 0
    print("Going to run the loop with waittime = " + str(waittime) + " min (" + str(waittime_sec) + " sec)")

    ## Get channel ID
    mychannel_request = youtube.channels().list(
        part="statistics",
        mine=True
    )
    mychannel_response = mychannel_request.execute()
    mychannelid = mychannel_response["items"][0]["id"]
    prev_ytvid_id = ""


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

                if "nextPageToken" not in subdel_response or len(subdel_channel) >= mysub_delcount:
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
        else:
            print("Your Channel : " + mychannelid + " subscribed to " + str(mysubcount))

##################################################################

        if ytvid_id == prev_ytvid_id:
            print("Previous Video and New Video are Same, Try to Run the Script again with new video ID having more comments")
            break
        else:
            prev_ytvid_id = ytvid_id

            getsub_request = youtube.videos().list(
                part="snippet",
                id=ytvid_id
            )
            getsub_response = getsub_request.execute()
            subchannelid = getsub_response["items"][0]["snippet"]["channelId"]

            random_sub_replies_0 = randint(0,19)
            random_sub_replies_1 = randint(0,19)
            random_sub_replies_2 = randint(0,19)
            random_sub_replies_3 = randint(0,19)
            random_sub_replies_4 = randint(0,19)
            random_sub_replies_5 = randint(0,19)


            my_sub_replies = sub_replies_0[random_sub_replies_0] + " " + sub_replies_1[random_sub_replies_1] + " " + sub_replies_2[random_sub_replies_2] + " " + sub_replies_3[random_sub_replies_3] + " " + sub_replies_4[random_sub_replies_4] + " " + sub_replies_5[random_sub_replies_5]
            print("my_sub_replies is : " + my_sub_replies)

            ## commenting on the channel
            mycmnt_request = youtube.commentThreads().insert(
                part="snippet",
                body=dict(
                    snippet=dict(
                        videoId=ytvid_id,
                        topLevelComment=dict(
                            snippet=dict(
                                textOriginal=my_sub_replies
                            )
                        )
                    )
                )
            )

            ## subscribe
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
            try:
                print(mychannelid + " Going to subscribe the channel : " + subchannelid + " by commenting on the video : " + ytvid_id)
                subadd_response = subadd_request.execute()
                mycmnt_response = mycmnt_request.execute()
            except:
                print("An exception occurred, " + mychannelid + " Not able to subscribe the channel : " + subchannelid + " but commented on the video : " + ytvid_id)

            subscribe_count = subscribe_count + 1
            print("Total Subscribed Channel in this loop : " + str(subscribe_count))
            

    ##################################################################

            ## Check the non-spam comments
            cmnt_request = youtube.commentThreads().list(
                part="snippet,replies",
                maxResults=50,
                order="time",
                videoId=ytvid_id
            )
            cmnt_response = cmnt_request.execute()

            for item in cmnt_response["items"][2:cmnt_maxrespond]:

                random_support_replies_0 = randint(0,19)
                random_support_replies_1 = randint(0,19)
                random_support_replies_2 = randint(0,19)
                random_friends_replies_0 = randint(0,19)
                random_friends_replies_1 = randint(0,19)
                random_friends_replies_2 = randint(0,19)
                random_friends_replies_3 = randint(0,19)
                random_friends_replies_4 = randint(0,19)

                # ## Smiles 
                # my_smile_num = 0
                # # mid smiles
                # mid_smile_reply = ""
                # mid_smile_num = randint(1,maxsmiles)
                # while my_smile_num < mid_smile_num:
                #     random_smile_replies = randint(0,39)
                #     mid_smile_reply += smile_replies[random_smile_replies]
                #     my_smile_num = my_smile_num + 1

                # my_smile_num = 0
                # # end smiles
                # end_smile_reply = ""
                # end_smile_num = randint(1,maxsmiles)
                # while my_smile_num < end_smile_num:
                #     random_smile_replies = randint(0,39)
                #     end_smile_reply += smile_replies[random_smile_replies]
                #     my_smile_num = my_smile_num + 1

                # my_replies = support_replies_0[random_support_replies_0] + " " + support_replies_1[random_support_replies_1] + " " +  support_replies_2[random_support_replies_2] + ", " + mid_smile_reply + " " + friends_replies_0[random_friends_replies_0] + " " + friends_replies_1[random_friends_replies_1] + " " + friends_replies_2[random_friends_replies_2] + " " + friends_replies_3[random_friends_replies_3] + " " + friends_replies_4[random_friends_replies_4] + end_smile_reply
                my_replies = support_replies_0[random_support_replies_0] + " " + support_replies_1[random_support_replies_1] + " " +  support_replies_2[random_support_replies_2] + " " + friends_replies_0[random_friends_replies_0] + " " + friends_replies_1[random_friends_replies_1] + " " + friends_replies_2[random_friends_replies_2] + " " + friends_replies_3[random_friends_replies_3] + " " + friends_replies_4[random_friends_replies_4]

                cmnt_commentid = item["id"];
                cmnt_commentown = item["snippet"]["topLevelComment"]["snippet"]["authorDisplayName"]


                ## vaidate reply
                reply_check = "null"
                if "replies" in item:
                    replies_data = item["replies"];
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


            print("Total Reply in this loop : " + str(comment_count))

            now = datetime.now(timezone.utc)
            nextexe = (now + timedelta(minutes=waittime)).astimezone()
            print("Sleeping for " + str(waittime) + " min (" + str(waittime_sec) + " sec). Next exe at : {nextexe:%I:%M %p}".format(**vars()))
            time.sleep(waittime_sec)



    ##################################################################

            for cmntitem in cmnt_response["items"][1:cmnt_maxresult]:
                cmnt_commentownid = cmntitem["snippet"]["topLevelComment"]["snippet"]["authorChannelId"]["value"]

                if cmnt_commentownid == mychannelid:
                    print("This is my channel ID, Looking for another channel ID")
                else:
                    ## Check Subscribers Count
                    sub_request = youtube.channels().list(
                        part="statistics",
                        id=cmnt_commentownid
                    )
                    sub_response = sub_request.execute()
                    sub_response_status = sub_response["items"][0]["statistics"]["hiddenSubscriberCount"]
                    sub_count = sub_response["items"][0]["statistics"]["subscriberCount"]

                    if int(sub_count) < targetsub_mincount:
                        print("Subscribers count is less than " + str(targetsub_mincount) + " for channel : " + cmnt_commentown)
                    elif int(sub_count) > targetsub_maxcount:
                        print("Subscribers count is greater than " + str(targetsub_maxcount) + " for channel : " + cmnt_commentown)
                    else:
                        print(cmnt_commentown + "Has Subscribers count : " + sub_count)

                        ## Check Subscription
                        subcheck_request = youtube.subscriptions().list(
                            part="snippet,contentDetails",
                            channelId=mychannelid,
                            forChannelId=cmnt_commentownid
                        )
                        subcheck_response = subcheck_request.execute()

                        if len(subcheck_response["items"]) >= 1:
                            print(mychannelid + " Already Subscribed to this channel")
                        else:
                            ## Take Uploads Playlist ID
                            content_request = youtube.channels().list(
                                part="contentDetails",
                                id=cmnt_commentownid
                            )
                            content_response = content_request.execute()

                            if len(content_response["items"]) < 1:
                                print(cmnt_commentownid + " has no playlist")
                            else:
                                uploads_id = content_response["items"][0]["contentDetails"]["relatedPlaylists"]["uploads"]
                                print("uploads Playlist's ID :" + uploads_id)

                                ## New Video ID
                                plvid_request = youtube.playlistItems().list(
                                    playlistId=uploads_id,
                                    part="snippet",
                                    maxResults=1
                                )
                                plvid_response = plvid_request.execute()

                                if len(plvid_response["items"]) < 1:
                                    print(cmnt_commentownid + " Hasn't any video")
                                else:
                                    ytvid_id = plvid_response["items"][0]["snippet"]["resourceId"]["videoId"]
                                    ## Validate comments are turned on or off
                                    cmntoffon_request = youtube.videos().list(
                                        part="statistics",
                                        id=ytvid_id
                                    )
                                    cmntoffon_response = cmntoffon_request.execute()

                                    cmntkey_to_ckeck = 'commentCount'
                                    if cmntkey_to_ckeck not in cmntoffon_response['items'][0]['statistics']:
                                        print("Comments are turned off for this video : " + ytvid_id)
                                    else:
                                        cmntcountcheck = cmntoffon_response["items"][0]["statistics"]["commentCount"]
                                        if cmntcountcheck == "0":
                                            print("Comments are turned off for this video : " + ytvid_id)
                                        else:
                                            ## Check Comments length
                                            newcmnt_request = youtube.commentThreads().list(
                                                part="snippet,replies",
                                                maxResults=50,
                                                order="time",
                                                videoId=ytvid_id
                                            )
                                            newcmnt_response = newcmnt_request.execute()

                                            cmnt_count = len(newcmnt_response["items"])
                                            if cmnt_count < cmnt_maxresult:
                                                print("The new video has not enough comments : " + str(cmnt_count))
                                            else:
                                                print("Previous Video ID : " + prev_ytvid_id + "\n")
                                                print("The new video : " + ytvid_id + " has " + str(cmnt_count) + " comments \n")
                                                break






if __name__ == "__main__":
    main(sys.argv[1:])
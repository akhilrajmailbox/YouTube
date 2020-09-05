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
params_validation="\n\n python sub-del.py -s <max sub number persist> -d <max sub number to delete> -u <google user>\n google user : choose between 0 and 9\n"

api_service_name = "youtube"
api_version = "v3"
waittime = 720
scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]



########### function main
def main(argv):
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    # os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    mysub_maxcount = "" # no need to change anything here
    mysub_delcount = "" # no need to change anything here
    google_user = "" # no need to change anything here

    try:
        opts, args = getopt.getopt(argv,"hs:d:u:")
    except getopt.GetoptError:
        print(params_validation)
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print(params_validation)
            sys.exit()
        elif opt in ("-s"):
            mysub_maxcount = arg
        elif opt in ("-d"):
            mysub_delcount = arg
        elif opt in ("-u"):
            google_user = arg


    if mysub_maxcount and len(mysub_maxcount) >= 1:
        print ("Maximum Subscribers Count need to Persist : " + mysub_maxcount)
    else:
        print(params_validation)
        sys.exit(2)

    if mysub_delcount and len(mysub_delcount) >= 1:
        print ("Maximum Subscribers Count need to Delete : " + mysub_delcount)
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
        if int(mysubcount) >= int(mysub_maxcount):
            print("Your Channel subscribed to " + str(mysubcount) + "\nNeed to Delete " + str(mysub_delcount) + " Subscribed channels")
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

                if "nextPageToken" not in subdel_response or len(subdel_channel) >= int(mysub_delcount):
                    break

            for delchannels in subdel_channel:
                list_subdel += delchannels["id"] + ","

            arr_subdel = list_subdel.split(',')
            print("Number subscribers listed for delete : " + mysub_delcount)

            for subremove in arr_subdel[:int(mysub_delcount)]:
                subremove_request = youtube.subscriptions().delete(
                    id=subremove
                )
                print("Removing subscription ID : " + subremove)
                subremove_response = subremove_request.execute()

        else:
            print("Your Channel subscribed to " + str(mysubcount))


        waittime_sec = waittime * 60
        now = datetime.now(timezone.utc)
        nextexe = (now + timedelta(minutes=waittime)).astimezone()
        print("Sleeping for " + str(waittime) + " min (" + str(waittime_sec) + " sec). Next exe at : {nextexe:%I:%M %p}".format(**vars()))
        time.sleep(waittime_sec)



if __name__ == "__main__":
    main(sys.argv[1:])
YTapiKey = "INSERT KEY HERE"

from googleapiclient.discovery import build
import sys
import os
import os.path
from pytube import YouTube
import cropVideos
import glob
import CombineVideos


def searchYoutube(query, numResults):
    youtube = build('youtube', 'v3', developerKey=YTapiKey)

    # creates a dictionary of the youtube search
    # (q = query, part = 'snippet', type = 'channel,video',maxResult = # you want to see)
    request = youtube.search().list(q=query, part='snippet',
                                    type='video', maxResults=numResults)
    request = request.execute()
    ytURL = 'https://www.youtube.com/watch?v='
    urlQuery = []
    titleQuery = []

    for item in request['items']:
        videoId = item['id']['videoId']
        # print(item['snippet']['title'])
        # print(ytURL + videoId)
        titleQuery.append(item['snippet']['title'])
        urlQuery.append(ytURL + videoId)
    return urlQuery, titleQuery


def downloadVideos360p(urlQuery, clipCut):  # downloads 360p video object

    for url in urlQuery:
        filesOld = os.listdir('videos')
        prevVideos = os.listdir('videos')
        yt = YouTube(url)
        title = yt.title
        yt = yt.streams.filter(file_extension='mp4',
                               progressive=True, res="360p").first()
        if yt != None:
            print('Currently Downloading Video for: ' + title)
            yt.download('videos')
            filesNew = os.listdir('videos')
            file = list(set(filesNew) - set(filesOld))
            cropVideos.cropVideo(file[0], clipCut)
        else:
            print("Unable to Download - " + title)


# downloads 720p video and audio individually to later be combined
def downloadVideos720p(urlQuery, clipCut):
    for url in urlQuery:
        # prevents cropping videos that were previously cropped
        prevVideos = os.listdir('videos')
        yt = YouTube(url)

        print(yt.length)
        ytVideo = yt.streams.get_by_itag('136')  # check for 720p Video
        ytAudio = yt.streams.filter(only_audio=True).all()[0]
        if(ytVideo == None):
            ytVideo = yt.streams.get_by_itag('135')
            if(ytVideo == None):
                ytVideo = yt.streams.get_by_itag('134')
                if(ytVideo == None):
                    print('Video Not available')
                    continue
        if(ytVideo != None):
            print('Currently Downloading Video for: ' + yt.title)
            ytVideo.download('videos720p')
            print('Currently Downloading Audio for: ' + yt.title)
            ytAudio.download('audio720p')


def removePreviousVideos(path):
    files = os.listdir(path)
    for f in files:
        os.remove(os.path.join(path, f))


def start():

    print("\nYour clips will be saved to : {}".format('videos'))

    # Input
    query = input('What video/videos do you want from YouTube? ')
    maxResults = input('How many results do you want? ')
    try:
        val = int(maxResults)
    except ValueError:
        raise Exception("Please input an integer")
    clipCut = input(
        'Lastly,when do you want the clip to end? "min:sec" NOTE: min>=1, sec<60 & Time cannot be longer than video  ')
    clipCut = clipCut.split(":")
    clipCut = tuple([int(clipCut[0]), int(clipCut[1])])
    if clipCut[0] < 1:
        raise Exception('You cannot have less than 1 minute')
    if clipCut[1] >= 60:
        raise Exception('You cannot have more than 60s')

    print("Accessing Youtube Query...")
    urls, titles = searchYoutube(query, maxResults)
    delete = True
    while(delete):
        count = 1
        print("Found: ")
        for title in titles:
            print(str(count) + ":" + title)
            count += 1
        index = input(
            "Delete any of the Suggestions?(# of entry you dont want included, 'n' if okay) ")
        if index == 'n':
            delete = False
            break
        else:
            try:
                val = int(index)
            except ValueError:
                print("not a valid input")
                continue
            if(1 <= val <= len(urls)):
                del urls[val - 1]
                del titles[val - 1]
    if len(urls) == 0:
        print('No more clips to Download')
        start()
    print(urls)
    downloadVideos360p(urls, clipCut)
    print('You downloaded ' + str(len(titles)) + ' videos')
    print('You have ' + str(len(os.listdir('videos'))) + " total videos saved")
    more = input("Want to add more videos? y/n ")
    if more == 'y':
        start()
    else:
        print("\nCreate PowerHour of ")
        for file in os.listdir('videos'):
            if file != '.DS_Store':
                print(file)
        create = input('??? y/n ')
        if create == 'y':
            print("CREATING POWERHOUR")
            CombineVideos.combineVideos()
        else:
            print("No PowerHour is created. Clips will be saved for later")


def main():
         # clears the videos file
    fresh = input("\nCreate a Fresh PowerHour? y/n ")
    # song query, number of requests, start(sec) of 60s clip, if new collection of vids
    if fresh == 'y':  # create a new clip collection for the power hour
        print("Erasing all previous videos")
        removePreviousVideos('videos')
    start()


if __name__ == "__main__":
    main()

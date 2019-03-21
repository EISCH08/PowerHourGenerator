import gatherClips
import cropVideos
import os
from pytube import YouTube

def downloadVideos360p(urlQuery,clipCut):#downloads 360p video object

	for url in urlQuery:
		filesOld = os.listdir('videos')
		prevVideos = os.listdir('videos')
		yt = YouTube(url)
		title = yt.title
		yt = yt.streams.filter(file_extension = 'mp4',progressive = True, res = "360p").first()
		if yt!=None:
			print('Currently Downloading Video for: '+ title)
			yt.download('videos')
			filesNew = os.listdir('videos')
			file = list(set(filesNew) - set(filesOld))
			cropVideos.cropVideo(file[0],clipCut)
		else:
			print("Unable to Download - "+ title)
			
		
#gatherClips.downloadVideos360p(['https://www.youtube.com/watch?v=FTQbiNvZqaY','https://www.youtube.com/watch?v=YVkUvmDQ3HY'],(1,5))
downloadVideos360p(['https://www.youtube.com/watch?v=nYCURBSSyXw'],(1,0))
#cropVideos.cropAllVideos([]

import sys, os, os.path
from moviepy.editor import *
import random


def combineVideos():
	titles = os.listdir('videos')
	random.shuffle(titles)
	clips = []
	for title in titles:
		if title != '.DS_Store':
			video = VideoFileClip('videos/'+title)
			clips.append(video)
	count = 0
	for clip in clips:
		if count !=0:
			clip.crossfadein(1)
		count+=1
	titleClip = VideoFileClip('PowerHourIntro.mp4')
	clips = [titleClip] + clips			
	finalClip = concatenate_videoclips(clips, method ='compose')
	finalClip.write_videofile('POWERHOUR!.mp4',codec='libx264', audio_codec='aac',temp_audiofile='temp-audio.m4a', remove_temp=True,fps =30)
	pwNumber =  len(os.listdir('completedPWs'))+1
	os.rename('POWERHOUR!.mp4', 'completedPWs/POWERHOUR'+str(pwNumber)+'!.mp4')
def main():
	combineVideos()

if __name__ == "__main__":
	main()





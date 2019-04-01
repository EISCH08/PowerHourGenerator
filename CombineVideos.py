
import sys
import os
import os.path
from moviepy.editor import *
import random


def combineVideos():
    titles = os.listdir('videos')
    random.shuffle(titles) #randomizes order of the titles
    clips = []
    for title in titles: #creates the Moviepy clip object and adds it to the clip array
        if title != '.DS_Store': #does not include random DS File
            video = VideoFileClip('videos/' + title)
            clips.append(video)
    count = 0
    for clip in clips: #adds a fade to the clips
        if count != 0:
            clip.crossfadein(1)
        count += 1
    titleClip = VideoFileClip('PowerHourIntro.mp4')
    clips = [titleClip] + clips
    finalClip = concatenate_videoclips(clips, method='compose') #concates the clips together
    pwNumber = len(os.listdir('completedPWs')) + 1
    #creates the clip and saves
    finalClip.write_videofile('completedPWs/POWERHOUR' + str(pwNumber) +'!.mp4', codec='libx264', audio_codec='aac',
                              temp_audiofile='temp-audio.m4a', remove_temp=True, fps=30)
    

def main():
    combineVideos()


if __name__ == "__main__":
    main()

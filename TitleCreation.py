from moviepy.editor import *
import os

def titleCreation():
	countdownAudio = AudioFileClip('audio/countdownTimer.mp3')
	countdownAudio = countdownAudio.subclip(10,20) #strips only the countdown section
	beerCrackAudio = AudioFileClip('audio/beercrack.mp3')
	beercrackAudio = beerCrackAudio.subclip(5,7)
	beerCrackAudio = beercrackAudio.volumex(2)

	title = TextClip(txt='Welcome to my Powerhour', color ='white', bg_color='black',fontsize = 50)
	titleClip = title.set_duration(3)
	titleClip.wrtie_videofile('TitleClip.mov',codec='libx264', audio_codec='aac',temp_audiofile='temp-audio.m4a', remove_temp=True)


def main():
	titleCreation()

if __name__ == "__main__":
	main()
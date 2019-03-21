from moviepy.editor import *
import os


def cropVideo(title,clipCut):
	min,sec = clipCut
	video = VideoFileClip('videos/'+title)
	videoedited = video.subclip((min-1,sec),(clipCut))
	logoOut = (ImageClip("keystone.png")
      .set_duration(4)
      .resize(height=200) # if you need to resize...
      .margin(right=8, top=8, opacity=0) # (optional) logo-border padding
      .set_pos(("center")))
	logoIn = (ImageClip("keystone.png")
      .set_duration(1)
      .resize(height=200)
      .margin(right=8, top=8, opacity=0) # (optional) logo-border padding
      .set_pos(("center")))
	beerCrack = AudioFileClip('audio/beercrack.mp3')
	beerCrack = beerCrack.subclip(5,7)
	beerCrack = beerCrack.volumex(2)
	final = CompositeVideoClip([videoedited,logoIn.set_start(0).crossfadeout(.5),logoOut.set_start(56.00).crossfadein(.5)])
	audioClip = CompositeAudioClip([final.audio.volumex(1),beerCrack.set_start(58.00)])
	final.audio = audioClip
	final.write_videofile(title,codec='libx264', audio_codec='aac',temp_audiofile='temp-audio.m4a', remove_temp=True)
	os.rename(title, "videos/"+title)





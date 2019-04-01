from moviepy.editor import *
import os


def cropVideo(title, clipCut):
    min, sec = clipCut
    video = VideoFileClip('videos/' + title)
    # crops a 60 sec clip from 60s before clipcut
    videoedited = video.subclip((min - 1, sec), (clipCut))
    logoOut = (ImageClip("keystone.png")  # adds keystone fade in
               .set_duration(4)
               .resize(height=200)  # if you need to resize...
               # (optional) logo-border padding
               .margin(right=8, top=8, opacity=0)
               .set_pos(("center")))
    logoIn = (ImageClip("keystone.png")  # adds keystone fade out
              .set_duration(1)
              .resize(height=200)
              # (optional) logo-border padding
              .margin(right=8, top=8, opacity=0)
              .set_pos(("center")))
    # adds the beer crack sound
    beerCrack = AudioFileClip('audio/beercrack.mp3')
    beerCrack = beerCrack.subclip(5, 7)
    beerCrack = beerCrack.volumex(2)
    final = CompositeVideoClip([videoedited, logoIn.set_start(
        0).crossfadeout(.5), logoOut.set_start(56.00).crossfadein(.5)])
    audioClip = CompositeAudioClip(
        [final.audio.volumex(1), beerCrack.set_start(58.00)])
    final.audio = audioClip
    final.write_videofile(title, codec='libx264', audio_codec='aac',
                          temp_audiofile='temp-audio.m4a', remove_temp=True)
    os.rename(title, "videos/" + title)

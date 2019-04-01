# PowerHourGenerator

This is a program that generates PowerHours based off of a users desired searches.

Reference to what PowerHours are:

https://www.youtube.com/watch?v=IZ9FLVBKmo0&t=1407s


This was mainly created due to my friends and I's need of wanting to make a custom PowerHour because the lack of them online. This project was mainly created for fun and should be used only for that. 

## What I Learned
I learned how to navigate the Youtube API and edit videos using Moviepy

## How to use the PowerHour Generator

Gain Access to Youtube API Libraries:
```
pip install --upgrade google-api-python-client
pip install --upgrade google-auth google-auth-oauthlib google-auth-httplib2
```

Install Pytube
 
``pip install pytube``

Get API key from youtube and replace it to the YouTubeSearch ``YTapiKey`` variable

After all packages are installed, run 

python gatherClips.py

Follow instructions in the terminal to generate your own PowerHour!

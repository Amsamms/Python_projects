pip install youtube_dl

from __future__ import unicode_literals
import youtube_dl

url = "https://www.youtube.com/playlist?list=PL5-da3qGB5ID7YYAqireYEew2mWVvgmj6" # this is the link of the desired playlist

ydl_opts = {}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])
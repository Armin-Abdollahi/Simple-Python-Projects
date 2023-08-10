#!/usr/bin/env python
# coding: utf-8

# In[ ]:


pip install pytube


# In[ ]:


from pytube import YouTube

# Enter the video link
video_url = input("Enter the YouTube video URL: ")

# Create YouTube object using video link
yt = YouTube(video_url)

# Show video details
print("Video Title:", yt.title)
print("Video Length:", yt.length, "seconds")
print("Video Views:", yt.views)

# Choose the download format
stream = yt.streams.get_highest_resolution()

# video download
print("Downloading...")
stream.download()
print("Download completed!")


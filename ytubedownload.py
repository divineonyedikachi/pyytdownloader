from pytube import YouTube

def Download(link):
  youtubeObject = YouTube(link)
  youtubeObject = youtubeObject.streams.get_highest_resolution()
  try:
      youtubeObject.download()
  except:
    print("There has been an error in downloading your youtube video")
  print("This download has completed!")

link = input("Enter YouTube URL: ")
Download(link)
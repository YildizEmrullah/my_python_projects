import pytube

url = input("enter your video url:")

path = ""
pytube.Youtube(url).streams.get_highest_resolution().download(path)
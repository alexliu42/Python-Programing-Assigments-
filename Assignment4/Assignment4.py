from bs4 import BeautifulSoup
import requests
import os

if not os.path.exists("Assignment4_Downloaded_Pics"):
	os.mkdir("Assignment4_Downloaded_Pics")

endpoint = "https://wallhaven.cc/search"

p = { "categories": "100", "purity": "100", "topRange":"1y", "sorting": "toplist", "order": "desc" }

response = requests.get(endpoint, params = p)

mainPageSoup = BeautifulSoup(response.content, features = "html.parser")

preview = mainPageSoup.findAll("a",{"class":"preview"})

previewLinks = [ele["href"] for ele in preview]

count = 0 

for link in previewLinks:
	tempResponse = requests.get(link)
	tempPageSoup = BeautifulSoup(tempResponse.content, features = "html.parser")
	tempPic = tempPageSoup.find("img",{"id":"wallpaper"})

	finalPicLinks = tempPic["src"]
	title = tempPic["alt"]
	finalResponse = requests.get(finalPicLinks)

	with open("Assignment4_Downloaded_Pics//{}.jpg".format(title), "wb") as file:
		file.write(finalResponse.content)
		print("Downloading file %s ..." % title)
		count += 1

print("Download Completed, %d pictures downloaded" %count)
		
import requests
import pyperclip
import urllib.request

sizeOne = input("Enter x value: ")
sizeTwo = input("Enter y value: ")
fileName = input("Enter file name: ")
blurred = input("Blurred? [y/n]: ")
grayscale = input("Grayscale? [y/n]: ")
export = input("Export data about image? [y/n]: ")
if blurred == "y" and grayscale == "y":
    blurLevel = input("Enter the amount of blur (1-5): ")
    r = requests.get("https://picsum.photos/" + sizeOne + "/" + sizeTwo + "/?grayscale&blur=" + blurLevel)
elif blurred == "y":
    blurLevel = input("Enter the amount of blur (1-5): ")
    r = requests.get("https://picsum.photos/" + sizeOne + "/" + sizeTwo + "/?blur=" + blurLevel)
elif grayscale == "y":
    r = requests.get("https://picsum.photos/" + sizeOne + "/" + sizeTwo + "/?grayscale")
elif blurred != "y" and grayscale != "y":
    r = requests.get("https://picsum.photos/" + sizeOne + "/" + sizeTwo + "/")
if export == "y":
    urlLink = str(r.url)
    split = urlLink.split("/")[4] # Splits the url from requests into different sections divided by /, the ID is the fifth element (4 starting from 0)
    newR = requests.get("https://picsum.photos/id/" + split + "/info")
    urllib.request.urlretrieve(str(newR.url), fileName + ".txt")
else: 
    print("ok")
# r = requests.get("https://picsum.photos/" + sizeOne + "/" + sizeTwo + "/?blur"
urllib.request.urlretrieve(str(r.url), fileName + ".png")
print(str(r.url))
print("Image Saved")
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
    r = requests.get("https://picsum.photos/" + sizeOne + "/" + sizeTwo + "/?grayscale&blur")
elif blurred == "y":
    r = requests.get("https://picsum.photos/" + sizeOne + "/" + sizeTwo + "/?blur")
elif grayscale == "y":
    r = requests.get("https://picsum.photos/" + sizeOne + "/" + sizeTwo + "/?grayscale")
elif blurred != "y" and grayscale != "y":
    r = requests.get("https://picsum.photos/" + sizeOne + "/" + sizeTwo + "/")
if export == "y":
    urlLink = str(r.url)
    split = urlLink.split("/")[4]
    newR = requests.get("https://picsum.photos/id/" + split + "/info")
else: 
    print("")
# r = requests.get("https://picsum.photos/" + sizeOne + "/" + sizeTwo + "/?blur")
urllib.request.urlretrieve(str(r.url), fileName + ".png")
urllib.request.urlretrieve(str(newR.url), fileName + ".txt")
print("Image Saved")
print(split)
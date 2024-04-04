from bs4 import BeautifulSoup
import requests
import os

os.chdir("/home/djole/downloads/tro-mechs/")

directory = "https://www.sarna.net/wiki/index.php?title=Category:TRO_BattleMech_Images&filefrom=Ymir.jpg#mw-category-media"

links = []
image_links = []
images = []


def get_direct_links(directory):
    r = requests.get(directory)

    soup = BeautifulSoup(r.content, 'html.parser')
    urls = soup.select('a.image', href=True)
    for url in urls:
        links.append(f"https://www.sarna.net{url['href']}")

    return links


def get_image_links(next_image):
    r = requests.get(next_image)

    soup = BeautifulSoup(r.content, 'html.parser')
    urls = soup.select('a.internal', href=True)
    for url in urls:
        images.append(url['href'])

    return images


get_direct_links(directory)

for next_image in links:
    # print(next_image)
    get_image_links(next_image)

for image_url in images:
    # print(image_url)
    image_name = image_url.split('/')[-1].split('?')[0]
    print("grabbing:%s"%image_name)
    r = requests.get(image_url, stream=True)
    with open(image_name, 'wb') as f:
        for chunk in r:
            f.write(chunk)



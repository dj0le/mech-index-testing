from bs4 import BeautifulSoup
import requests

directory = "https://www.sarna.net/wiki/Category:TRO_BattleMech_Images"

links = []

def get_image_links():
    r = requests.get(directory)

    soup = BeautifulSoup(r.content, 'html.parser')
    urls = soup.select('a.image', href=True)
    for url in urls:
        links.append(f"https://www.sarna.net{url['href']}")

    return links


get_image_links()

size = len(links)
print(size)

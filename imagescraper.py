from bs4 import BeautifulSoup
import requests

directory = "https://www.sarna.net/wiki/Category:TRO_BattleMech_Images"

next_page_links = [
    "https://www.sarna.net/wiki/Category:TRO_BattleMech_Images",
    "https://www.sarna.net/wiki/index.php?title=Category:TRO_BattleMech_Images&filefrom=3055u+Wraith.jpg#mw-category-media",
"https://www.sarna.net/wiki/index.php?title=Category:TRO_BattleMech_Images&filefrom=CRK-Katana.png#mw-category-media",
"https://www.sarna.net/wiki/index.php?title=Category:TRO_BattleMech_Images&filefrom=Grizzly+Invading+Clans.jpg#mw-category-media",
"https://www.sarna.net/wiki/index.php?title=Category:TRO_BattleMech_Images&filefrom=Lightning+RGilClan+v14.png#mw-category-media",
"https://www.sarna.net/wiki/index.php?title=Category:TRO_BattleMech_Images&filefrom=Phoenix+hawk+iic.jpg#mw-category-media",
"https://www.sarna.net/wiki/index.php?title=Category:TRO_BattleMech_Images&filefrom=STN-SENTINEL.png#mw-category-media",
"https://www.sarna.net/wiki/index.php?title=Category:TRO_BattleMech_Images&filefrom=Ymir.jpg#mw-category-media"
]

links = []

def get_image_links(next_page):
    r = requests.get(next_page)

    soup = BeautifulSoup(r.content, 'html.parser')
    urls = soup.select('a.image', href=True)
    for url in urls:
        links.append(f"https://www.sarna.net{url['href']}")

    return links

for next_page in next_page_links:
    print(next_page)
    get_image_links(next_page)



size = len(links)
print(size)

with open("mechlist1", "w") as mechlist1:
    mechlist1.write("\n".join(links))

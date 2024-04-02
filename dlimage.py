from bs4 import BeautifulSoup
import requests
import os

os.chdir("/home/djole/downloads/battlemechs/")

image_links = []
images = []

with open('/home/djole/python-dev/mech-index/mechlist1') as f:
    image_links = [line.strip() for line in f]
    # lines = f.read().splitlines()
    # image_links.append(lines)

print(image_links)

def get_image_links(next_image):
    r = requests.get(next_image)

    soup = BeautifulSoup(r.content, 'html.parser')
    urls = soup.select('a.internal', href=True)
    for url in urls:
        images.append(url['href'])

    return images

for next_image in image_links:
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




# size = len(images)
# print(size)


# with open("mechfile", "w") as mechfile:
#     mechfile.write("\n".join(links))



# print(next_page_links)

# def scrape_page(url):
#     print ("URL: " + url)
#     r = requests.get(url)
#     soup = BeautifulSoup(r.content, "html.parser")
    
#     next_page_link = soup.find('a', )
#     if next_page_link is not None:
#         href = next_page_link.get("href")
#         scrape_page(href)
#         print(next_page_link)
#     else:
#         print ("Done")

# scrape_page(directory)




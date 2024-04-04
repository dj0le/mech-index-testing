from bs4 import BeautifulSoup
import requests
import pandas as pd

url = "http://www.masterunitlist.info/Unit/Filter?Name=&HasBV=true&HasBV=false&MinTons=&MaxTons=&MinBV=&MaxBV=&MinIntro=&MaxIntro=&MinCost=&MaxCost=&Roles=Ambusher&Roles=Attack&Roles=Brawler&Roles=Dogfighter&Roles=Fast+Dogfighter&Roles=Fire-Support&Roles=Interceptor&Roles=Juggernaut&Roles=Missile+Boat&Roles=None&Roles=Scout&Roles=Skirmisher&Roles=Sniper&Roles=Striker&Roles=Transport&HasBFAbility=&MinPV=&MaxPV=&Technologies=1&Technologies=2&Rules=55&Rules=4&Rules=5&Types=18&BookAuto=&FactionAuto=&SubTypes=29&SubTypes=45&Eras=10&Eras=11&Eras=255&Eras=256&Eras=13"

page = requests.get(url)

# print(page.status_code)

soup = BeautifulSoup(page.text,'html.parser')

# Find the table
html_table = soup.find(class_="table")

headers = []
for element in html_table.find_all("th"):
    title = element.text
    headers.append(title)

# print(headers)
    
# create a dataframe
mechindex = pd.DataFrame(columns = headers)


for table_row in html_table.find_all("tr")[1:]:
    row_data = table_row.find_all("td")
    row = [element.text for element in row_data]
    length = len(mechindex)
    mechindex.loc[length] = row

mechindex.drop(columns=['', 'TRO/RS', 'Rules', 'Era'], inplace=True)
print(mechindex)

mechindex.to_csv("mechindex.csv", index=False)
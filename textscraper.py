from bs4 import BeautifulSoup
import requests
import pandas as pd

url = "http://www.masterunitlist.info/Unit/Filter?Name=&HasBV=true&HasBV=false&MinTons=&MaxTons=&MinBV=&MaxBV=&MinIntro=&MaxIntro=&MinCost=&MaxCost=&Roles=Ambusher&Roles=Attack&Roles=Brawler&Roles=Dogfighter&Roles=Fast+Dogfighter&Roles=Fire-Support&Roles=Interceptor&Roles=Juggernaut&Roles=Missile+Boat&Roles=None&Roles=Scout&Roles=Skirmisher&Roles=Sniper&Roles=Striker&Roles=Transport&HasBFAbility=&MinPV=&MaxPV=&Technologies=1&Technologies=2&Rules=55&Rules=4&Rules=5&Types=18&BookAuto=&FactionAuto=&SubTypes=29&SubTypes=45&Eras=10&Eras=11&Eras=255&Eras=256&Eras=13"

page = requests.get(url)

# print(page.status_code)

soup = BeautifulSoup(page.content,'html.parser')

# Find the table
table = soup.find(class_="table")

# Find all table rows
rows = table.find_all('tr')
1
with open('battlemechs.txt', 'w') as f:
    for row in rows:
        data = row.find_all("td")
        name = data[0].get_text() if len(data) > 0 else "Name of Mech"
        tonnage = data[2].get_text() if len(data) > 2 else "Tonnage"
        bv = data[3].get_text() if len(data) > 3 else "BV"
        pv = data[4].get_text() if len(data) > 4 else "PV"
        role = data[5].get_text() if len(data) > 5 else "Role"
        intro = data[9].get_text() if len(data) > 9 else "Date"

        print(f'Name : {name} | Tons: {tonnage} | BV: {bv} | PV: {pv} | Role: {role} | Date: {intro}')

        f.write(
            f'Name : {name} | Tons: {tonnage} | BV: {bv} | PV: {pv} | Role: {role} | Date: {intro}\n')

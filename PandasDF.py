import requests
import pandas as pd
from bs4 import BeautifulSoup

statnameslist = []
nameslist = []
page = requests.get("https://www.fangraphs.com/leaders.aspx?pos=all&stats=bat&lg=all&qual=y&type=0&season=2018&month=0&season1=2018&ind=0&team=0&rost=0&age=0&filter=&players=0")
soup = BeautifulSoup(page.content,'html.parser')
table = soup.find('div', class_="RadGrid RadGrid_FanGraphs")
theader = table.find('thead')
statnamesraw = theader.find_all('th')

for stat in statnamesraw:
    stat=stat.text.strip()
    statnameslist.append(stat)

statnameslist.remove('#')
statnameslist.remove('Name')
df = pd.DataFrame(index=statnameslist)


tbody = table.find('tbody')
tablerows = tbody.find_all('tr')
for row in tablerows:
    stat_values = []
    player_row = row.find_all('td')
    nameraw = player_row[1]
    name = nameraw.text.strip()
    if name not in nameslist:
        nameslist.append(name)
    for rawstat in player_row:
        stat = rawstat.text.strip()
        stat_values.append(stat)
    data = stat_values
    df[name] = pd.Series(data[2:], index = statnameslist) #Slicing to remove Name and Team pulled from Fangraphs table

print(df)

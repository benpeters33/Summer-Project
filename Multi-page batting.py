#Ben Test File
import requests
import pandas as pd
from bs4 import BeautifulSoup
masterdict = {}
#COLLECTS THE STANDARD STATS OF ALL QUALIFIED BATTERS FROM FANGRAPHS
battingpages = [{'pos':'all', 'stats':'bat', 'lg':'all', 'qual':'y', 'type':'0', 'season':'2018', 'month':'0', 'team':'0', 'rost':'0',  'age':'0', 'filter' :'', 'players':'0', 'page':'1_500'}, {'pos':'all', 'stats':'bat', 'lg':'all', 'qual':'y', 'type':'1', 'season':'2018', 'month':'0', 'team':'0', 'rost':'0',  'age':'0', 'filter':'', 'players':'0', 'page':'1_500'},{'pos':'all', 'stats':'bat', 'lg':'all', 'qual':'y', 'type':'2', 'season':'2018', 'month':'0', 'team':'0', 'rost':'0',  'age':'0', 'filter':'', 'players':'0', 'page':'1_500'}, {'pos':'all', 'stats':'bat', 'lg':'all', 'qual':'y', 'type':'3', 'season':'2018', 'month':'0', 'team':'0', 'rost':'0',  'age':'0', 'filter':'', 'players':'0', 'page':'1_500'}]


def addtodict(player, year, source, statname, value):
    if player in masterdict:
        masterdict[player][year][source][statname] = value
    else:
        masterdict[player]={year:{source: {stat:value}}}

def test(testplayers = ['Mike Trout', 'Bryce Harper']):
    for player in testplayers:
        print(masterdict[player][2018]['FANGRAPHS'])



kounter = 0
for x in range(3):
    kounter = str(kounter)
    page = requests.get("https://www.fangraphs.com/leaders.aspx?pos=all&stats=bat&lg=all&qual=y&type="+kounter+"&season=2018&month=0&season1=2018&ind=0&page=1_500") #'page=1_500' added to end of URL to get entire collection rather than 30/50/90 per page
    soup = BeautifulSoup(page.content,'html.parser')
    kounter = int(kounter)
    kounter+=1

    table = soup.find('div', class_="RadGrid RadGrid_FanGraphs")
    theader = table.find('thead')
    statnamesraw = theader.find_all('th')
    statnameslist = []
    for stat in statnamesraw:
        stat=stat.text.strip()
        statnameslist.append(stat)
    


    tbody = table.find('tbody')
    tablerows = tbody.find_all('tr')
    for row in tablerows:
        values = row.find_all('td')
        nameraw = values[1]
        player = nameraw.text.strip()
        stat_column = 0
        for statname in statnameslist:
            valueraw = values[stat_column]
            value = valueraw.text.strip()
            stat = statnameslist[stat_column]
            addtodict(player, 2018, 'FANGRAPHS', stat, value )
            stat_column+= 1

# test()

#This is just to test and see what stats were pulled
for stat in masterdict['Bryce Harper'][2018]['FANGRAPHS']:
    print(stat, masterdict['Bryce Harper'][2018]['FANGRAPHS'][stat])

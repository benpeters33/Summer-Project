import requests
import pandas as pd
from bs4 import BeautifulSoup


masterdict = {}

def addtodict(player, year, source, statname, value):
    #Updates dict if player is in
    if player in masterdict:
        masterdict[player][year][source][statname] = value
    #Creates new entry into dict if player is not in dict
    else:
        masterdict[player]={year:{source: {stat:value}}}

def test(testplayers = ['Bryce Harper', 'Max Scherzer', 'Sean Doolittle']):
    for player in testplayers:
        print(masterdict[player][2018]['FANGRAPHS'])

#FANGRAPH BATTERS SCRAPER
# Iterates through pages using counter index. RANGE(4) CAN BE CHANGE UP TO 8
page_index = 0
for x in range(4):
    page = requests.get("https://www.fangraphs.com/leaders.aspx?pos=all&stats=bat&lg=all&qual=y&type="+str(page_index)+"&season=2018&month=0&season1=2018&ind=0&page=1_500")
    soup = BeautifulSoup(page.content,'html.parser')
    page_index+=1

#Collects statnames from the headers at the top of every table
    table = soup.find('div', class_="RadGrid RadGrid_FanGraphs")
    theader = table.find('thead')
    statnamesraw = theader.find_all('th')

    statnameslist = []
    for stat in statnamesraw:
        stat=stat.text.strip()
        statnameslist.append(stat)


#Collects the value of every statistic from the table body
    tbody = table.find('tbody')
    tablerows = tbody.find_all('tr')
    for row in tablerows:
        player_row = row.find_all('td')
        nameraw = player_row[1]
        player = nameraw.text.strip()
        stat_column = 0
        for statname in statnameslist:
            valueraw = player_row[stat_column]
            value = valueraw.text.strip()
            stat = statnameslist[stat_column]
            addtodict(player, 2018, 'FANGRAPHS', stat, value)
            stat_column+= 1

#FANGRAPHS PITCHER SCRAPER
page_index = 0
for x in range(4):
    page = requests.get("https://www.fangraphs.com/leaders.aspx?pos=all&stats=pit&lg=all&qual=0&type="+str(page_index)+"&season=2018&month=0&season1=2018&ind=0&team=0&rost=0&age=0&filter=&players=0&page=1_500")
    soup = BeautifulSoup(page.content,'html.parser')
    page_index+=1

#Collects statnames from the headers at the top of every table
    table = soup.find('div', class_="RadGrid RadGrid_FanGraphs")
    theader = table.find('thead')
    statnamesraw = theader.find_all('th')

    statnameslist = []
    for stat in statnamesraw:
        stat=stat.text.strip()
        statnameslist.append(stat)


#Collects the value of every statistic from the table body
    tbody = table.find('tbody')
    tablerows = tbody.find_all('tr')
    for row in tablerows:
        player_row = row.find_all('td')
        nameraw = player_row[1]
        player = nameraw.text.strip()
        stat_column = 0
        for statname in statnameslist:
            valueraw = player_row[stat_column]
            value = valueraw.text.strip()
            stat = statnameslist[stat_column]
            addtodict(player, 2018, 'FANGRAPHS', stat, value)
            stat_column+= 1

test()

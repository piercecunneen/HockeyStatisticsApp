import requests
from bs4 import BeautifulSoup


def GetWOWY():
    url = 'http://stats.hockeyanalysis.com/showplayer.php?pid=951&withagainst=true&season=2014-15&sit=5v5'
    
    response = requests.get(url)
    
    soup = BeautifulSoup(response.content)
    
    data = soup.find_all('table')[2].find_all('tr')
    
    Teammates = data[1:]
    
    Stats = []
    for teammate in Teammates:
        stats = teammate.find_all('td')
        Temp = []
        for stat in stats[:23]:
            if len(stat.text):
                Temp.append(str(stat.text).replace('\n', '').replace('  ', ''))
        Stats.append(Temp)
    return Stats
    






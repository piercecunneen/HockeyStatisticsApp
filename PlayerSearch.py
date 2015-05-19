# Player Search Web Scrapping
import requests
from bs4 import BeautifulSoup
def GetPlayers():
    Players = {}
    response = requests.get('http://stats.hockeyanalysis.com/players.php')
    soup = BeautifulSoup(response.content)
    data = soup.find_all('a')

    for link in data:
        href = link.get('href')
        if 'showplayer' in str(href):
            try:
                Players[str(link.text).replace(',' ,'')] = href
            except:
                # Deals with lone exception
                link = link.text.replace(u'\u2039', '')
                link = link.replace(u'\xc3', '')
                Players[str(link).replace(',' ,'')] = href
    return Players


def PlayerSearch(search, first_or_last_name, Players):
    search = search.lower() # makes search lower case
    
    perfect_matches = {}
    partial_matches = {}
    # if looking at first_name, first_or_last_name will be 1. If last name, it will be 0
    
    # First look for complete matches
    for player in Players:
        name = player.split()[first_or_last_name].lower()
        if search == name:
            perfect_matches[player] = Players[player]
        if search in name:
            partial_matches[player] = Players[player]
            
    if len(perfect_matches):
        return perfect_matches
    elif len(partial_matches):
        return partial_matches
    else:
        return None
    # if no perfect matches, luse any partial matches
    
        

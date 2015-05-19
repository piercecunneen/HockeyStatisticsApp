#scraps team data from stats.hockeyanalysis.com
import requests
from bs4 import BeautifulSoup

#Situation



    

    

def GetPlayerOnIceStats(year, Situation, Team, Position, Minutes, Report):
    url = 'http://stats.hockeyanalysis.com/ratings.php?disp=1&db=' + year + '&sit=' + Situation + '&pos=' + Position + '&minutes=' + Minutes +  '&teamid=' + Team + '&type=' + Report + '&sort=name&sortdir=ASC'
    response = requests.get(url)
    soup = BeautifulSoup(response.content)
    data = soup.find_all('tr')[2:]
    Categories_list = data[0].find_all('th')
    Categories = []
    Order = []
    Stats= []
    for i in data[1:]:
        stats = i.find_all('td')
        Order.append(str(stats[0].text.replace(' ', '')))
        temp = []
        for j in stats[1:20]:
            temp.append(str(j.text.replace(' ', '')))
        Stats.append(temp)
        
    for i in Categories_list[1:20]:
        Categories.append(str(i.text))
    return Stats, Categories

def GetPlayerIndividualStats(year, Situation,  Team, Position, Minutes):
    Report = 'individual'
    url = 'http://stats.hockeyanalysis.com/ratings.php?disp=1&db=' + year+ '&sit=' +Situation+ '&pos='+ Position + '&minutes=' + Minutes +'&teamid=' + Team + '&type=' + Report + '&sort=name&sortdir=ASC'
    response = requests.get(url)
    
    soup = BeautifulSoup(response.content)
    
    Data = soup.find_all('table')[2]
    
    Players = Data.find_all('tr')
    Names = {}
    Team = {}
    GP = {}
    TOI = {}
    G = {}
    A = {}
    FirstA = {}
    Points = {}
    Shots = {}
    iFenwick = {}
    iCorsi = {}
    SHpercent = {}
    G60 = {}
    A60 = {}
    FirstA60 = {}
    Points60= {}
    Shots60 = {}
    iFenwick60 = {}
    iCorsi60 = {}
    Categories = ['Names', 'Team', 'GP', 'TOI','G', 'A', 'FirstA','Points', 'Shots', 'iFenwick', 'iCorsi', 'SH%','G60', 'A60','FirstA60', 'Points60', 'Shots60', 'iFenwick60', 'iCorsi60']

    for player in Players:
        try:
            stats = player.find_all('td')
            Order = int(stats[0].text.replace(' ', ''))
            Names[Order] = str(stats[1].text)
            Team[Order] = str(stats[2].text)
            GP[Order] = int(stats[3].text)
            toi = float(stats[4].text.replace(':', '.'))
            TOI[Order] = toi
            Goals = int(stats[5].text)
            G[Order] = Goals
            Assists = int(stats[6].text)
            A[Order] = Assists
            FirstAssists = int(stats[7].text)
            FirstA[Order] = FirstAssists
            Num_Points = int(stats[8].text)
            Points[Order] = Num_Points
            iShots = int(stats[9].text)
            Shots[Order] = iShots
            individual_Fenwick = int(stats[10].text)
            iFenwick[Order] = individual_Fenwick
            individual_Corsi = int(stats[11].text)
            iCorsi[Order] = individual_Corsi
            individual_SHpercent = float(stats[12].text)
            SHpercent[Order] = individual_SHpercent
            G60[Order] = round(Goals * 60 / toi,2)
            A60[Order] = round(Assists * 60 / toi,2)
            FirstA60[Order] = round(FirstAssists * 60 / toi,2)
            Points60[Order] = round(Num_Points * 60 / toi,2)
            Shots60[Order] = round(iShots * 60 / toi,2)
            iFenwick60[Order] = round(individual_Fenwick * 60 / toi,2)
            iCorsi60[Order] = round(individual_Corsi * 60 / toi,2)
    
    
        except:
            pass
    Stats = [Names, Team, GP, TOI, G, A, FirstA, Points, Shots, iFenwick, iCorsi, SHpercent, G60, A60, FirstA60, Points60, Shots60,iFenwick60, iCorsi60 ]
    
    return Stats, Categories
            
    
    
    
    
    
    
    

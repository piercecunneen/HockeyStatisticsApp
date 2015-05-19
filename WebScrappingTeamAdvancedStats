#scraps team data from stats.hockeyanalysis.com. 
import requests
from bs4 import BeautifulSoup


def GetTeamAdvancedStats(year, situation):
    url = 'http://stats.hockeyanalysis.com/teamstats.php?&disp=1&db=' +  year + '&sit=' + situation + '&sort=team&sortdir=ASC'
    response = requests.get(url)
    soup = BeautifulSoup(response.content)
    
    Data = soup.find_all('table')[2]
    
    Teams = Data.find_all('tr')
    
    Names = {}
    GP = {}
    TOI = {}
    GF = {}
    GA = {}
    GF60 = {}
    GA60 = {}
    GFpercent = {}
    SF = {}
    SA = {}
    SF60 = {}
    SA60 = {}
    SFpercent = {}
    FF = {}
    FA = {}
    FF60 = {}
    FA60 = {}
    FFpercent = {}
    CF = {}
    CA = {}
    CF60 = {}
    CA60 = {}
    CFpercent = {}
    SH_Percentage = {}
    SV_Percentage = {}
    PDO = {}
    Categories = ['Team', 'GP', 'TOI', 'GF','GA', 'GF60', 'GA60', 'GF%',
    'SF','SA', 'SF60', 'SA60', 'SF%','FF','FA', 'FF60', 'FA60', 'FF%',
    'CF','CA', 'CF60', 'CA60', 'CF%','SH%', 'SV%', 'PDO']
    
    
    #Loop popilates above lists with values. In  alphabetical order
    for i in Teams[1:]:
        categories = i.find_all('td')
        Order = int(categories[0].text)
        Names[Order] = str(categories[1].text)
        GP[Order] = int(categories[2].text)
        toi = float(categories[3].text.replace(':', '.'))
        TOI[Order] =(toi)
        GoalsFor = int(categories[4].text)
        GF[Order] =(GoalsFor)
        GoalsAgainst= int(categories[5].text)
        GA[Order] =(GoalsAgainst)   
        GF60[Order] = round((GoalsFor/toi * 60), 2)
        GA60[Order] = round((GoalsAgainst/toi * 60), 2)
        GFpercent[Order] = round(((float(GoalsFor)) / (GoalsFor + GoalsAgainst)* 100),2)
        ShotsFor = int(categories[9].text)
        SF[Order] = (ShotsFor)
        ShotsAgainst = int(categories[10].text)
        SA[Order] = (ShotsAgainst)
        SF60[Order] = round((ShotsFor*60/toi),2)
        SA60[Order] = round((ShotsAgainst*60/toi),2)
        SFpercent[Order] = round((float(ShotsFor)/(ShotsFor + ShotsAgainst)* 100),2)
        
        FenwickFor = int(categories[14].text)
        FF[Order] = (FenwickFor)
        FenwickAgainst = int(categories[15].text)
        FA[Order] = (FenwickAgainst)
        FF60[Order] =round((FenwickFor*60/toi),2)
        FA60[Order] = round((FenwickAgainst*60/toi),2)
        FFpercent[Order] = round((float(FenwickFor)/(FenwickFor + FenwickAgainst)* 100),2)
        
        CorsiFor = int(categories[19].text)
        CF[Order] = (CorsiFor)
        CorsiAgainst = int(categories[20].text)
        CA[Order] = (CorsiAgainst)
        CF60[Order] =round((CorsiFor*60/toi), 2)
        CA60[Order] = round((CorsiAgainst*60/toi), 2)
        CFpercent[Order] =round( (float(CorsiFor)/(CorsiFor + CorsiAgainst) * 100), 2)
        Shooting_Percentage = float(categories[24].text)
        SH_Percentage[Order] = round((Shooting_Percentage),2)
        Save_Percentage = round(float(categories[25].text),2)
        SV_Percentage[Order] = (Save_Percentage)
        PDO[Order] = (Shooting_Percentage + Save_Percentage)
        
    Stats= [Names,GP ,TOI ,GF ,GA ,GF60 ,GA60 ,GFpercent ,SF ,SA ,
    SF60 ,SA60 ,SFpercent ,FF ,FA ,FF60 ,FA60 ,FFpercent ,CF ,CA ,
    CF60 ,CA60 ,CFpercent ,SH_Percentage ,SV_Percentage ,PDO ]
    return Stats, Categories

Stats, Categories = GetTeamAdvancedStats('201415', '5v5')






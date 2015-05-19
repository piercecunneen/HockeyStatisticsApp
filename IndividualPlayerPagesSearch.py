# Individual Player pages
import requests
from bs4 import BeautifulSoup
import time

def GetPlayerStats(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content)
    tables = soup.find_all('table')[2:]
    
    
    
    
    # Get Stat Categories
    On_ice_Goal_categories = []
    On_ice_Fenwick_categories = []
    
    Individual_categories = []
    
    Individual= tables[0].find_all('tr')
    On_Ice1 = tables[1].find_all('tr')
    On_Ice2 = tables[2].find_all('tr')
    
    Individual_Category = Individual[0]
    On_Ice1_Category= On_Ice1[0]
    On_Ice2_Category= On_Ice2[0]
    for j,k in zip(On_Ice1_Category,On_Ice2_Category):
        On_ice_Goal_categories.append(str(j.text))
        On_ice_Fenwick_categories.append(str(k.text))
    for i in Individual_Category:
           Individual_categories.append(str(i.text ))


    
    
    # Get Stats
    Individual_stats_5v5 = []
    On_ice_Goal_stats = []
    On_ice_Fenwick_stats = []
    
    
    Indi_5v5_Table = Individual[1:]
    On_Ice1_Table = On_Ice1[1:]
    On_Ice2_Table = On_Ice2[1:]
    
    
    for j,k in zip(On_Ice1_Table,On_Ice2_Table):
        On_ice_Goal_stats.append(str(j.text).replace('\n', '').split())
        On_ice_Fenwick_stats.append(str(k.text).replace('\n', '').split())
    for i in Indi_5v5_Table:
        Individual_stats_5v5.append(str(i.text).replace('\n', '').split())
    return Individual_categories,  On_ice_Goal_categories,  On_ice_Fenwick_categories, Individual_stats_5v5, On_ice_Goal_stats, On_ice_Fenwick_stats
    
        
        


def TeamSearch(search):
    # Takes in a search query and returns either an exact match or a list of partial matches
    TeamNames = {'Anaheim Ducks': 1, 'Arizona Coyotes':23, 'Boston Bruins':3, 
            'Buffalo Sabres': 4, 'Carolina Hurricanes':5, 'Calgary Flames':6, 'Chicago Blackhawks':7,
            'Colorodo Avalanche':9, 'Columbus Blue jackets':8, 'Dallas Stats':10, 'Detroit Redwings':11, 
            'Edmonton Oilers':12, 'Florida Panthers':13, 'Los Angeles Kings':14,  'Minnesota Stars':15, 
            'Montreal Canadiens':16, 'Nashville Predators':17, 'New Jersey Devils':18, 'New York Islanders':19, 
            'New York Rangers':20, 'Ottawa Senators':21, 'Philadelphia Flyers':22, 'Pittsburgh Penguins':24, 'San Jose Sharks':25, 
            'St. Louis Blues':26, 'Tampa Bay Lightening':27, 'Toronto Redwings':28, 'Vancouver Canucks':29, 'Washington Capitals':30, 'Winnipeg Jets':2}
    
    Partial_Matches = {}
    Exact_Matches = {}
    search = search.lower()
    
    # 
    for team in TeamNames:
        if team.lower() == search:
            Exact_Matches[team] = TeamNames[team]
            return Exact_Matches
        name = team.lower()
        search_list = search.split()
        for query in search_list:
            if query in name:
                if query != 'new' or len(search_list) == 1:  
                    Partial_Matches[team] = TeamNames[team]
                    break
    
    if len(Partial_Matches) >0:
        return Partial_Matches
    else:
        return None
def GetTeams():
    TeamNames = {'Anaheim Ducks': 1, 'Arizona Coyotes':23, 'Boston Bruins':3,
    'Buffalo Sabres': 4, 'Carolina Hurricanes':5, 'Calgary Flames':6, 'Chicago Blackhawks':7,
    'Colorodo Avalanche':9, 'Columbus Blue jackets':8, 'Dallas Stats':10, 'Detroit Redwings':11,
    'Edmonton Oilers':12, 'Florida Panthers':13, 'Los Angeles Kings':14,  'Minnesota Stars':15,
    'Montreal Canadiens':16, 'Nashville Predators':17, 'New Jersey Devils':18, 'New York Islanders':19,
    'New York Rangers':20, 'Ottawa Senators':21, 'Philadelphia Flyers':22, 'Pittsburgh Penguins':24, 'San Jose Sharks':25,
    'St. Louis Blues':26, 'Tampa Bay Lightening':27, 'Toronto Redwings':28, 'Vancouver Canucks':29, 'Washington Capitals':30, 'Winnipeg Jets':2}
    return TeamNames


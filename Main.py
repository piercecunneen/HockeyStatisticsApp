
import kivy
from kivy.uix.gridlayout import GridLayout
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
from kivy.uix.floatlayout  import FloatLayout
from kivy.uix.dropdown import DropDown
from kivy.uix.label import Label
from kivy.uix.image import Image 
from kivy.core.window import Window
import webbrowser

from WebScrappingTeamAdvancedStats import GetTeamAdvancedStats
from WebScrappingPlayerIndividualAdvancedStats import GetPlayerIndividualStats, GetPlayerOnIceStats
from PlayerSearch import GetPlayers, PlayerSearch
from IndividualPlayerPagesSearch import GetPlayerStats
from TeamSearch import TeamSearch, GetTeams

PlayerData = GetPlayers()
Teams = GetTeams()


seasons = {'2014-2015': '201415', '2013-2014':'201314', '2012-2013':'201213', '2011-2012': '201112', '2010-2011':'201011', '2009-2010':'200910', '2008-2009':'200809', '2007-2008':'200708',  '2013-2015':'201315', '2012-2014':'201214', '2011-2013':'201113', '2010-2012':'201012', '2009-2011':'200911', '2008-2010':'200810', '2007-2009':'200709'}
ordered_seasons= ['2014-2015', '2013-2014', '2012-2013', '2011-2012', '2010-2011', '2009-2010', '2008-2009', '2007-2008', '2013-2015', '2012-2014', '2011-2013', '2010-2012', '2009-2011', '2008-2010', '2007-2009']
situations = {'5v5':'5v5', '5v4':'5v4', '4v5': '4v5', '5v5 close':'5v5close','5v5 leading':'5v5leading','5v5 trailing':'5v5trailing', 'All situations':'all'}
ordered_situations = ['5v5', '5v4', '4v5', '5v5 close', '5v5 leading', '5v5 trailing', 'All situations']



class HockeyApp(App):
    def build(self):
        parent1 = FloatLayout()
        parent = FloatLayout()
        BackgroundImage = Image(source = 'background_ice.jpg', size_hint= (1, 1), pos_hint={'x':0 , 'center_y' : .5}, allow_stretch = True, keep_ratio = False)
        # Beginning of Team Stats Section
        def GoToTeamStats(obj):
            parent1.clear_widgets()
            parent1.add_widget(BackgroundImage)
            Layout = GridLayout(cols = 26, rows = 31, size_hint = (None, None))
            Layout.bind(minimum_height=Layout.setter('height'), minimum_width = Layout.setter('width'))
            # Button Functions
            def GetStats(obj):
                # Updates the Grid Layout with the new categories
                SortBy = 0
                
            
                
                do_update = True
                if b3.text == 'Situation' and b2.text != 'Season':
                    Stats, Categories = GetTeamAdvancedStats(seasons[b2.text],'5v5')

                    b3.text = '5v5'
                    Layout.clear_widgets()
                elif b3.text == 'Situation' and b2.text == 'Season':
                    do_update = False
                elif b3.text != 'Situation' and b2.text == 'Season':
                    Stats,Categories = GetTeamAdvancedStats('201415', situations[b3.text])
                    b2.text = '2014-15'
                    Layout.clear_widgets()
                    
                else:
                    Stats,Categories = GetTeamAdvancedStats(seasons[b2.text], situations[b3.text])
                    Layout.clear_widgets()
                
                
                if do_update:
                    for category in Categories:
                        Layout.add_widget(TextInput(text= str(category), size_hint = (None, None), font_size = 20, background_color = [1, 1, 1, 1]))
                    for id_num in range(1, 31):
                        if id_num % 2 != 0:
                            ColorBackGround = [200./255, 204./255, 255./255, 1]
                        else:
                            ColorBackGround = [1,1,1,1]
                        for stat in Stats:
                            Layout.add_widget(TextInput(text= str(stat[id_num]), size_hint = (None, None), font_size = 16, background_color = ColorBackGround))

                # Allows for drop down menus to be accessed again after Layout has been updates
                b2.bind(on_release=dropdown1.open)
                b3.bind(on_release=dropdown2.open)
            def on_double_tap():
                SortBy = Stats.index(TextInput.selection_text)
                print 'fds'
                print SortBy
            
            def BackToMenu(obj):
                parent1.clear_widgets()
                Layout.clear_widgets()
                parent1.add_widget(BackgroundImage)

                parent1.add_widget(TeamButton)
                parent1.add_widget(PlayerStatsButton)
                parent1.add_widget(Title)
                parent1.add_widget(Citations)
                parent1.add_widget(Author)

            
            # Drop Down for b2 (Season Button)
            dropdown1 = DropDownCreation(ordered_seasons)
            b2 = Button(text = 'Season',pos_hint={'x': .25, 'center_y': .95}, size_hint=(.25, .1))
            b2.bind(on_release=dropdown1.open)
            dropdown1.bind(on_select=lambda instance, x: setattr(b2, 'text', x))

             # Drop down for b3 (situation button)
            dropdown2 = DropDownCreation(ordered_situations)
            b3 = Button(text = 'Situation',pos_hint={'x': .5, 'center_y': .95}, size_hint=(.25, .1))
            b3.bind(on_release=dropdown2.open)
                        
            dropdown2.bind(on_select=lambda instance, x: setattr(b3, 'text', x))
            
            
            b1 = Button(text = 'Back to Menu', pos_hint={'x': 0, 'center_y': .95}, size_hint=(.25, .1))
            b4 = Button(text = 'Get Stats', pos_hint={'x': .75, 'center_y': .95},size_hint = (.25, .1))
            
            b1.bind(on_release = BackToMenu)
            b4.bind(on_release = GetStats)
            
            
            root = ScrollView(size_hint = (1, .8))
            
            # Add Buttons and Layout to Float Layout
            root.add_widget(Layout)
            parent.add_widget(root)
            parent.add_widget(b1)
            parent.add_widget(b2)
            parent.add_widget(b3)
            parent.add_widget(b4)
            parent1.add_widget(parent)
    
    # End of Team Stats Page
    
    
    
    
    # Start of Player Stats Page
    
        def GoToPlayerStats(obj):
            parent1.clear_widgets()
            parent1.add_widget(BackgroundImage)
            Layout = FloatLayout(anchor_x = 'left',  size_hint = (1,1))
            SearchResults = Button(text = 'Results',pos_hint={'center_x': .5, 'center_y': .45}, size_hint=(.25, .05))
            
            
        
            
            def LastNamePlayerSearch(obj):
                search = TeamNameText.text
                Matches = PlayerSearch(search, 0, PlayerData)
                if Matches != None:
                    dropdown =DropDownCreation(Matches)
                    dropdown.open(SearchResults)
                    SearchResults.bind(on_release=dropdown.open)
                    dropdown.bind(on_select=lambda instance, x: setattr(SearchResults, 'text', x))
                    dropdown.bind(on_dismiss = DisplayPlayerData)
                else:
                    TeamNameText.text = 'No Results, Please try again'
            def FirstNameSearch(obj):
                search = TeamNameText.text
                Matches = PlayerSearch(search, 1, PlayerData)
                if Matches != None:
                    dropdown = DropDownCreation(Matches)
                    SearchResults.bind(on_release=dropdown.open)
                    dropdown.open(SearchResults)
                    dropdown.bind(on_dismiss = DisplayPlayerData)
                    dropdown.bind(on_select=lambda instance, x: setattr(SearchResults, 'text', x))
                else:
                    TeamNameText.text = 'No Results, Please try again'
            def TeamNameSearch(obj):
                search = TeamNameText.text
                Matches = TeamSearch(search)
                if Matches != None:
                    dropdown = DropDownCreation(Matches)
                    SearchResults.bind(on_release=dropdown.open)
                    dropdown.open(SearchResults)
                    dropdown.bind(on_dismiss = DisplayPlayerData)
                    dropdown.bind(on_select=lambda instance, x: setattr(SearchResults, 'text', x))
                else:
                    TeamNameText.text = 'No Results, Please try again'
            def DisplayPlayerData(obj):
                def IndividualStats(obj):
                
                    # Clear widgets in order to hide previous table if user searched for other play stat categories first
                    Layout.clear_widgets()
                    Layout.add_widget(BackToPlayerSearch)
                    Layout.add_widget(IndividualButton)
                    Layout.add_widget(On_Ice_Goals_Button)
                    Layout.add_widget(On_Ice_Fenwick_Button)
                    Layout.add_widget(PlayerSearchLabel)

                    Grid = GridLayout(rows = len(Individual_stats_5v5) + 1, cols = len(Individual_categories), size_hint = (None, None))
                    Grid.bind(minimum_height=Grid.setter('height'), minimum_width = Grid.setter('width'))
                    for stat_category in Individual_categories:
                        Grid.add_widget(TextInput(text = str(stat_category), size_hint = (None, None), font_size = 18))
                    for i in range(len(Individual_stats_5v5)):
                        if i % 2 == 0:
                            ColorBackGround = [200./255, 204./255, 255./255, 1]
                        else:
                            ColorBackGround = [1,1,1,1]
                        season = Individual_stats_5v5[i]
                        for stat in season:
                            Grid.add_widget(TextInput(text = str(stat), size_hint = (None, None), font_size = 18, background_color = ColorBackGround))
                    Scroll = ScrollView(size_hint = (1, .65))

                    Scroll.add_widget(Grid)
                    Layout.add_widget(Scroll)
                def OnIceGoalsStats(obj):
                    # Clear widgets in order to hide previous table if user searched for other play stat categories first
                    Layout.clear_widgets()
                    Layout.add_widget(PlayerSearchLabel)
                    Layout.add_widget(BackToPlayerSearch)
                    Layout.add_widget(IndividualButton)
                    Layout.add_widget(On_Ice_Goals_Button)
                    Layout.add_widget(On_Ice_Fenwick_Button)
                    Grid = GridLayout(rows = len(On_ice_Goal_stats) + 1, cols = len(On_ice_Goal_categories), size_hint = (None, None))
                    Grid.bind(minimum_height=Grid.setter('height'), minimum_width = Grid.setter('width'))
                    for stat_category in On_ice_Goal_categories:
                        Grid.add_widget(TextInput(text = str(stat_category), size_hint = (None, None), font_size = 18))
                    for i in range(len(On_ice_Goal_stats)):
                        if i % 2 == 0:
                            ColorBackGround = [200./255, 204./255, 255./255, 1]
                        else:
                            ColorBackGround = [1,1,1,1]
                        season = On_ice_Goal_stats[i]
                        for stat in season:
                            Grid.add_widget(TextInput(text = str(stat), size_hint = (None, None), font_size = 18, background_color = ColorBackGround))
                    Scroll = ScrollView(size_hint = (1, .65))
                    Scroll.add_widget(Grid)
                    Layout.add_widget(Scroll)
                def OnIceFenwickStats(obj):
                
                    # Clear widgets in order to hide previous table if user searched for other play stat categories first
                    Layout.clear_widgets()
                    Layout.add_widget(BackToPlayerSearch)
                    Layout.add_widget(PlayerSearchLabel)
                    Layout.add_widget(IndividualButton)
                    Layout.add_widget(On_Ice_Goals_Button)
                    Layout.add_widget(On_Ice_Fenwick_Button)

                    Grid = GridLayout(rows = len(On_ice_Fenwick_stats) + 1, cols = len(On_ice_Fenwick_categories), size_hint = (None, None))
                    Grid.bind(minimum_height=Grid.setter('height'), minimum_width = Grid.setter('width'))
                    for stat_category in On_ice_Fenwick_categories:
                        Grid.add_widget(TextInput(text = str(stat_category), size_hint = (None, None), font_size = 18))
                    for i in range(len(On_ice_Fenwick_stats)):
                        if i % 2 == 0:
                            ColorBackGround = [200./255, 204./255, 255./255, 1]
                        else:
                            ColorBackGround = [1,1,1,1]
                        season = On_ice_Fenwick_stats[i]
                        for stat in season:
                            Grid.add_widget(TextInput(text = str(stat), size_hint = (None, None), font_size = 18, background_color = ColorBackGround))
                    Scroll = ScrollView(size_hint = (1, .65))
                    
                    Scroll.add_widget(Grid)
                    Layout.add_widget(Scroll)
                def BackToSearch(obj):
                    parent1.remove_widget(Layout)
                    GoToPlayerStats(obj)
                
                if SearchResults.text in Teams:
                    # Searching by Team
                    Positions = {'All Skaters':'skaters', 'Forwards':'forwards', 'Defensemen':'defense', 'Goalies':'goalies'}
                    ordered_positions = ['All Skaters', 'Forwards', 'Defensemen', 'Goalies']
                    minutes = ['50', '100', '200', '300', '400', '500', '750', '1000', '1250', '1500', '2000']
                    StatReports = ['Individual', 'Goals', 'Shots', 'Fenwick', 'Corsi']
                    
                    
                    Layout.clear_widgets()
                    Layout.add_widget(PlayerSearchLabel)
                    
                    def TeamSearchDisplayPlayerData(obj):
                        
                        Layout.clear_widgets()
                        Layout.add_widget(PlayerSearchLabel)
                        Layout.add_widget(SelectMinutes)
                        Layout.add_widget(SelectSituation)
                        Layout.add_widget(SelectSeason)
                        Layout.add_widget(GetStatsButton)
                        Layout.add_widget(SelectPosition)
                        Layout.add_widget(BackToPlayerSearch)
                        Layout.add_widget(SelectStatsReport)

                        if SelectPosition.text == 'Position':
                            SelectPosition.text = ordered_positions[0]
                        if SelectSeason.text == 'Season':
                            SelectSeason.text = ordered_seasons[0]
                        if SelectSituation.text == 'Situation':
                            SelectSituation.text = ordered_situations[0]
                        if SelectMinutes.text == 'Minutes':
                            SelectMinutes.text = minutes[0]
                        if SelectStatsReport.text == 'Report Options':
                            SelectStatsReport.text = 'Individual'
                        
                        
                        if SelectStatsReport.text == 'Individual':
                            Stats, Categories = GetPlayerIndividualStats(seasons[SelectSeason.text],situations[SelectSituation.text] , str(Teams[SearchResults.text]), Positions[SelectPosition.text], SelectMinutes.text)
                            print Stats[5]
                            print Sort(Stats[5])
                            Grid = GridLayout(rows = len(Stats[0]) + 1, cols = len(Stats), size_hint = (None, None))
                        
                            Grid.bind(minimum_height=Grid.setter('height'), minimum_width = Grid.setter('width'))
                        
                            for stat_category in Categories:
                                Grid.add_widget(TextInput(text = stat_category, size_hint = (None, None), font_size = 18))
                            for i in range(1, len(Stats[0]) + 1):
                                if i % 2 != 0:
                                    ColorBackGround = [200./255, 204./255, 255./255, 1]
                                else:
                                    ColorBackGround = [1,1,1,1]
                            
                                for stat in Stats:
                                    Grid.add_widget(TextInput(text = str(stat[i]), size_hint = (None, None), font_size = 18, background_color = ColorBackGround))
                        else:
                            Stats, Categories = GetPlayerOnIceStats(seasons[SelectSeason.text],situations[SelectSituation.text] , str(Teams[SearchResults.text]), Positions[SelectPosition.text], SelectMinutes.text, SelectStatsReport.text.lower())
                            Grid = GridLayout(rows = len(Stats) + 1, cols = len(Categories), size_hint = (None, None), spacing = [.1, .1])
                            
                            Grid.bind(minimum_height=Grid.setter('height'), minimum_width = Grid.setter('width'))
                            
                            for stat_category in Categories:
                                Grid.add_widget(TextInput(text = stat_category, size_hint = (None, None), font_size = 18))
                            for i in range(1, len(Stats) + 1):
                                if i % 2 != 0:
                                    ColorBackGround = [200./255, 204./255, 255./255, 1]
                                else:
                                    ColorBackGround = [1,1,1,1]
                                
                                for player in Stats[i-1]:
                                    Grid.add_widget(TextInput(text = player, size_hint = (None, None), font_size = 18, background_color = ColorBackGround))
                            
                        # re bind drop down menus
                        SelectPosition.bind(on_release = position_dropdown.open)
                        SelectSeason.bind(on_release = Season_dropdown.open)
                        SelectSituation.bind(on_release = Situation_dropdown.open)
                        SelectMinutes.bind(on_release = Minutes_dropdown.open)
                        SelectStatsReport.bind(on_release = StatsReport_dropdown.open)
                    
                        Scroll = ScrollView(size_hint = (1, .65))
                        Scroll.add_widget(Grid)
                        Layout.add_widget(Scroll)
                        

                    BackToPlayerSearch = Button(text='Back to Player Search', size_hint = (.5, .1), pos_hint = {'x':.0, 'center_y':.95})
                    
                    GetStatsButton = Button(text='Get Stats', size_hint = (.5, .1), pos_hint = {'x':.5, 'center_y':.95})
                    GetStatsButton.bind(on_release = TeamSearchDisplayPlayerData)
                    
                    
                    #####  Select Position Button and Drop down for select position
                    SelectPosition = Button(text = 'Position', size_hint = (.2, .1), pos_hint = {'x':.4, 'center_y':.85} , background_color = [1,0,0,1])
                    position_dropdown = DropDownCreation(ordered_positions)
                    SelectPosition.bind(on_release=position_dropdown.open)
                    position_dropdown.bind(on_select=lambda instance, x: setattr(SelectPosition, 'text', x))
                    
                    
                    #### Select Season Button and drop down
                    SelectSeason = Button(text = 'Season', size_hint = (.2, .1), pos_hint = {'x':.2, 'center_y':.85} , background_color = [1,0,0,1])
                    Season_dropdown = DropDownCreation(ordered_seasons)
                    SelectSeason.bind(on_release=Season_dropdown.open)
                    Season_dropdown.bind(on_select=lambda instance, x: setattr(SelectSeason, 'text', x))
                    
                    
                    #### Select Situation Button and drop down
                    
                    SelectSituation = Button(text = 'Situation', size_hint = (.2, .1), pos_hint = {'x':.0, 'center_y':.85}, background_color = [1,0,0,1] )
                    Situation_dropdown = DropDownCreation(ordered_situations)
                    SelectSituation.bind(on_release=Situation_dropdown.open)
                    Situation_dropdown.bind(on_select=lambda instance, x: setattr(SelectSituation, 'text',  x))


                    #### Select Minutes Button and drop down
                    SelectMinutes = Button(text = 'Minutes', size_hint = (.2, .1), pos_hint = {'x':.8, 'center_y':.85}, background_color = [1,0,0,1])
                    Minutes_dropdown = DropDownCreation(minutes)
                    SelectMinutes.bind(on_release=Minutes_dropdown.open)
                    Minutes_dropdown.bind(on_select = lambda instance, x: setattr(SelectMinutes, 'text', x))

                    #### Select Stats Report and drop down
                    SelectStatsReport = Button(text = 'Report Options', size_hint = (.2, .1), pos_hint = {'x':.6, 'center_y':.85}, background_color = [1,0,0,1])
                    StatsReport_dropdown = DropDownCreation(StatReports)
                    SelectStatsReport.bind(on_release = StatsReport_dropdown.open)
                    StatsReport_dropdown.bind(on_select = lambda instace, x: setattr(SelectStatsReport, 'text', x))
                
                    
                    

                    BackToPlayerSearch.bind(on_release = BackToSearch)
                    Layout.add_widget(SelectStatsReport)
                    Layout.add_widget(SelectMinutes)
                    Layout.add_widget(SelectSituation)
                    Layout.add_widget(SelectSeason)
                    Layout.add_widget(GetStatsButton)
                    Layout.add_widget(SelectPosition)
                    Layout.add_widget(BackToPlayerSearch)
                elif SearchResults.text != 'Results':
                    # Searching by First or Last name
                    url = 'http://stats.hockeyanalysis.com/' + PlayerData[SearchResults.text]
                    Individual_categories,  On_ice_Goal_categories,  On_ice_Fenwick_categories, Individual_stats_5v5, On_ice_Goal_stats, On_ice_Fenwick_stats = GetPlayerStats(url)
                    Layout.clear_widgets()
                    Layout.add_widget(PlayerSearchLabel)
                    
                    IndividualButton = Button(text='Individual Stats 5v5', size_hint= (.25, .1), pos_hint = {'x':0, 'center_y':.95})
                    On_Ice_Goals_Button = Button(text='On Ice Goals Stats 5v5', size_hint= (.25, .1), pos_hint = {'x':.25, 'center_y':.95})
                    On_Ice_Fenwick_Button = Button(text='On Ice Fenwick Stats 5v5', size_hint= (.25, .1), pos_hint = {'x':.5, 'center_y':.95})
            
                    BackToPlayerSearch = Button(text='Back to Player Search', size_hint = (.25, .1), pos_hint = {'x':.75, 'center_y':.95})
                    BackToPlayerSearch.bind(on_release = BackToSearch)
                    IndividualButton.bind(on_release = IndividualStats)
                    On_Ice_Goals_Button.bind(on_release = OnIceGoalsStats)
                    On_Ice_Fenwick_Button.bind(on_release = OnIceFenwickStats)
                    Layout.add_widget(BackToPlayerSearch)
                    Layout.add_widget(IndividualButton)
                    Layout.add_widget(On_Ice_Goals_Button)
                    Layout.add_widget(On_Ice_Fenwick_Button)

    
            def Menu(obj):
                # Send back to Main Menu by removing Layout widget
                parent1.remove_widget(Layout)
                parent1.add_widget(TeamButton)
                parent1.add_widget(PlayerStatsButton)
                parent1.add_widget(Title)
                parent1.add_widget(Citations)
                parent1.add_widget(Author)



            
            
            # Create TextInput and Button Widgets
            
            # LastNameText = TextInput(text ='Seach Last Name here (delete this text first) ', size_hint = (.25, .1), pos_hint = {'x':.25, 'y': 0})
            # FirstNameText = TextInput(text ='Seach first Name here (delete this text first)  ', size_hint = (.25, .1), pos_hint = {'x':.25, 'y': .25})
            TeamNameText = TextInput(text ='Seach here, and then hit a search option above ', size_hint = (.35, .095), pos_hint = {'x':.325, 'y': .5})
        
            LastNameSearchButton = Button(text ='Search by Last Name', size_hint=(.25, .1), pos_hint = {'x' :.25, 'center_y':.95})
            FirstNameSearchButton = Button(text ='Search by First Name', size_hint=(.25, .1), pos_hint = {'x' :.5, 'center_y':.95})
            TeamSearchButton = Button(text ='Search by Team ', size_hint=(.25, .1), pos_hint = {'x' :.75, 'center_y':.95})
            PlayerSearchLabel = Label(text = 'Player Search', size_hint= (1, .2), pos_hint={'x':0 , 'center_y' : .74}, font_size = 140, color = [0,0,0,1])
            
            # Bind buttons to their respective functions
            LastNameSearchButton.bind(on_release = LastNamePlayerSearch)
            FirstNameSearchButton.bind(on_release = FirstNameSearch)
            TeamSearchButton.bind(on_release = TeamNameSearch)
            
            Menu_Button = Button(text = 'Back to menu', size_hint=(.25, .1), pos_hint = {'x' :0, 'center_y':.95})
            Menu_Button.bind(on_release=Menu)
            
            # Add Buttons, Images TextInputs to Layout
#            Layout.add_widget(LastNameText)
#            Layout.add_widget(FirstNameText)
            Layout.add_widget(TeamNameText)
            Layout.add_widget(LastNameSearchButton)
            Layout.add_widget(FirstNameSearchButton)
            Layout.add_widget(TeamSearchButton)
            Layout.add_widget(Menu_Button)
            Layout.add_widget(PlayerSearchLabel)
            Layout.add_widget(SearchResults)
            parent1.add_widget(Layout)



        def GoToSite(self, obj):
            webbrowser.open('http://stats.hockeyanalysis.com/index.php')
        
        
        TeamButton = Button(text = 'Get Team Stats', pos_hint={'x': .3, 'center_y': .4}, size_hint=(.15, .1))
        PlayerStatsButton = Button(text = 'Get Player Stats', pos_hint={'x': .55, 'center_y': .4}, size_hint=(.15, .1) )
        
        Title = Label(text = 'Advanced Hockey Statistics', pos_hint = {'x':0, 'center_y':.85}, font_size = 100, color = [0,0,0,1], size_hint = (1, .2))
        
        Citations = Label(text = 'Data courtesy of David Johnson via [ref=]stats.hockeyanalysis.com[/ref]',pos_hint = {'center_x':.5, 'center_y':.2}, font_size = 50, color = [0,0,0,1], size_hint = (1, .2)  , markup = True)

        Author = Label(text = 'Developed by Pierce Cunneen',pos_hint = {'center_x':.5, 'center_y':.1}, font_size = 30, color = [0,0,0,1], size_hint = (1, .2))
        
        Citations.bind(on_ref_press = GoToSite)
        TeamButton.bind(on_release=GoToTeamStats)
        PlayerStatsButton.bind(on_release = GoToPlayerStats)
        

        
        parent1.add_widget(BackgroundImage)
        parent1.add_widget(Citations)
        parent1.add_widget(Author)
        parent1.add_widget(Title)
        parent1.add_widget(TeamButton)
        parent1.add_widget(PlayerStatsButton)
        return parent1
    
    
def DropDownCreation(data):
    Dropdown = DropDown()
    for i in data:
        drop_option = Button(text = i, size_hint_y = None, height = 40)
        drop_option.bind(on_release = lambda drop_option: Dropdown.select(drop_option.text))
        Dropdown.add_widget(drop_option)
    return Dropdown



def Sort(data):
    # Uses built in python method sorted (time sort algorithm O(nlogn)) to sort a dictionary by keys
    return sorted(data, key=data.get)


if __name__ == '__main__':
    HockeyApp().run()



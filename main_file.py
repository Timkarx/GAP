from openpyxl import Workbook
from gap_ratings.data_load.extraction_funcs import *
from gap_ratings.gap_calc import *


#Load and extract data
teams_list , matches_list = extract_league_data('D',load_leagues('Prem',
                                                                 10,21))


#Create a list of teams where each member is a Teams class instance
all_teams = []
for season in teams_list:
    for each_team in season:
        all_teams.append(each_team)

all_teams = sorted(set(all_teams))
teams = []
for each_team in all_teams:
    teams.append(Teams(each_team))


#Load up the initial gap_ratings


#Simulate the GAP inputs
kick_off(matches_list, teams,0,1,2,3,4)


#Save and export the data to an excel spreadsheet
filename = 'gap_data.xlsx'
gap_data = Workbook() 
gap_data.save(filename=filename)

for team in teams:
    team_sheet = gap_data.create_sheet(team.name)
    for match in team.performance:
        team_sheet.append(match)

gap_data.save(filename=filename)

from openpyxl import load_workbook

from extraction_funcs import *
from TeamsClass import Teams

#Load the spreadsheet containing the raw match data
match_sheet = load_workbook(filename="sample_prem.xlsx").active

#Extract all the data in the form of lists
teams_sorted = team_list(match_sheet,"D")
matches_played = match_list(match_sheet,2,7)

#Create a list of teams where each member is a Teams class object
teams = []
for each_team in teams_sorted:
    team = Teams(each_team,0)
    teams.append(team)

#Iterate through every match and update each object in Teams with
#their correct match_outcome and goals scored dutring that match
for each_match in matches_played:
    home_team = each_match[2]
    away_team = each_match[3]
    home_goals = each_match[4]
    away_goals = each_match[5]

    for team in teams:
        if team.name == home_team:
            team.played_home_match(home_goals,away_goals)
        elif team.name == away_team:
            team.played_away_match(away_goals,home_goals)

from extraction_funcs import *
from Teams import Teams

#Load the spreadsheet containing the raw match data
season_sheet = load_sheet('epl_1516.xlsx')

#Extract all the data in the form of lists
teams_sorted = team_list(season_sheet,"D")
matches_played = match_list(season_sheet,3,6)

#Create a list of teams where each member is a Teams class object
teams = []
for each_team in teams_sorted:
    team = Teams(each_team)
    teams.append(team)

#Iterate through every match and update each object in Teams with
#their correct match_outcome and goals scored dutring that match
for each_match in matches_played:
    home_team = each_match[0]
    away_team = each_match[1]
    home_goals = each_match[2]
    away_goals = each_match[3]

    for team in teams:
        if team.name == home_team:
            team.played_home_match(home_goals,away_goals)
        elif team.name == away_team:
            team.played_away_match(away_goals,home_goals)

#Calculate the initial gap ratings and update each teams gap rating
initial_gap_ratings = []
for team in teams:
    average_scored = team.total_scored/team.total_played
    initial_gap_team = [team.name,average_scored]
    initial_gap_ratings.append(initial_gap_team)
    team.gap_rat.append(average_scored)


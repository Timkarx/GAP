from gap_ratings.extraction_funcs import *
from gap_ratings.TeamsClass import Teams

season_list = load_league('Prem',16,20)


#Extract all the match data for all the seasons in the form of lists
teams_list , matches_list = extract_league_data('D',season_list)
    

#Create a list of teams where each member is a Teams class object
all_teams = []
for season in teams_list:
    for each_team in season:
        all_teams.append(each_team)

unique = sorted(set(all_teams))
unique_teams = []
for each_team in unique:
    team_obj = Teams(each_team)
    unique_teams.append(team_obj)




#Iterate through every match and update each object in Teams with
#their correct match_outcome and goals scored dutring that match
for each_season in matches_list:
    for each_match in each_season:
        date = each_match[0]
        home_team = each_match[1]
        away_team = each_match[2]
        home_goals = each_match[3]
        away_goals = each_match[4]

        for team in unique_teams:
            if team.name == home_team:
                team.played_home_match(date,home_goals,away_goals)
            elif team.name == away_team:
                team.played_away_match(date,away_goals,home_goals)

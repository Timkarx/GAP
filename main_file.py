from gap_ratings.extraction_funcs import *
from gap_ratings.TeamsClass import Teams


#Load and extract data
season_list = load_league('Prem',16,21)
teams_list , matches_list = extract_league_data('D',season_list)
    

#Create a list of teams where each member is a Teams class object
all_teams = []
for season in teams_list:
    for each_team in season:
        all_teams.append(each_team)

all_teams = sorted(set(all_teams))
teams = []
for each_team in all_teams:
    teams.append(Teams(each_team))


#Iterate through every match and update each object in Teams with
#their correct match_outcome and goals scored dutring that match
for each_season in matches_list:
    for each_match in each_season:
        date = each_match[0]
        home_team = each_match[1]
        away_team = each_match[2]
        home_goals = each_match[3]
        away_goals = each_match[4]

        for team in teams:
            if team.name == home_team:
                team.played_home_match(date,home_goals,away_goals)
                home = team
            elif team.name == away_team:
                team.played_away_match(date,away_goals,home_goals)
                away = team

        ht_new_HA, ht_new_HD = Teams.calc_home_gap_rat(home, away,
                                                       home_goals,away_goals)
        at_new_AA, at_new_AD = Teams.calc_away_gap_rat(home, away,
                                                       home_goals, away_goals)

        Teams.update_gap_rat(home, away, ht_new_HA, ht_new_HD,
                             at_new_AA, at_new_AD)

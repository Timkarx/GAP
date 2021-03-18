from gap_ratings.team_data.TeamsClass import Teams

def kick_off(list_of_matches, list_of_teams, date_idx, home_team_idx, away_team_idx,
             home_gs_idx, away_gs_idx, home_gap_idx=None, away_gap_idx=None ):

#This function runs through all the loaded matches and updates
#the gap ratings of each team after every match
#Note1: The elements of list_of_matches are lists of games per season
#Note1: (i.e. the first element is a list of all games in season 1, etc.)
#Note2: The list_of_teams variable must be a list of Teams class objects


    for each_season in list_of_matches:
        for each_match in each_season:
            date = each_match[date_idx]
            home_team = each_match[home_team_idx]
            away_team = each_match[away_team_idx]
            home_goals = each_match[home_gs_idx]
            away_goals = each_match[away_gs_idx]
            if home_team_idx is int:
                home_gap = each_match[home_gap_idx]
                away_gap = each_match[away_gap_idx]

            for team in list_of_teams:
                if team.name == home_team:
                    team.played_home_match(date,home_goals,away_goals)
                    home = team
                elif team.name == away_team:
                    team.played_away_match(date,away_goals,home_goals)
                    away = team

            ht_new_HA, ht_new_HD,ht_new_AA, ht_new_AD = Teams.calc_home_gap_rat(home,away,
                                                                                home_goals,away_goals)
            at_new_AA, at_new_AD,at_new_HA, at_new_HD = Teams.calc_away_gap_rat(home,away,
                                                                                home_goals,away_goals)

            Teams.update_gap_rat(home,away, ht_new_HA,ht_new_HD,ht_new_AA,ht_new_AD,
                                 at_new_AA,at_new_AD,at_new_HA,at_new_HD)


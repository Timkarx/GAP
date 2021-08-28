from gap_ratings.team_data.TeamsClass import Teams

def kick_off(list_of_seasons, list_of_teams, date_idx, home_team_idx, away_team_idx,
             home_gs_idx, away_gs_idx, over_odds_idx, home_gap_idx=None, away_gap_idx=None):
    # This function runs through all the loaded matches and updates
    # the gap ratings of each team after every match
    # Note1: The elements of list_of_seasons are lists of games per season
    # Note1: (i.e. the first element is a list of all games in season 1, etc.)
    # Note2: The list_of_teams variable must be a list of Teams class objects

    regression_data = []

    for each_season in list_of_seasons:
        for each_match in each_season:
            data_point = []
            date = each_match[date_idx]
            home_team = each_match[home_team_idx]
            away_team = each_match[away_team_idx]
            home_goals = each_match[home_gs_idx]
            away_goals = each_match[away_gs_idx]
            over_odds = each_match[over_odds_idx]
            total_goals = home_goals + away_goals
            if home_team_idx is not None:
                home_gap = each_match[home_gap_idx]
                away_gap = each_match[away_gap_idx]

            for team in list_of_teams:
                if team.name == home_team:
                    team.played_home_match(date, home_goals, away_goals)
                    home = team
                elif team.name == away_team:
                    team.played_away_match(date, away_goals, home_goals)
                    away = team

            match_gap_rating = home.gap_rat_HA + home.gap_rat_HD + away.gap_rat_AA + away.gap_rat_AD

            data_point.append(total_goals)
            data_point.append(match_gap_rating)
            data_point.append(over_odds)
            regression_data.append(data_point)

            ht_new_HA, ht_new_HD, ht_new_AA, ht_new_AD = Teams.calc_home_gap_rat(home, away, home_gap, away_gap)
            at_new_AA, at_new_AD, at_new_HA, at_new_HD = Teams.calc_away_gap_rat(home, away, home_gap, away_gap)

            Teams.update_gap_rat(home, away, ht_new_HA, ht_new_HD, ht_new_AA, ht_new_AD,
                                 at_new_AA, at_new_AD, at_new_HA, at_new_HD)

    return regression_data
#This function returns a neat list of teams without duplicates
def team_list(worksheet, column):
    """This function returns and ordered list of all the teams in the list"""
    teams = []
    for team in worksheet[column]:
        teams.append(team.value)

#Delete duplicates and HomeTeam and sort
    if "HomeTeam" in teams:
        teams.remove("HomeTeam")
    elif "AwayTeam" in teams:
        teams.remove("AwayTeam")
    elif "Referee" in teams:
        teams.remove("Referee")
    
    sor_teams = sorted(set(teams))
    return (sor_teams)


#This function takes returns a list of matches,
#with each match being a nested list

def match_list(worksheet, start_col, end_col):
    """This function returns information about matches"""
    matches_played = []
    for match in worksheet.iter_rows(min_col = start_col,
                                    max_col = end_col,
                                     values_only=True):
        matches_played.append(match)
    del matches_played[0]
    return(matches_played)

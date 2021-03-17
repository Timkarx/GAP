class Teams:
    """Describes attributes of a football team"""
    """gap_rat means gap raitngs"""
    
    def __init__(self,name):
        self.name = name
        self.total_scored = 0
        self.total_conceded = 0
        self.total_played = 0
        self.gap_rat_HA = 0
        self.gap_rat_HD = 0
        self.gap_rat_AA = 0
        self.gap_rat_AD = 0
        self.record = []
        self.performance = []

    def played_home_match(self, date, goals_scored=None, goals_conceded=None):
        self.total_scored += goals_scored
        self.total_conceded += goals_conceded
        self.total_played += 1
        if goals_scored > goals_conceded:
            match_outcome = 'W'
        elif goals_scored < goals_conceded:
            match_outcome = 'L'
        else:
            match_outcome = 'D'
        self.record.append(match_outcome)
        game = [date,"Home", match_outcome, self.gap_rat_HA, goals_scored, self.gap_rat_HD, goals_conceded]
        self.performance.append(game)


    def played_away_match(self, date, goals_scored=None, goals_conceded=None):
        self.total_scored += goals_scored
        self.total_conceded += goals_conceded
        self.total_played += 1
        if goals_scored > goals_conceded:
            match_outcome = 'W'
        elif goals_scored < goals_conceded:
            match_outcome = 'L'
        else:
            match_outcome = 'D'
        self.record.append(match_outcome)
        game = [date,"Away", match_outcome, self.gap_rat_AA, goals_scored, self.gap_rat_AD, goals_conceded]
        self.performance.append(game)


    def calc_home_gap_rat(home_team, away_team, home_gap_input, away_gap_input):
        """Calculates home gap ratings after a match and stores as temporary variables"""
        
        home_team_new_HA = (home_gap_input - (home_team.gap_rat_HA + away_team.gap_rat_AD)/2)
        home_team_new_HD = (away_gap_input - (home_team.gap_rat_HD + away_team.gap_rat_AA)/2)
        
        return(home_team_new_HA, home_team_new_HD)
    
    def calc_away_gap_rat(home_team, away_team, home_gap_input, away_gap_input):
        """Calculates away gap ratings after a match and stores as temporary variables"""
        
        away_team_new_AA = (away_gap_input - (away_team.gap_rat_AA + home_team.gap_rat_HD)/2)
        away_team_new_AD = (home_gap_input - (away_team.gap_rat_AD + home_team.gap_rat_HA)/2)

        return(away_team_new_AA, away_team_new_AD)

    def update_gap_rat(home_team, away_team, ht_HA, ht_HD, at_AA, at_AD,):

        lamda = 0.1

        home_team.gap_rat_HA += lamda*ht_HA
        home_team.gap_rat_HD += lamda*ht_HD
        away_team.gap_rat_AA += lamda*at_AA
        away_team.gap_rat_AD += lamda*at_AD



import datetime
class Teams:
    """This class describes the teams"""
    def __init__(self,name):
        self.name = name
        self.total_scored = 0
        self.total_conceded = 0
        self.total_played = 0
        self.gap_rat = []
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
        game = [date, match_outcome, goals_scored]
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
        game = [date, match_outcome, goals_scored]
        self.performance.append(game)

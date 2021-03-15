class Teams:
    """This class describes the teams"""
    def __init__(self,name,total_goals,):
        self.name = name
        self.total_goals = total_goals
        self.record = []
        self.performance = []

    def played_home_match(self, goals_scored=None, goals_conceded=None):
        self.total_goals += goals_scored
        if goals_scored > goals_conceded:
            match_outcome = 'W'
        elif goals_scored < goals_conceded:
            match_outcome = 'L'
        else:
            match_outcome = 'D'
        self.record.append(match_outcome)
        game = [match_outcome, goals_scored]
        self.performance.append(game)


    def played_away_match(self, goals_scored=None, goals_conceded=None):
        self.total_goals += goals_scored
        if goals_scored > goals_conceded:
            match_outcome = 'W'
        elif goals_scored < goals_conceded:
            match_outcome = 'L'
        else:
            match_outcome = 'D'
        self.record.append(match_outcome)
        game = [match_outcome, goals_scored]
        self.performance.append(game)

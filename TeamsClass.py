class Teams:
    """This class describes the teams"""
    def __init__(self,name,total_goals):
        self.name = name
        self.total_goals = total_goals

    def played_match(self, goals_scored):
        self.total_goals += goals_scored

import sys
sys.path.insert(1,r'C:\Users\Tim\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages')

from openpyxl import Workbook
from gap_ratings.data_load.extraction_funcs import *
import gap_ratings.gap_calc

league_prompt = (
    "Please choose the league that you would like to analyse: (Premier_League/Ligue_1/La_Liga/Seria_A/Bundesliga) ")
accepted_leagues = ["Premier_League", "Ligue_1", "La_Liga", "Seria_A", "Bundesliga"]
gap_input_promt = (
        "Please enter which match performance statistics you would like to choose as inputs to the gap rating system " +
        "(Shots/Shots on Target/Corners): ")
accepted_inputs = {"Shots": [9, 10], "Shots on Target": [11, 12], "Corners": [15,16],}

# Prompt the user for the league that they want to analyse
league = input(league_prompt)
if league in accepted_leagues:
    pass
else:
    print("The input doesn't constitute an allowed league")
    exit()


gap_input = input(gap_input_promt)
if gap_input in accepted_inputs.keys():
    home_input = accepted_inputs[gap_input][0]
    away_input = accepted_inputs[gap_input][1]
else:
    print("This gap input isn't currently supported")
    exit()


# Load and extract data
teams_list, matches_list = extract_league_data('D', load_leagues(league,
                                                                 10, 21), 2, 28)

# Create a list of teams where each member is a Teams class instance

all_teams = []
for season in teams_list:
    for each_team in season:
        all_teams.append(each_team)

all_teams = sorted(set(all_teams))
teams = []
for each_team in all_teams:
    teams.append(gap_ratings.gap_calc.Teams(each_team))


# Load up the initial gap_ratings
# ...


# Simulate the GAP inputs
reg_data = gap_ratings.gap_calc.kick_off(matches_list, teams, 0, 1, 2, 3, 4, 26, home_input, away_input)


# Save and export the data to an excel spreadsheet
filename = f'foot_data\output\{league}\{league}_gap_data_{gap_input}.xlsx'
workbook = Workbook()
worksheet = workbook.active

for data_point in reg_data:
    worksheet.append(data_point)


workbook.save(filename=filename)


from bkgames.reader import Reader
from bkgames.parsers import TeamFrequencyParser
from bkgames.games_history import GamesHistory
from pprint import pprint as pp

print("Starting...")

file_reader = Reader("data.dat")
file_content = file_reader.read()

parser = TeamFrequencyParser(2018)
games_history = GamesHistory()
not_parsed = []

for line in file_content:
    parsing_status, data = parser.parse(line)
    if parsing_status:
        games_history.add_game(**data)
    else:
        not_parsed.append(data)
    
teams_frequency = games_history.get_teams_frequency()
result = games_history.get_teams_to_watch(teams_frequency)
pp(result)



print("Program finished.")

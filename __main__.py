from bkgames.reader import Reader
from bkgames.parsers import TeamFrequencyParser
from bkgames.games_history import GamesHistory
from pprint import pprint as pp
from bkgames.printers import TeamsToWatchPrinter

print("Printing the oldest games at the bottom...")

file_reader = Reader("data.dat")
file_content = file_reader.read()

parser = TeamFrequencyParser(2018) # TODO: move to config file
games_history = GamesHistory()
not_parsed = []

for line in file_content:
    parsing_status, data = parser.parse(line)
    if parsing_status:
        games_history.add_game(**data)
    else:
        not_parsed.append(data)
    
teams_frequency = games_history.get_teams_frequency()
results = games_history.get_teams_to_watch(teams_frequency)

printer = TeamsToWatchPrinter(results)
printer.print_teams_to_watch()



print("Program finished.")

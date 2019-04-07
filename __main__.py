from bkgames.reader import Reader
from bkgames.parsers import TeamFrequencyParser
from bkgames.games_history import GamesHistory
from pprint import pprint as pp
from bkgames.printers import TeamsToWatchPrinter
from bkgames.reader.file_parser import FileParser

print("Printing the oldest games at the bottom...")

file_reader = Reader("data.dat")
file_content = file_reader.read()

games_history = GamesHistory() # get rid of this initialization

# TODO: move TeamFrequencyParser argument to config file
file_parser = FileParser(file_content, TeamFrequencyParser(2018), games_history)
file_parser.run()
teams_frequency = file_parser.results

results = games_history.get_teams_to_watch(teams_frequency)

printer = TeamsToWatchPrinter(results)
printer.print_teams_to_watch()


print("Program finished.")

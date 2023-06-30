# (info) With implicit packages it would work like this
# from bkgames.configuration.config_file_reader import Config
from bkgames.configuration import ConfigFileReader, Config, Initializer
from bkgames.readers import FileReader
from bkgames.parsers import FileParser, TeamFrequencyParser
from bkgames.validators import TeamsValidator
from bkgames.printers import TeamsToWatchPrinter, NotParsedLinesPrinter
from bkgames.gameshistory import GamesHistory
from bkgames.planners import PastOnlyPlanner
from bkgames.dataenhancers import NotYetPlayedEnhancer, SkipTeamsEnhancer
from bkgames.root_path import ROOT_PATH  # TODO: fix this in all places
import os

def run():
    Initializer().initialize()

    print("Printing the least recently played teams at the bottom...")
 
    exit(1)

    config_file_path = os.path.join(ROOT_PATH, "config.json")
    config = Config()
    config_reader = ConfigFileReader(config_file_path)
    config_reader.read(config)

    lines = FileReader().read()

    file_parser = FileParser(
        lines,
        TeamFrequencyParser(
            config.season_year, config.season_start_month),
        TeamsValidator(config.allowed_teams),
    )
    file_parser.run()

    parsed_lines = file_parser.parsed_lines

    games_history = GamesHistory()
    teams_history = games_history.build_teams_history(parsed_lines)

    games_planner = PastOnlyPlanner()
    teams_to_watch = games_planner.get_teams_to_watch(teams_history)

    not_yet_played_enhancer = NotYetPlayedEnhancer()
    teams_to_watch = not_yet_played_enhancer.enhance_data(
        teams_to_watch, config)

    skip_teams_enhancer = SkipTeamsEnhancer()
    teams_to_watch = skip_teams_enhancer.enhance_data(teams_to_watch, config)

    printer = TeamsToWatchPrinter()
    printer.print_teams_to_watch(teams_to_watch)

    not_parsed_lines_printer = NotParsedLinesPrinter(
        file_parser.not_parsed_lines
    )
    not_parsed_lines_printer.print_not_parsed_lines()

    print("Program finished.")

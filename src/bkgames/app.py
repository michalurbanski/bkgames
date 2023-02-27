from .configuration import Configuration
from .readers import FileReader
from .parsers import FileParser, TeamFrequencyParser
from .validators import TeamsValidator
from .printers import TeamsToWatchPrinter, NotParsedLinesPrinter
from .gameshistory import GamesHistory
from .planners import PastOnlyPlanner
from .dataenhancers import NotYetPlayedEnhancer, SkipTeamsEnhancer
from .root_path import ROOT_PATH  # TODO: fix this in all places
import os


def run():
    print("Printing the least recently played teams at the bottom...")

    config = Configuration(
        os.path.join(ROOT_PATH, "config.json"))

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

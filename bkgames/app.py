# (info) With implicit packages it would work like this.
#        So the specific file name would have to be provided.
# from bkgames.configuration.config_file_reader import Config
from bkgames.configuration import ConfigFileReader, Initializer, CustomPaths, DataFinder
from bkgames.readers import SimpleFileReader
from bkgames.parsers import FileParser, TeamFrequencyParser
from bkgames.validators import TeamsValidator
from bkgames.printers import TeamsToWatchPrinter, NotParsedLinesPrinter
from bkgames.gameshistory import GamesHistory
from bkgames.planners import PastOnlyPlanner
from bkgames.dataenhancers import NotYetPlayedEnhancer, SkipTeamsEnhancer
import logging

logging.basicConfig(level=logging.WARNING)  # should use config file, in which level will be defined


def run():
    custom_paths = CustomPaths()
    Initializer(custom_paths).initialize()

    logging.info(f"Reading configuration file: {custom_paths.config_path} ...")

    config_reader = ConfigFileReader(custom_paths.config_path)
    config = config_reader.read()

    data_finder = DataFinder(config, custom_paths)
    data_file_path = data_finder.find_data_path()

    logging.info(f"Path to the file with data is: {data_file_path}")

    reader = SimpleFileReader(data_file_path)
    lines = reader.read()

    print("Printing the least recently played teams at the bottom...")

    file_parser = FileParser(
        lines,
        TeamFrequencyParser(config.season_start_month),
        TeamsValidator(config.allowed_teams),
    )
    file_parser.run()

    teams_history = GamesHistory().build_teams_history(file_parser.parsed_lines)
    teams_to_watch = PastOnlyPlanner().get_teams_to_watch(teams_history)

    # Enhancers could use chain of responsibility pattern. But there's no need to
    # do it in this simple app.
    not_yet_played_enhancer = NotYetPlayedEnhancer()
    teams_to_watch = not_yet_played_enhancer.enhance_data(teams_to_watch, config)

    skip_teams_enhancer = SkipTeamsEnhancer()
    teams_to_watch = skip_teams_enhancer.enhance_data(teams_to_watch, config)

    printers = [
        TeamsToWatchPrinter(teams_to_watch),
        NotParsedLinesPrinter(file_parser.not_parsed_lines),
    ]

    for printer in printers:
        printer.print()

    print("Program finished.")

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
import logging.config
import os

# Location relative to the file. Ensures that the path to the config file
# is correct even after the app installation.
script_dir = os.path.dirname(__file__)
logging_config_path = os.path.join(script_dir, "logging.ini")
logging.config.fileConfig(logging_config_path)
logger = logging.getLogger(__name__)

def run():
    custom_paths = CustomPaths()
    Initializer(custom_paths).initialize()

    logger.info(f"Reading configuration file: {custom_paths.config_path} ...")

    config = ConfigFileReader(custom_paths.config_path).read()
    data_file_path = DataFinder(config, custom_paths).find_data_path()

    logger.info(f"Path to the file with data is: {data_file_path}")

    lines = SimpleFileReader(data_file_path).read()

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

# (info) With implicit packages it would work like this.
#        So the specific file name would have to be provided.
# from bkgames.configuration.config_file_reader import Config
from typing import List
from bkgames.configuration import (
    ConfigFileReader,
    Initializer,
    ApplicationPaths,
    DataFinder,
)
from bkgames.configuration.config import Config
from bkgames.readers import SimpleFileReader
from bkgames.parsers import FileParser, TeamFrequencyParser
from bkgames.validators import TeamsValidator
from bkgames.printers import TeamsToWatchPrinter, NotParsedLinesPrinter
from bkgames.gameshistory import GamesHistory
from bkgames.planners import PastOnlyPlanner
from bkgames.dataenhancers import NotYetPlayedEnhancer, SkipTeamsEnhancer
from bkgames.infrastructure import setup_logging
import logging

setup_logging()
logger = logging.getLogger(__name__)


def load_data(
    config: Config, app_paths: ApplicationPaths, logger: logging.Logger
) -> List[str]:
    data_file_path = DataFinder(config, app_paths).find_data_path()

    logger.info(f"Path to the file with data is: {data_file_path}")

    return SimpleFileReader(data_file_path).read()


def run():
    app_paths = ApplicationPaths()
    Initializer(app_paths).initialize()
    config_file_path = app_paths.config_path

    logger.info(f"Reading configuration file: {config_file_path} ...")

    config = ConfigFileReader(config_file_path).read()
    lines = load_data(config, app_paths, logger)

    file_parser = FileParser(
        lines,
        TeamFrequencyParser(config.season_start_month),
        TeamsValidator(config.allowed_teams),
    )
    # TODO: file_parser.run() could just return parsed lines - it would look nicer - both parsed and not parsed as an object of a class that does not exist yet.
    file_parser.run()

    teams_history = GamesHistory().build_teams_history(file_parser.parsed_lines)
    teams_to_watch = PastOnlyPlanner().get_teams_to_watch(teams_history)

    # Enhancers could use chain of responsibility pattern.
    # It would be an overkill to do it in this simple app.
    not_yet_played_enhancer = NotYetPlayedEnhancer()
    teams_to_watch = not_yet_played_enhancer.enhance_data(teams_to_watch, config)

    skip_teams_enhancer = SkipTeamsEnhancer()
    teams_to_watch = skip_teams_enhancer.enhance_data(teams_to_watch, config)

    printers = [
        TeamsToWatchPrinter(teams_to_watch),
        NotParsedLinesPrinter(file_parser.not_parsed_lines),
    ]

    print("Printing the least recently played teams at the bottom...")

    [printer.print() for printer in printers]

    print("Program finished.")

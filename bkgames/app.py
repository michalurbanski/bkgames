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
from bkgames.parsers import RawLineParser, TeamFrequencyParser
from bkgames.validators import TeamsValidator
from bkgames.models import TeamModel
from bkgames.printers import TeamsToWatchPrinter, NotParsedLinesPrinter
from bkgames.gameshistory import GamesHistory
from bkgames.planners import PastOnlyPlanner
from bkgames.dataenhancers import (
    EnhancerProtocol,
    NotYetPlayedEnhancer,
    SkipTeamsEnhancer,
)
from bkgames.infrastructure import setup_logging
import logging

setup_logging()
logger = logging.getLogger(__name__)


def _load_data(
    config: Config, app_paths: ApplicationPaths, logger: logging.Logger
) -> List[str]:
    data_file_path = DataFinder(config, app_paths).find_data_path()

    logger.info(f"Path to the file with data is: {data_file_path}")

    return SimpleFileReader(data_file_path).read()


def _enhance_teams_to_watch(
    teams_to_watch: List[TeamModel], config: Config
) -> List[TeamModel]:
    enhancers: List[EnhancerProtocol] = [
        NotYetPlayedEnhancer(config.allowed_teams),
        SkipTeamsEnhancer(config.skipped_teams),
    ]

    for enhancer in enhancers:
        teams_to_watch = enhancer.enhance_data(teams_to_watch)

    return teams_to_watch


def run():
    app_paths = ApplicationPaths()
    Initializer(app_paths).initialize()
    config_file_path = app_paths.config_path

    logger.info(f"Reading configuration file: {config_file_path} ...")

    config = ConfigFileReader(config_file_path).read()
    input_lines = _load_data(config, app_paths, logger)

    file_parser = RawLineParser(
        TeamFrequencyParser(config.season_start_month),
        TeamsValidator(config.allowed_teams),
    )
    parsing_result = file_parser.run(input_lines)

    teams_history = GamesHistory().build_teams_history(parsing_result.parsed_lines)
    teams_to_watch = PastOnlyPlanner().get_teams_to_watch(teams_history)
    teams_to_watch = _enhance_teams_to_watch(teams_to_watch, config)

    printers = [
        TeamsToWatchPrinter(teams_to_watch),
        NotParsedLinesPrinter(parsing_result.not_parsed_lines),
    ]

    print("Printing the least recently played teams at the bottom...")

    for printer in printers:
        printer.print()

    print("Program finished.")

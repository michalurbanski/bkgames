# (info) With implicit packages it would work like this
# from bkgames.configuration.config_file_reader import Config
from bkgames.configuration import ConfigFileReader, Config, Initializer, CustomPaths
from bkgames.readers import FileReader
from bkgames.parsers import FileParser, TeamFrequencyParser
from bkgames.validators import TeamsValidator
from bkgames.printers import TeamsToWatchPrinter, NotParsedLinesPrinter
from bkgames.gameshistory import GamesHistory
from bkgames.planners import PastOnlyPlanner
from bkgames.dataenhancers import NotYetPlayedEnhancer, SkipTeamsEnhancer


def run():
    # TODO: there should be a configuration class that keeps the information
    #       what is the user folder, it has path to the config file, user folder, data path.
    #       Initializer should only use that data. Initializer should also create a data folder inside user directory.
    #       Another class DataConfigurator or similar should check if any data exists (data folder is not empty)
    #       config.json should have a regexp to search data files with a specific naming convention s2021.dat or similar

    custom_paths = CustomPaths()

    initializer = Initializer(
        application_folder_path=custom_paths.application_folder_path,
        config_file_name=custom_paths.config_file_name,
        config_file_path=custom_paths.config_path,
        data_folder_path=custom_paths.data_folder_path,
    )
    initializer.execute()

    print("Reading configuration file...")

    config = Config()
    config_reader = ConfigFileReader(custom_paths.config_path)
    config_reader.read(config)

    exit(1)

    lines = FileReader().read()

    print("Printing the least recently played teams at the bottom...")

    file_parser = FileParser(
        lines,
        TeamFrequencyParser(config.season_year, config.season_start_month),
        TeamsValidator(config.allowed_teams),
    )
    file_parser.run()

    parsed_lines = file_parser.parsed_lines

    games_history = GamesHistory()
    teams_history = games_history.build_teams_history(parsed_lines)

    games_planner = PastOnlyPlanner()
    teams_to_watch = games_planner.get_teams_to_watch(teams_history)

    not_yet_played_enhancer = NotYetPlayedEnhancer()
    teams_to_watch = not_yet_played_enhancer.enhance_data(teams_to_watch, config)

    skip_teams_enhancer = SkipTeamsEnhancer()
    teams_to_watch = skip_teams_enhancer.enhance_data(teams_to_watch, config)

    printer = TeamsToWatchPrinter()
    printer.print_teams_to_watch(teams_to_watch)

    not_parsed_lines_printer = NotParsedLinesPrinter(file_parser.not_parsed_lines)
    not_parsed_lines_printer.print_not_parsed_lines()

    print("Program finished.")

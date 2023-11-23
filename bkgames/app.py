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


def run():
    custom_paths = CustomPaths()
    Initializer(custom_paths).initialize()

    # TODO: use logging library for such diagnostic messages.
    print(f"Reading configuration file: {custom_paths.config_path} ...")

    config_reader = ConfigFileReader(custom_paths.config_path)
    config = config_reader.read()

    data_finder = DataFinder(config, custom_paths)
    data_file_path = data_finder.find_data_path()
    print(f"Path to the file with data is: {data_file_path}")

    reader = SimpleFileReader(data_file_path)
    lines = reader.read()

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

    # Enhancers could use chain of responsibility pattern. But there's no need to
    # do it in this simple app.
    not_yet_played_enhancer = NotYetPlayedEnhancer()
    teams_to_watch = not_yet_played_enhancer.enhance_data(teams_to_watch, config)

    skip_teams_enhancer = SkipTeamsEnhancer()
    teams_to_watch = skip_teams_enhancer.enhance_data(teams_to_watch, config)

    printer = TeamsToWatchPrinter()
    printer.print_teams_to_watch(teams_to_watch)

    not_parsed_lines_printer = NotParsedLinesPrinter(file_parser.not_parsed_lines)
    not_parsed_lines_printer.print_not_parsed_lines()

    print("Program finished.")

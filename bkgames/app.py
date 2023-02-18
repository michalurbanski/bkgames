from bkgames import configuration
from bkgames import reader
from bkgames import parsers
from bkgames import validators
from bkgames import printers
from bkgames import gameshistory
from bkgames import planners
from bkgames.dataenhancers import NotYetPlayedEnhancer, SkipTeamsEnhancer


def run():
    print("Printing the oldest games at the bottom...")

    config = configuration.Configuration("config.json")
    file_content = reader.Reader.create_default_reader().read()

    file_parser = parsers.FileParser(
        file_content,
        parsers.TeamFrequencyParser(
            config.season_year, config.season_start_month),
        validators.TeamsValidator(config.allowed_teams),
    )
    file_parser.run()

    parsed_lines = file_parser.parsed_lines

    games_history = gameshistory.GamesHistory()
    teams_history = games_history.build_teams_history(parsed_lines)

    games_planner = planners.PastOnlyPlanner()
    teams_to_watch = games_planner.get_teams_to_watch(teams_history)

    not_yet_played_enhancer = NotYetPlayedEnhancer()
    teams_to_watch = not_yet_played_enhancer.enhance_data(
        teams_to_watch, config)

    skip_teams_enhancer = SkipTeamsEnhancer()
    teams_to_watch = skip_teams_enhancer.enhance_data(teams_to_watch, config)

    printer = printers.TeamsToWatchPrinter()
    printer.print_teams_to_watch(teams_to_watch)

    not_parsed_lines_printer = printers.NotParsedLinesPrinter(
        file_parser.not_parsed_lines
    )
    not_parsed_lines_printer.print_not_parsed_lines()

    print("Program finished.")

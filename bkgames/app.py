from bkgames import configuration
from bkgames import reader
from bkgames import parsers
from bkgames import validators
from bkgames import printers
from bkgames import gameshistory
from bkgames import planners
from bkgames.dataenhancers import NotYetPlayedEnhancer


def run():
    print("Printing the oldest games at the bottom...")

    config = configuration.Configuration("config.json")
    file_content = reader.Reader().read()

    file_parser = parsers.FileParser(
        file_content,
        parsers.TeamFrequencyParser(
            config.season_year, config.season_start_month),
        validators.TeamsValidator(config.allowed_teams))
    file_parser.run()

    games = file_parser.parsed_lines

    games_history = gameshistory.GamesHistory()
    teams_history = games_history.build_teams_history(games)

    games_planner = planners.PastOnlyPlanner(teams_history)
    teams_to_watch = games_planner.get_teams_to_watch()

    not_yet_played_enhancer = NotYetPlayedEnhancer(config)
    teams_to_watch = not_yet_played_enhancer.enhance_data(teams_to_watch)

    printer = printers.TeamsToWatchPrinter(teams_to_watch)
    printer.print_teams_to_watch()

    not_parsed_lines_printer = printers.NotParsedLinesPrinter(
        file_parser.not_parsed_lines)
    not_parsed_lines_printer.print_not_parsed_lines()

    print("Program finished.")

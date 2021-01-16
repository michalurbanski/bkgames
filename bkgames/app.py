from bkgames import configuration
from bkgames import reader
from bkgames import parsers
from bkgames import printers
from bkgames import gameshistory
from bkgames.dataenhancers import NotYetPlayedEnhancer


def run():
    print("Printing the oldest games at the bottom...")

    config = configuration.Configuration("config.json")
    file_content = reader.Reader().read()

    file_parser = parsers.FileParser(
        file_content,
        parsers.TeamFrequencyParser(
            config.season_year, config.season_start_month),
        parsers.TeamsValidator(config.allowed_teams))
    file_parser.run()

    games = file_parser.parsed_lines
    games_history = _build_games_history(games)

    # TODO: get_teams_to_watch might use only history data,
    # but it may also rely on the future data (if desired).
    # GamesPlanner would be a good name for this class.
    # It's appropriate to put it in a different class and abstract it.
    # Right now only historic data is fetched here.
    teams_to_watch = games_history.get_teams_to_watch()

    not_yet_played_enhancer = NotYetPlayedEnhancer(config)
    teams_to_watch = not_yet_played_enhancer.enhance_data(teams_to_watch)

    printer = printers.TeamsToWatchPrinter(teams_to_watch)
    printer.print_teams_to_watch()

    not_parsed_lines_printer = printers.NotParsedLinesPrinter(
        file_parser.not_parsed_lines)
    not_parsed_lines_printer.print_not_parsed_lines()

    print("Program finished.")


def _build_games_history(lines):
    history = gameshistory.GamesHistory()
    for line in lines:
        # Unpack object keys to the list of arguments expected by the function
        history.add_game(**line)
    return history

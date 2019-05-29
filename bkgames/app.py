import bkgames.reader as reader
import bkgames.parsers as parsers
import bkgames.printers as printers
import bkgames.gameshistory as gameshistory

def run():

    print("Printing the oldest games at the bottom...")

    config = reader.Configuration("config.json")
    file_content = reader.Reader("data.dat").read()
    games_history = gameshistory.GamesHistory() # get rid of this initialization

    file_parser = parsers.FileParser(file_content, 
        parsers.TeamFrequencyParser(config.season_year, config.season_start_month), 
        parsers.ValidTeamParser(config.allowed_teams), 
        games_history)
    file_parser.run()
    teams_frequency = file_parser.results

    results = games_history.get_teams_to_watch(teams_frequency)

    printer = printers.TeamsToWatchPrinter(results)
    printer.print_teams_to_watch()

    not_parsed_lines_printer = printers.NotParsedLinesPrinter(file_parser.not_parsed_lines)
    not_parsed_lines_printer.print_not_parsed_lines()

    print("Program finished.")

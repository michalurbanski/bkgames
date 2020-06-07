from datetime import datetime
from bkgames.helpers import game_helper
import re
import traceback

class TeamFrequencyParser:

    def __init__(self, season_start_year, season_start_month):
        self._season_start_year = season_start_year
        self._season_start_month = season_start_month

    def parse(self, line):
        """
        Expected format is day.month (without year); day and/or month can be 1 or 2 digits.
        Example: DONE - Nba game 16.10 bos at phi -> bos?

        Returns: (status, data) - bool, dict
        """
        try:
            date_search = re.findall(r"\d{1,2}\.\d{1,2}", line, flags=re.I)
            if not date_search: # if list is empty, i.e. searched expression was not found
                raise ValueError("Line does not have correct data")
            
            # date_search is expected to be 'day.month'
            found_date = date_search[0] # first occurrence of date
            split = found_date.split(".")

            day = split[0]
            month = split[1]
            game_year = game_helper.calculate_game_year(
                    self._season_start_year, 
                    self._season_start_month, 
                    int(month)
                )
            date = datetime(game_year, int(month), int(day))

            # Get what's after the date
            skip_after = f"{day}.{month}"
            end_pos = re.search(skip_after, line).end()
            split = re.split(r"\s", line[end_pos:])
            remaining_list = list(filter(None, split)) # Clean empty strings
        except Exception as e:
            tb = traceback.format_exc()
            return (False, {"not_parsed": line, "error": e, "traceback": tb})
        
        return (True, {
                "home_team": remaining_list[0], #[1] is 'at' word that is not needed
                "away_team": remaining_list[2],
                "date": date,
                "line": line
                })
        
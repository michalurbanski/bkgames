from datetime import datetime
import re
import traceback

class TeamFrequencyParser:
    
    SEASON_START_MONTH = 9

    #TODO: year value should be take from config
    def __init__(self, season_start_year):
        TeamFrequencyParser.season_start_year = season_start_year

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
            date = datetime(TeamFrequencyParser._get_game_year(month), int(month), int(day))

            # Get what's after the date
            skip_after = day + "." + month
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

    @classmethod
    def _get_game_year(cls, month):
        return cls.season_start_year if int(month) >= cls.SEASON_START_MONTH else (cls.season_start_year + 1)
        
from datetime import datetime
import re

class TeamFrequencyParser:
    
    SEASON_START_MONTH = 9

    #TODO: year value should be take from config
    def __init__(self, season_start_year):
        TeamFrequencyParser.season_start_year = season_start_year

    def parse(self, line):
        """
        Expected format is day.month (without year)
        Example: DONE - Nba game 16.10 bos at phi -> bos?

        Returns: (status, data) - bool, dict
        """
        try:
            date_search = re.findall(r"\d{2}", line, flags=re.I)
            if not date_search: # if list is empty, i.e. searched expression was not found
                raise ValueError("Line does not have correct data")
            
            day = date_search[0]
            month = date_search[1]
            date = datetime(TeamFrequencyParser._get_game_year(month), int(month), int(day))

            # Get what's after the date
            skip_after = day + "." + month
            end_pos = re.search(skip_after, line).end()
            split = re.split(r"\s", line[end_pos:])
            remaining_list = list(filter(None, split)) # Clean empty strings
        except Exception as e:
            return (False, {"not_parsed": line, "error": e})
        
        return (True, {
                "home_team": remaining_list[0], #[1] is 'at' word that is not needed
                "away_team": remaining_list[2],
                "date": date
                })

    @classmethod
    def _get_game_year(cls, month):
        return cls.season_start_year if int(month) >= cls.SEASON_START_MONTH else (cls.season_start_year + 1)
        



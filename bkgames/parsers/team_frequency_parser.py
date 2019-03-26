from datetime import datetime
import re

class TeamFrequencyParser:
    
    @staticmethod
    def Parse(line):
        """
        Expected format is day.month (without year)
        Example: DONE - Nba game 16.10 bos at phi -> bos?

        Returns: (status, data) - bool, dict
        """
        try:
            date_search = re.findall(r"\d{2}", line, flags=re.I)
            if not date_search: # if list is empty, i.e. searched expression was not found
                raise ValueError("Line does not have correct data")
            
            #TODO: year value should be take from config, maybe callable class would be good for this?
            date = datetime(2018, int(date_search[1]), int(date_search[0]))

            # Get what's after the date
            skip_after = date_search[0] + "." + date_search[1]
            end_pos = re.search(skip_after, line).end()
            split = re.split(r"\s", line[end_pos:])
            remaining_list = list(filter(None, split)) # Clean empty strings
        except:
            return (False, {"not_parsed": line})
        
        return (True, {
                "home_team": remaining_list[0], #[1] is 'at' word
                "away_team": remaining_list[2],
                "date": date
                })

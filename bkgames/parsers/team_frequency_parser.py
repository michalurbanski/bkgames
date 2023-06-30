from datetime import datetime
import re
import traceback
from typing import Tuple


class TeamFrequencyParser:

    def __init__(self, season_start_year: int, season_start_month: int):
        self._season_start_year = season_start_year
        self._season_start_month = season_start_month

    def parse(self, line: str) -> Tuple[bool, dict]:
        """
        Expected format is day.month (without year); day and/or month can be 1 or 2 digits.
        Example: DONE - Nba game 16.10 bos at phi -> bos?

        Returns: (status, data) - bool, dict
        """
        try:
            date_search = re.findall(r"\d{1,2}\.\d{1,2}", line, flags=re.I)
            if not date_search:  # if list is empty, i.e. searched expression was not found
                raise ValueError("Line does not have correct data")

            # date_search is expected to be 'day.month'
            found_date = date_search[0]  # first occurrence of a date
            (day, month) = found_date.split(".")

            # NOTE: if games are in order, then this can be calculated only once
            game_year = self._calculate_game_year(
                self._season_start_year,
                self._season_start_month,
                int(month)
            )
            date = datetime(game_year, int(month), int(day))

            # Get what's after the date
            skip_after = f"{day}.{month}"
            end_pos = re.search(skip_after, line).end()
            split = re.split(r"\s", line[end_pos:])
            remaining_list = list(filter(None, split))  # Clean empty strings
        except Exception as e:
            tb = traceback.format_exc()
            return (False, {"not_parsed": line, "error": e, "traceback": tb})

        return (True, {
                # remaining_list[1] is 'at' word that can be skipped
                "home_team": remaining_list[0],
                "away_team": remaining_list[2],
                "date": date,
                "line": line
                })

    @staticmethod
    def _calculate_game_year(season_start_year: int, season_start_month: int, month: int) -> int:
        """ Based on available data, calculates year in which games was played.

        Year information is missing in current input data - only month and day
        are available. Year has to be inferred then from available data.

        When season starts in October (10th month), months greater than 10 are
        known to be in the same year. If month has smaller number, it means that
        it's from the next year. E.g. game on 1.01 takes place after 30.12

        Parameters:
            season_start_year (int): Year when season has started
                (in current implementation - from config file)
            season_start_month (int): Month starting from which games should be
                processed
            month (int): Month when game was played

        Returns:
            int: Year in which game was played
        """

        if month >= season_start_month:
            return season_start_year

        return season_start_year + 1

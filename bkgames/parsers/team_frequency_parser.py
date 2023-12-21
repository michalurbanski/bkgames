from bkgames.models import GameDate
import re
import traceback
from typing import Tuple


class TeamFrequencyParser:
    def __init__(self, season_start_month: int):
        self._season_start_month = season_start_month

    def parse(self, line: str) -> Tuple[bool, dict]:
        """
        Expected format is day.month (without year); day and/or month can be 1 or 2 digits.
        Example: DONE - Nba game 16.10 bos at phi -> bos?

        Returns: (status, data) - bool, dict
        """
        try:
            date_search = re.findall(r"\d{1,2}\.\d{1,2}", line, flags=re.I)
            if (
                not date_search
            ):  # if list is empty, i.e. searched expression was not found
                raise ValueError("Line does not have correct data")

            # date_search is expected to be 'day.month'
            found_date = date_search[0]  # first occurrence of a date
            (day, month) = found_date.split(".")

            game_date = GameDate(
                month=int(month),
                day=int(day),
                season_start_month=self._season_start_month,
            )

            # Get what's after the date
            skip_after = f"{day}.{month}"
            end_pos = re.search(skip_after, line).end()
            split = re.split(r"\s", line[end_pos:])
            remaining_list = list(filter(None, split))  # Clean empty strings
        except Exception as e:
            tb = traceback.format_exc()
            return (False, {"not_parsed": line, "error": e, "traceback": tb})

        return (
            True,
            {
                # remaining_list[1] is 'at' word that can be skipped
                "home_team": remaining_list[0],
                "away_team": remaining_list[2],
                "game_date": game_date,
                "line": line,
            },
        )

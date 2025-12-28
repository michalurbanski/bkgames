from bkgames.models import GameDate
from bkgames.parsers import LineParserBase
import re
import traceback
from typing import Union
from .parse_result import ParsedLine, NotParsedLine


# TODO: name of this class is not clear. And it inherits from LineParserBase.
# Its name doesn't say anything that it's a type of line parser.
class TeamFrequencyParser(LineParserBase):
    def __init__(self, season_start_month: int):
        if season_start_month < 1 or season_start_month > 12:
            raise ValueError(f"Incorrect season start month: {season_start_month}")

        self._season_start_month = season_start_month

    # TODO: it might be a bad idea to return union. It's not easy to handle it later. Asserting by types is needed then.
    def parse(self, line: str) -> Union[ParsedLine, NotParsedLine]:
        """
        Expected format is day.month (without year); day and/or month can be 1 or 2 digits.
        Example: DONE - Nba game 16.10 bos at phi -> bos?

        Returns: (status, data) - bool, dict
        """
        try:
            # date_search_result is expected to be "day.month", e.g. 12.01, 3.5
            date_search_result = re.findall(r"\d{1,2}\.\d{1,2}", line, flags=re.I)
            if not date_search_result:
                raise ValueError("Line does not have correct data")

            found_date = date_search_result[0]  # first occurrence of a date
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
            return NotParsedLine(
                raw_line=line,
                error=e,
                traceback=tb,
            )

        return ParsedLine(
            away_team=remaining_list[0],
            home_team=remaining_list[2],
            game_date=game_date,
            raw_line=line,
        )

from typing import List, Tuple
from datetime import datetime
from bkgames.reader.configuration import Configuration


class NotYetPlayedEnhancer:

    def __init__(self, config: Configuration):
        self._config = config

    def enhance_data(
        self,
        input: List[Tuple[str, int, List[datetime], datetime]]
    ) -> List[Tuple[str, int, List[datetime], datetime]]:
        """
        When team has not played yet, it's not in the results (input to this function).
        To display information that team has 0 games, results have to be enhanced.
        """

        allowed_teams = self._config.allowed_teams
        if (len(allowed_teams) != len(input)):
            teams_that_played = [item[0] for item in input]
            missing_teams = self._find_difference(
                allowed_teams, teams_that_played)

            for team in missing_teams:
                input.append((team, 0, [], None))

        return input

    @staticmethod
    def _find_difference(first: List[str], second: List[str]) -> List[str]:
        """ first list has to contain the second list """

        # Note: there's even better solution to find difference:
        # https://stackoverflow.com/a/3462202
        return list(set(first) - set(second))

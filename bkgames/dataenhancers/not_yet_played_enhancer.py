from typing import List
from bkgames.configuration import Configuration
from bkgames.reader import TeamModel


class NotYetPlayedEnhancer:
    def enhance_data(
        self, input: List[TeamModel], config: Configuration
    ) -> List[TeamModel]:
        """
        When team has not played yet, it's not in the results (input to this function).
        Enhance results by adding those teams that have 0 games.
        """

        allowed_teams = config.allowed_teams
        if len(allowed_teams) != len(input):
            teams_that_played = [team.team_code for team in input]
            missing_teams = self._find_difference(allowed_teams, teams_that_played)

            for team in missing_teams:
                input.append(TeamModel(team))

        return input

    @staticmethod
    def _find_difference(first: List[str], second: List[str]) -> List[str]:
        """first list has to contain the second list"""

        # Note: there's even better solution to find difference:
        # https://stackoverflow.com/a/3462202
        return list(set(first) - set(second))

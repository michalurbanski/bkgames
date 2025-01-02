import copy
from typing import List
from bkgames.configuration import Config
from bkgames.models import TeamModel


class NotYetPlayedEnhancer:
    def enhance_data(self, input: List[TeamModel], config: Config) -> List[TeamModel]:
        """
        When team has not played yet, it's not in the results (input to this function).
        Enhance results by adding those teams that have 0 games played,
        so that they show up in the results.
        """

        allowed_teams = config.allowed_teams
        results = copy.deepcopy(input)

        if len(allowed_teams) != len(input):
            teams_that_played = [team.team_code for team in input]
            missing_teams = self._find_difference(allowed_teams, teams_that_played)

            for team in missing_teams:
                results.append(TeamModel(team))

        return results

    @staticmethod
    def _find_difference(first: List[str], second: List[str]) -> List[str]:
        """First list has to be a superset of the second list to get any meaningful results.
        """

        # Note: there's even better solution to find difference:
        # https://stackoverflow.com/a/3462202
        return list(set(first) - set(second))

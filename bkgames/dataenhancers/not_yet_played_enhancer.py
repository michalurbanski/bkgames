import copy
from typing import List
from bkgames.models import TeamModel


class NotYetPlayedEnhancer:
    def __init__(self, allowed_teams: List[str]):
        self._allowed_teams = allowed_teams

    def enhance_data(self, input: List[TeamModel]) -> List[TeamModel]:
        """
        When a team has not played yet, it's not in the results (input to this function).
        Enhance results by adding those teams that have 0 games played,
        so that they show up in the results.

        Args:
            input: List of TeamModel objects representing teams that have played games

        Returns:
            List[TeamModel]: Enhanced list of teams including both teams that have played
            and teams that haven't played yet (with 0 games)
        """

        results = copy.deepcopy(input)

        # No additional teams to be added, all are already in place.
        if len(self._allowed_teams) == len(input):
            return results

        teams_that_played = [team.team_code for team in input]
        missing_teams = self._find_difference(self._allowed_teams, teams_that_played)

        teams_to_add = [TeamModel(team) for team in missing_teams]
        results.extend(teams_to_add)

        return results

    @staticmethod
    def _find_difference(first: List[str], second: List[str]) -> List[str]:
        """First list has to be a superset of the second list to get any meaningful results."""

        # Note: there's even better solution to find difference:
        # https://stackoverflow.com/a/3462202
        return list(set(first) - set(second))

import copy
from typing import List
from bkgames.models import TeamModel


class SkipTeamsEnhancer:
    """Skips some teams from watching, based on the passed list to exclude."""

    def __init__(self, skipped_teams: List[str]):
        self._skipped_teams = skipped_teams

    def enhance_data(self, input: List[TeamModel]) -> List[TeamModel]:
        results = copy.deepcopy(input)

        if not self._skipped_teams:
            return results

        for team in results:
            if team.team_code in self._skipped_teams:
                team.skip_from_watching = True

        return results

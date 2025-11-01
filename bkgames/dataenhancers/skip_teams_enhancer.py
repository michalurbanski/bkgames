import copy
from typing import List
from bkgames.models import TeamModel


class SkipTeamsEnhancer:
    """Skips some teams from watching, based on the passed list to exclude."""

    def enhance_data(
        self, input: List[TeamModel], skipped_teams: List[str]
    ) -> List[TeamModel]:
        results = copy.deepcopy(input)

        if not skipped_teams:
            return results

        for team in results:
            if team.team_code in skipped_teams:
                team.skip_from_watching = True

        return results

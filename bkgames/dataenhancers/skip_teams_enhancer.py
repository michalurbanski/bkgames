from typing import List
from bkgames.models import TeamModel
from bkgames.configuration import Config


class SkipTeamsEnhancer:
    """Skips some teams from watching, based on config file."""

    def enhance_data(self, input: List[TeamModel], config: Config) -> List[TeamModel]:
        for team in input:
            if team.team_code in config.skipped_teams:
                team.skip_from_watching = True
        return input

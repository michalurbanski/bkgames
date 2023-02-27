from typing import List
from bkgames.readers import TeamModel
from bkgames.configuration import Configuration


class SkipTeamsEnhancer:
    """Skips some teams from watching, based on config file."""

    def enhance_data(
        self, input: List[TeamModel], config: Configuration
    ) -> List[TeamModel]:
        for team in input:
            if team.team_code in config.skipped_teams:
                team.skip_from_watching = True
        return input

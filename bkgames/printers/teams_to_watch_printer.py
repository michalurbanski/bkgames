from typing import List
from bkgames.models import TeamModel


class TeamsToWatchPrinter:
    def __init__(self, teams: List[TeamModel]):
        self._teams = teams

    def print(self):
        for team in self._teams:
            # TODO: team should not have information whether it should be watched or not
            #       it's not a feature of a team.
            if not team.skip_from_watching:
                print(team.team_code, team.number_of_games_played)
            else:
                print(team.team_code, team.number_of_games_played, "(skip)")

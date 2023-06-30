from typing import List
from bkgames.readers import TeamModel


class TeamsToWatchPrinter:
    def print_teams_to_watch(self, teams: List[TeamModel]):
        for team in teams:
            if not team.skip_from_watching:
                print(team.team_code, team.number_of_games_played)
            else:
                print(team.team_code, team.number_of_games_played, "(skip)")

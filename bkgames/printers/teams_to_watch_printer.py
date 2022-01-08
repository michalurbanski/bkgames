from typing import List
from bkgames.reader import TeamModel


class TeamsToWatchPrinter:
    def print_teams_to_watch(self, teams: List[TeamModel]):
        for team in teams:
            print(team.team_code, team.number_of_games_played)

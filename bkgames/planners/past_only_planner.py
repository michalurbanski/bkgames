from typing import List
from bkgames.models import TeamModel
from copy import deepcopy


class PastOnlyPlanner:
    """Finds teams to watch, based only on past games."""

    def get_teams_to_watch(self, teams_history: List[TeamModel]) -> List[TeamModel]:
        """Get teams to watch, based on historic results.
        Teams watched the longest time ago is the last in the returned collection.

        Args:
            teams_history (List[TeamModel]): List of teams with dates of games
                played by them.

        Returns:
            List[TeamModel]: List of teams ordered by:
                - the most played games
                - and most recently played game (in case of ties for the 1st condition)

        Example:
            first_team      6 games     23 days ago
            second_team     6 games     25 days ago
            third_team      4 games     30 days ago
        """

        # Games played by teams are read from a file in chronological order.
        # Oldest game is first, newest game is last.
        # To easier sort by the most recent games, it's convenient to sort those
        # games at first.

        if teams_history is None or len(teams_history) == 0:
            raise ValueError("Empty collection of games")

        # Copy in order not to change input collection.
        copied_teams = deepcopy(teams_history)

        for team in copied_teams:
            team.games_dates.sort()

        return sorted(
            copied_teams,
            key=lambda team: (team.number_of_games_played, team.games_dates[-1]),
            reverse=True,
        )

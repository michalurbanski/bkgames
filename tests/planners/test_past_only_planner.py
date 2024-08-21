import pytest
from bkgames.planners.past_only_planner import PastOnlyPlanner
from bkgames.gameshistory import GamesHistory
from bkgames.models import GameDate


class TestPastOnlyPlanner:
    def test_empty_list_of_games_throws_error(self):
        games = list()
        games_history = GamesHistory()
        teams = games_history.build_teams_history(games)

        games_planner = PastOnlyPlanner()

        with pytest.raises(ValueError):
            games_planner.get_teams_to_watch(teams)

    def test_most_games_played_at_the_top(self):
        """
        input:
        bos, atl, 23.10
        bos, phx, 24.10

        should give the following outcome:
        bos -> at the top
        atl, phx -> we don't care in this test
        """

        games = list()
        games.append(self._make_game("bos", "atl", "23.10"))
        games.append(self._make_game("bos", "phx", "24.10"))

        games_history = GamesHistory()
        teams = games_history.build_teams_history(games)
        games_planner = PastOnlyPlanner()
        teams_to_watch = games_planner.get_teams_to_watch(teams)

        assert teams_to_watch[0].team_code == "bos"

    def test_same_number_of_games_newest_game_at_the_top(self):
        """
        input:
        bos, atl, 23.10
        phx, nyk, 25.10

        should give the following outcome:
        phx or nyk -> at the top
        bos or atl -> at the bottom
        """

        games = list()
        games.append(self._make_game("bos", "atl", "23.10"))
        games.append(self._make_game("phx", "nyk", "25.10"))

        games_history = GamesHistory()
        teams = games_history.build_teams_history(games)
        games_planner = PastOnlyPlanner()
        teams_to_watch = games_planner.get_teams_to_watch(teams)

        most_recently_watched_team = teams_to_watch[0].team_code
        least_recently_watched_team = teams_to_watch[-1].team_code

        assert most_recently_watched_team in {"phx", "nyk"}, most_recently_watched_team
        assert least_recently_watched_team in {
            "bos",
            "atl",
        }, least_recently_watched_team

    def test_two_games_played_correct_order(self):
        """
        input:
        bos, atl, 23.10
        nyk, hou, 24.10
        nyk, mia, 25.10
        bos, phx, 26.10

        should give the following outcome
        bos -> 1st
        nyk -> 2nd
        """

        games = list()
        games.append(self._make_game("bos", "atl", "23.10"))
        games.append(self._make_game("nyk", "hou", "24.10"))
        games.append(self._make_game("nyk", "mia", "25.10"))
        games.append(self._make_game("bos", "phx", "26.10"))

        games_history = GamesHistory()
        teams = games_history.build_teams_history(games)
        games_planner = PastOnlyPlanner()
        teams_to_watch = games_planner.get_teams_to_watch(teams)

        assert teams_to_watch[0].team_code == "bos"
        assert teams_to_watch[1].team_code == "nyk"

    def test_two_games_played_correct_order_2(self):
        games = list()

        games.append(self._make_game("bos", "atl", "23.10"))
        games.append(self._make_game("nyk", "hou", "24.10"))
        games.append(self._make_game("bos", "phx", "25.10"))
        games.append(self._make_game("nyk", "mia", "26.10"))

        games_history = GamesHistory()
        teams = games_history.build_teams_history(games)
        games_planner = PastOnlyPlanner()
        teams_to_watch = games_planner.get_teams_to_watch(teams)

        assert teams_to_watch[0].team_code == "nyk"
        assert teams_to_watch[1].team_code == "bos"

    # TODO: this is failing, fix the logic for sorting.
    def test_two_teams_played_with_each_other_correct_order(self):
        games = list()

        # bos and nyk have each 2 games. They both played recently, but the previous game of nyk
        # was later than bos, so it was more recently watched.
        # Because of that bos should have priority to be watched now.
        games.append(self._make_game("bos", "atl", "23.10"))
        games.append(self._make_game("nyk", "hou", "24.10"))
        games.append(self._make_game("cle", "phx", "25.10"))
        games.append(self._make_game("nyk", "bos", "26.10"))

        games_history = GamesHistory()
        teams = games_history.build_teams_history(games)
        games_planner = PastOnlyPlanner()
        teams_to_watch = games_planner.get_teams_to_watch(teams)

        assert teams_to_watch[0].team_code == "nyk"
        assert teams_to_watch[1].team_code == "bos"
        

    @staticmethod
    def _make_game(home_team: str, away_team: str, date: str):
        split = date.split(".")
        game_date = GameDate(
            month=int(split[1]), day=int(split[0]), season_start_month=9
        )

        return {"home_team": home_team, "away_team": away_team, "game_date": game_date}

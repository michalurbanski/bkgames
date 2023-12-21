from bkgames.models import GameDate
from bkgames.gameshistory import GamesHistory


class TestGamesHistory:
    def test_add_game_results_in_two_teams_having_the_same_game_date(self):
        games_history = GamesHistory()
        home_team_name = "bos"
        away_team_name = "tor"
        game_date = GameDate(month=10, day=13, season_start_month=9)

        game_dictionary = self._make_game(home_team_name, away_team_name, game_date)
        games = list()
        games.append(game_dictionary)

        teams = games_history.build_teams_history(games)

        assert len(teams) == 2
        assert len(teams[0].games_dates) == 1
        assert len(teams[1].games_dates) == 1
        assert teams[0].games_dates[0] == teams[1].games_dates[0]

    def test_add_game_to_existing_team_should_have_two_game_dates(self):
        # First game
        games_history = GamesHistory()
        home_team = "bos"
        away_team = "tor"
        game_date = GameDate(month=10, day=13, season_start_month=9)
        game_dictionary = self._make_game(home_team, away_team, game_date)
        games = list()
        games.append(game_dictionary)

        # Add second game for the same home_team
        away_team = "phx"
        game_date = GameDate(month=10, day=15, season_start_month=9)
        game_dictionary = self._make_game(home_team, away_team, game_date)
        games.append(game_dictionary)

        teams = games_history.build_teams_history(games)

        # next() finds the first occurrence
        selected_team = next(team for team in teams if team.team_code == home_team)

        assert len(teams) == 3
        assert len(selected_team.games_dates) == 2

    @staticmethod
    def _make_game(home_team: str, away_team: str, game_date: GameDate):
        return {"home_team": home_team, "away_team": away_team, "game_date": game_date}

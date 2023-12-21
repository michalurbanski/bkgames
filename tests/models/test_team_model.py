from bkgames.models import TeamModel, GameDate


class TestTeamModel:
    def test_team_model_add_one_game(self):
        team_name = "bos"
        team_model = TeamModel(team_name)
        game_date = GameDate(month=3, day=13, season_start_month=9)
        team_model.add_game(game_date)

        assert team_model.team_code == team_name
        assert len(team_model.games_dates) == 1
        assert team_model.games_dates[0] == game_date

    def test_team_model_add_two_games(self):
        team_name = "bos"
        team_model = TeamModel(team_name)
        game_date_1 = GameDate(month=3, day=13, season_start_month=9)
        game_date_2 = GameDate(month=3, day=15, season_start_month=9)
        team_model.add_game(game_date_1)
        team_model.add_game(game_date_2)

        assert team_model.team_code == team_name
        assert len(team_model.games_dates) == 2
        assert team_model.games_dates[0] == game_date_1
        assert team_model.games_dates[1] == game_date_2

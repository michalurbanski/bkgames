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
    
    def test_team_model_teams_with_no_games_are_equal(self):
        home_team = "bos"
        away_team = "nyk"
        home_team_model = TeamModel(home_team)
        away_team_model = TeamModel(away_team)

        assert home_team_model == away_team_model

    def test_team_model_teams_with_different_number_of_games_are_not_equal(self):
        home_team = "bos"
        away_team = "nyk"
        home_team_model = TeamModel(home_team)
        away_team_model = TeamModel(away_team)
        game_date_1 = GameDate(month=3, day=15, season_start_month=9)
        home_team_model.add_game(game_date_1)

        assert home_team_model != away_team_model
    
    def test_team_model_the_one_played_earlier_is_less(self):
        first_team = "bos"
        second_team = "nyk"
        first_team_model = TeamModel(first_team)
        second_team_model = TeamModel(second_team)
        game_date_1 = GameDate(month=3, day=15, season_start_month=9)
        game_date_2 = GameDate(month=1, day=10, season_start_month=9)
        
        first_team_model.add_game(game_date_1)
        second_team_model.add_game(game_date_2)

        assert second_team_model < first_team_model

    # TODO: one more test for equal number of games, first the same date, but second game dates different

        

from bkgames.dataenhancers import NotYetPlayedEnhancer
from bkgames.models import TeamModel


class TestNotYetPlayedEnhancer:
    def test_enhance_data_unplayed_team_is_added_to_results(self):
        played_teams = [TeamModel("bos")]
        allowed_teams = ["bos", "tor"]

        enhancer = NotYetPlayedEnhancer()
        results = enhancer.enhance_data(played_teams, allowed_teams)

        assert len(results) == len(allowed_teams)
        assert any(team.team_code == "tor" for team in results)

    def test_enhance_data_all_teams_played_no_change_in_results(self):
        played_teams = [TeamModel("bos")]
        allowed_teams = ["bos"]

        enhancer = NotYetPlayedEnhancer()
        results = enhancer.enhance_data(played_teams, allowed_teams)

        assert len(results) == len(allowed_teams)
        assert results[0].team_code == "bos"
        assert results == played_teams

    # TODO: add negative test cases - empty lists + allowed teams collection smaller than played

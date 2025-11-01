from bkgames.dataenhancers import SkipTeamsEnhancer
from bkgames.models import TeamModel


class TestSkipTeamsEnhancer:
    def test_enhance_data_skip_teams_empty_no_teams_skipped(self):
        played_teams = [TeamModel("bos")]
        skipped_teams = []

        enhancer = SkipTeamsEnhancer()
        results = enhancer.enhance_data(played_teams, skipped_teams)

        assert len(results) == len(played_teams)

    def test_enhance_data_skip_all_teams_all_skipped(self):
        played_teams = [TeamModel("bos")]
        skipped_teams = ["bos"]

        enhancer = SkipTeamsEnhancer()
        results = enhancer.enhance_data(played_teams, skipped_teams)

        assert len(results) == len(played_teams)
        assert all(team.skip_from_watching for team in results)

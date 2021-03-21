from typing import List


class TeamsValidator:
    """ Checks if team code is valid, based on configuration list """

    def __init__(self, valid_team_codes: List[str]):
        """ valid_team_codes - List of valid team codes """
        self._valid_team_codes = valid_team_codes

    def validate(self, previous_parsing_result: dict) -> (bool, dict):
        """ previous_parsing_result is a dictionary as follows

        {
            'home_team',
            'away_team',
            'date',
            'line'

        }
        """

        teams = [previous_parsing_result["home_team"],
                 previous_parsing_result["away_team"]]

        invalid_teams = self._validate_teams(teams)

        if invalid_teams:
            return (False, {
                "not_parsed": previous_parsing_result["line"],
                "error": "Incorrect team codes found: {}".format(invalid_teams)
            })
        else:
            return (True, previous_parsing_result)

    def _validate_teams(self, teams: list) -> list:
        invalid_teams = []

        for team in teams:
            valid_team = [True for team_code in self._valid_team_codes
                          if TeamsValidator._is_team_codes_match(team, team_code)]
            if not valid_team:
                invalid_teams.append(team)

        return invalid_teams

    @staticmethod
    def _is_team_codes_match(first: str, second: str) -> bool:
        return first.upper() == second.upper()

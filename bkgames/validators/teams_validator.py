from typing import List
from .validation_result import ValidationResult, InvalidResult, ValidResult


class TeamsValidator:
    """Checks if team code is valid, based on passed configuration list."""

    def __init__(self, valid_team_codes: List[str]):
        """
        Args:
            valid_team_codes: List of valid team codes
        """
        self._valid_team_codes = valid_team_codes

    def validate(self, input: str, home_team: str, away_team: str) -> ValidationResult:
        """Line that was parsed correctly may not pass validator check.
        In that case it becomes a NotParsedLine.
        """

        teams = [home_team, away_team]

        invalid_teams = self._get_invalid_teams(teams)

        if invalid_teams:
            return InvalidResult(
                input=input,
                message="Incorrect team codes found: {}".format(invalid_teams),
            )

        return ValidResult(
            input=input,
            message="",
        )

    def _get_invalid_teams(self, teams: list) -> list:
        invalid_teams = []

        for team in teams:
            valid_team = [
                True
                for team_code in self._valid_team_codes
                if TeamsValidator._is_team_codes_match(team, team_code)
            ]
            if not valid_team:
                invalid_teams.append(team)

        return invalid_teams

    @staticmethod
    def _is_team_codes_match(first: str, second: str) -> bool:
        if first is None or second is None:
            return False

        return first.strip().casefold() == second.strip().casefold()

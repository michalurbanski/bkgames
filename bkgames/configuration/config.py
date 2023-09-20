from typing import List


class Config:
    def __init__(self):
        pass

    @property
    def data_file_regexp(self) -> str:
        return self._data_file_regexp

    @data_file_regexp.setter
    def data_file_regexp(self, regexp: str) -> None:
        self._data_file_regexp = regexp

    @property
    def season_year(self) -> int:
        return self._season_year

    @season_year.setter
    def season_year(self, year) -> None:
        self._season_year = year

    @property
    def allowed_teams(self) -> List[str]:
        return self._allowed_teams

    @allowed_teams.setter
    def allowed_teams(self, teams: List[str]) -> None:
        self._allowed_teams = teams

    @property
    def season_start_month(self) -> int:
        return self._season_start_month

    @season_start_month.setter
    def season_start_month(self, month: int) -> None:
        self._season_start_month = month

    @property
    def skipped_teams(self) -> List[str]:
        return self._skipped_teams

    @skipped_teams.setter
    def skipped_teams(self, teams: List[str]) -> None:
        self._skipped_teams = teams

from bkgames.validators import (
    ValidationResult,
    ValidResult,
    InvalidResult,
    TeamsValidator,
)


class TestTeamsValidator:
    def test_valid_teams_valid_result(self):
        valid_teams = ["okc", "hou"]
        input = "25.11 okc at hou"
        teams_validator = TeamsValidator(valid_teams)

        result = teams_validator.validate(input, valid_teams[0], valid_teams[-1])

        assert isinstance(result, ValidationResult)
        assert isinstance(result, ValidResult)
        assert result.is_valid == True
        assert result.input == input

    def test_one_invalid_team_invalid_result(self):
        valid_teams = ["okc", "hou"]
        input = "25.11 okc at bos"
        teams_validator = TeamsValidator(valid_teams)

        result = teams_validator.validate(input, valid_teams[0], "bos")

        assert isinstance(result, ValidationResult)
        assert isinstance(result, InvalidResult)
        assert result.is_valid == False
        assert result.input == input
        assert "bos" in result.message  # only bos is invalid, okc is valid

    def test_both_invalid_teams_invalid_result(self):
        valid_teams = ["okc", "hou"]
        input = "25.11 bos at nyk"
        teams_validator = TeamsValidator(valid_teams)

        result = teams_validator.validate(input, "bos", "nyk")

        assert isinstance(result, ValidationResult)
        assert isinstance(result, InvalidResult)
        assert result.is_valid == False
        assert result.input == input
        assert all(word in result.message for word in ["nyk", "bos"])

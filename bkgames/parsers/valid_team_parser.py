class ValidTeamParser:
    """ Checks if team code is valid, based on configuration list """
    
    def __init__(self, valid_team_codes):
        """ valid_teams - array of valid team codes """
        self._valid_team_codes = valid_team_codes

    def parse(self, previous_parsing_result):
        """ previous_parsing_result is a dictionary as follows
        {
            'home_team',
            'away_team',
            'date',
            'line'
        }
        """

        teams = [previous_parsing_result["home_team"], previous_parsing_result["away_team"]]

        invalid_teams = []

        for team in teams:
            valid_team = [True for team_code in self._valid_team_codes
                            if ValidTeamParser._is_team_codes_match(team, team_code)]
            if not valid_team:
                invalid_teams.append(team)

        if invalid_teams:
            return (False, {
                "not_parsed": previous_parsing_result["line"],
                "error": "Incorrect team codes found: {}".format(invalid_teams)
            })
        else:
            return (True, previous_parsing_result)


    @staticmethod
    def _is_team_codes_match(first, second):
        return first.upper() == second.upper()

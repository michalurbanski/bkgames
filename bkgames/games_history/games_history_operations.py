class GamesHistoryOperations:
    
    @staticmethod
    def order_by_games_played(team_frequency):
        # TODO: add docstring
        # Team with the most games played is at the top
        results = list()
        
        for entry in team_frequency.items():
            results.append((entry[0], len(entry[1]), entry[1]))

        return sorted(results, key = lambda x: x[1], reverse = True)

    @staticmethod
    def order_by_oldest_games(team_frequency):
        """
        Returns list of tuples ("team_name", date_of_the_most_recent_game)
        Results are sorted by the oldest game played among all the teams
        """
        
        results = list()

        for entry in team_frequency.items():
            games_dates = entry[1]
            sorted_by_oldest = sorted(games_dates, reverse = True)
            first_oldest_game_by_the_team = sorted_by_oldest[0]
            results.append((entry[0], first_oldest_game_by_the_team))

        return sorted(results, key = lambda x: x[1], reverse = True)

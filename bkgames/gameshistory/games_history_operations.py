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
    def order_by_most_recent_games(team_frequency):
        """
        Returns list of tuples ("team_name", date_of_the_most_recent_game)
        Results are sorted by the most recent game played among all the teams
        
        In input (read from file) games are in chronogical order, so it's sufficient
        to take the first element of games collection.
        """
        
        results = list()

        for entry in team_frequency.items():
            games_dates = entry[1]
            date_of_the_most_recent_game = GamesHistoryOperations._get_most_recent_game(games_dates)          
            results.append((entry[0], date_of_the_most_recent_game))

        return sorted(results, key = lambda x: x[1], reverse = True)

    @staticmethod
    def _get_most_recent_game(games):
        return games[-1]

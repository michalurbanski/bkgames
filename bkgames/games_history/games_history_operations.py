class GamesHistoryOperations:
    
    @staticmethod
    def order_by_games_played(team_frequency):
        # TODO: add docstring
        results = list()
        
        for entry in team_frequency.items():
            results.append((entry[0], len(entry[1]), entry[1]))

        return sorted(results, key = lambda x: x[1], reverse = True)

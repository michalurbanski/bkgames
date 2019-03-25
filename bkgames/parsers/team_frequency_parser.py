from datetime import datetime

class TeamFrequencyParser:
    
    @staticmethod
    def Parse(line):
        return {
                "home_team": "phi", 
                "away_team": "bos",
                "date": datetime(2018, 10, 16)
                }

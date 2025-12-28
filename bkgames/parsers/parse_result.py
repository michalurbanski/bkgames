from dataclasses import dataclass
from bkgames.models import GameDate


@dataclass
class ParsedLine:
    home_team: str
    away_team: str
    game_date: GameDate
    raw_line: str


@dataclass
class NotParsedLine:
    raw_line: str
    error: Exception
    traceback: str

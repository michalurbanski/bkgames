from typing import List
from pydantic import BaseModel

class Config(BaseModel):
    data_file_regexp: str
    allowed_teams: List[str]
    season_start_month: int
    skipped_teams: List[str]

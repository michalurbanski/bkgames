from typing import List
from pydantic import BaseModel, Field


# ! default_factory is needed, because of python behavior that default arguments of a function are shared between instances.
# ! See also: https://www.pythonmorsels.com/mutable-default-arguments/
class Config(BaseModel):
    data_file_regexp: str
    season_start_month: int
    allowed_teams: List[str] = Field(default_factory=list)
    skipped_teams: List[str] = Field(default_factory=list)

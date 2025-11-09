from typing import Protocol, List
from bkgames.models import TeamModel


class EnhancerProtocol(Protocol):
    def enhance_data(self, input: List[TeamModel]):
        pass

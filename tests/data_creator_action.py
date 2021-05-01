from typing import Callable


class DataCreatorAction:
    def __init__(self, func: Callable, priority_for_creation: int = 99, priority_for_removal: int = 99):
        self.func = func
        self.priority_for_creation = priority_for_creation
        self.priority_for_removal = priority_for_removal

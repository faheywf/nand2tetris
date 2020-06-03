import attr
from abc import ABC, abstractmethod

@attr.s()
class Chip(ABC):
    @abstractmethod
    def run_cycle(self, *args, **kwargs):
        pass
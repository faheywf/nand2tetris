import attr

from src.chip import Chip

class Nand(Chip):
    def run_cycle(self, a: bool, b: bool) -> bool:
        return not (a and b)


@attr.s(auto_attribs=True)
class Not(Chip):
    nand = Nand()

    def run_cycle(self, a: bool) -> bool:
        return self.nand.run_cycle(a, True)

@attr.s(auto_attribs=True)
class And(Chip):
    nand = Nand()
    _not = Not()

    def run_cycle(self, a: bool, b: bool) -> bool:
        return self._not.run_cycle(self.nand.run_cycle(a, b))

@attr.s(auto_attribs=True)
class Or(Chip):
    nand = Nand()
    _not = Not()

    def run_cycle(self, a: bool, b: bool) -> bool:
        return self.nand.run_cycle(self._not.run_cycle(a), self._not.run_cycle(b))

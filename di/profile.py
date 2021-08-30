from dataclasses import dataclass
from typing import Set


@dataclass(init=True, frozen=True)
class Profile:
    values: Set[str]

    def match(self, actives: Set[str]) -> bool:
        return all([name in actives for name in self.values])

    def __hash__(self):
        return hash(str(sorted([name for name in self.values])))

    def __eq__(self, other):
        if (other is None) or (not isinstance(other, Profile)):
            return False
        return self.values == other.values

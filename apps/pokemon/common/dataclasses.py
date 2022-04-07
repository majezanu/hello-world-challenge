from dataclasses import dataclass
from typing import Optional


@dataclass
class Specie:
    name: str
    url: str


@dataclass
class Pokemon:
    id: int
    name: str
    height: int
    specie: Optional[Specie] = None

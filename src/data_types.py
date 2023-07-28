"""
File containing all the types
"""

from typing import TypeVar

Human = TypeVar('Human')
Vampire = TypeVar('Vampire')
Edible = TypeVar('Edible')

MAP_TYPE = list[list[Human | Vampire | Edible | None]]
OBJ_LIST_TYPE = list[Human | Vampire | Edible]
POSITION_TYPE = list[int, int]
HUMAN_OR_VAMPIRE_TYPE = [Human | Vampire]

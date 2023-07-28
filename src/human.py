from random import randrange
from moveable import Moveable
from data_types import POSITION_TYPE
from constants import MIN_HUMAN_AGE, MAX_HUMAN_AGE


class Human(Moveable):

    """
    Human class that implements all human related features

    Attributes:
        max_move_steps: Maximum number of moves that human can take in any direction
        color: Color that will be used to represent human on the map
        label: Label to be used on the graph for human
        marker: Marker that will be used to represent human on the map
    """

    max_move_steps = 4
    marker = "o"
    color = "brown"
    label = "Human"

    def __init__(self, position: POSITION_TYPE):
        """
        Initializes and object of class Human

        Args:
            position: Position of the human on the map
        """
        self.health = 100
        self.position = position
        self.age = randrange(MIN_HUMAN_AGE, MAX_HUMAN_AGE + 1)

    def move(self, new_position: POSITION_TYPE) -> None:
        """
        Move the human to the new position

        Args:
            new_position: New position to move to
        """
        self.age += 1
        self.health -= 1
        self.position = new_position

    @property
    def is_dead(self) -> bool:
        """
        Whether human alive or dead

        Returns:
            bool: Is human dead
        """
        return self.health < 1

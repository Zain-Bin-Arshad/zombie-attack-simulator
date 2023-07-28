from data_types import POSITION_TYPE
from moveable import Moveable


class Vampire(Moveable):
    """
    Represents an object of type Vampire

    Attributes:
        color: Color that will be used to represent vampire on the map
        label: Label to be used on the graph for vampire
        marker: Marker that will be used to represent vampire on the map
        max_move_steps: Maximum number of steps that a vampire can take in any direction
        default_health: The initial health of a firstly created vampire
    """

    max_move_steps = 8
    marker = "^"
    color = "red"
    label = "Vampire"
    default_health = 50

    def __init__(self, position: POSITION_TYPE, health=None):
        """
        Initializes and object of class Vampire

        Args:
            position: Position of the vampire on the map
            health: Health of the vampire
        """
        self.position = position
        self.health = health or self.default_health  # Vampires had to have health if they are the first ones

    def move(self, new_position: POSITION_TYPE) -> None:
        """
        Move the vampire to the new position

        Args:
            new_position: New position to move to
        """
        self.health -= 1
        self.position = new_position

    @property
    def is_dead(self) -> bool:
        """
        Whether a vampire is alive or dead

        Returns:
            bool: Is vampire dead
        """
        return self.health < 1

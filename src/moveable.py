from random import choice
from abc import ABC, abstractmethod
from data_types import POSITION_TYPE
from constants import MAP_SIZE_MAX_X, MAP_SIZE_MAX_Y, DIRECTIONS


def convert_to_valid_position(new_position: POSITION_TYPE) -> POSITION_TYPE:
    """Return the position after making sure that it's not outside the map

    Args:
        new_position (list): New position that human is trying to take

    Returns:
        list: valid new position that is inside the premises of the map
    """
    map_size = [MAP_SIZE_MAX_X, MAP_SIZE_MAX_Y]
    for i in [0, 1]:
        if new_position[i] < 0:
            new_position[i] = 0
        elif new_position[i] >= map_size[i]:
            new_position[i] = map_size[i] - 1
    return new_position


class Moveable(ABC):
    """
    Movaeable interface that defines the moving abilities of Humans and Vampires
    """
    @abstractmethod
    def is_dead(self) -> bool:
        ...

    @abstractmethod
    def move(self, new_position: POSITION_TYPE) -> None:
        ...

    def get_new_position(self, exclude_directions: list[str]) -> list[str, POSITION_TYPE]:
        """
        Get the new position of human

        Args:
            exclude_directions: Directions that a human can't move to,
            because he/she has already tried to move in that direction

        Returns:
            list: Direction and new position that human is trying to move to
        """
        new_position = self.position

        # exclude directions where human has already tried to move
        direction = choice(list(set(DIRECTIONS) - set(exclude_directions)))
        if direction == "left":
            new_position[0] = self.position[0] - self.max_move_steps
        elif direction == "right":
            new_position[0] = self.position[0] + self.max_move_steps
        elif direction == "up":
            new_position[1] = self.position[1] + self.max_move_steps
        elif direction == "down":
            new_position[1] = self.position[1] - self.max_move_steps
        return [direction, convert_to_valid_position(new_position)]

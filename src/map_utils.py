from human import Human
from edible import Edible
from vampire import Vampire
from random import randrange, choice, choices
from constants import MAP_SIZE_MAX_X, MAP_SIZE_MAX_Y, EDIBLES_DATA
from data_types import MAP_TYPE, POSITION_TYPE, HUMAN_OR_VAMPIRE_TYPE, OBJ_LIST_TYPE


def get_neighbors(map_obj: MAP_TYPE, obj: HUMAN_OR_VAMPIRE_TYPE) -> list[HUMAN_OR_VAMPIRE_TYPE]:
    """
    Get neighbors of a Human/Vampire in the map

    Args:
        map_obj: Map an object that holds humans, vampires and food
        obj: Human or Vampire object to find neighbors of

    Returns:
        list: neighbors of the Human/Vampire
    """
    # thanks to this question on stack overflow
    # https://stackoverflow.com/questions/652106/finding-neighbors-in-a-two-dimensional-array
    neighbors = []
    for i in range(max(0, obj.position[0] - 1), min(MAP_SIZE_MAX_X, obj.position[0] + 2)):
        for j in range(max(0, obj.position[1] - 1), min(MAP_SIZE_MAX_Y, obj.position[1] + 2)):
            if obj.position != [i, j]:
                neighbors.append(map_obj[i][j])
    return neighbors


def replace_map_position(map_obj: MAP_TYPE, obj: HUMAN_OR_VAMPIRE_TYPE, other_obj=None) -> None:
    """
    Replace the map position with a given object or makes it None

    Args:
        map_obj: Map object that holds humans, vampires and food
        obj: Object to be replaced
        other_obj: Second object to be replaced in place of first
    """
    map_obj[obj.position[0]][obj.position[1]] = other_obj


def get_random_object(obj_first: HUMAN_OR_VAMPIRE_TYPE, obj_second: HUMAN_OR_VAMPIRE_TYPE) -> HUMAN_OR_VAMPIRE_TYPE:
    """
    Choose a random object from the list of objects

    Args:
        obj_first: A vampire or human object
        obj_second: A vampire or human object

    Returns:
        Human/Vampire: A randomly chosen vampire or human object
    """
    return choice([obj_first, obj_second])


def get_weighted_choice(weights: list[int]) -> str:
    """
    Get the choice, according to the weights given for respective choice
    positive represents a positive outcome, like, human helping each other
    negative represents a negative outcome, like, vampire biting a human

    Args:
        weights (list): Chance of each outcome

    Returns:
        str: Negative or positive outcome
    """
    return choices(["positive", "negative"], weights=weights)[0]


def create_obj_on_map(obj_type: OBJ_LIST_TYPE, map_obj: MAP_TYPE, total_objs: int | None = None) -> OBJ_LIST_TYPE:
    """
    Populate a map with humans, vampires and food
    Args:
        obj_type: Human or Vampire or Edible
        map_obj: Map object that holds humans, vampires and food
        total_objs: Total number of objects to be created

    Returns:
        objects: List of created objects on the map
    """
    objects = []
    if obj_type is Human:
        objects = [Human(get_random_position(map_obj)) for _ in range(total_objs)]
    elif obj_type is Vampire:
        objects = [Vampire(get_random_position(map_obj)) for _ in range(total_objs)]
    elif obj_type is Edible:
        objects = [
            Edible(edible_type, get_random_position(map_obj), edible_data)
            for edible_type, edible_data in EDIBLES_DATA.items()
        ]
    populate_map(map_obj, objects)
    return objects


def populate_map(map_obj: MAP_TYPE, objects: OBJ_LIST_TYPE) -> None:
    """
    Populate given a list of objects on map
    Args:
        map_obj: Map object that holds humans, vampires and food
        objects: List of objects to be added to the map
    """
    for obj in objects:
        map_obj[obj.position[0]][obj.position[1]] = obj


def is_position_valid(map_obj: MAP_TYPE, new_position: POSITION_TYPE) -> bool:
    """
    Checks if the position that object is trying to make is valid or not

    Args:
        map_obj: Map object that holds humans, vampires and food
        new_position: New position submitted by the Human/Vampire

    Returns:
        bool: Is the new position valid or not
    """
    return map_obj[new_position[0]][new_position[1]] is None


def get_random_position(map_obj: MAP_TYPE) -> POSITION_TYPE:
    """
    Get a random empty position in the map

    Args:
        map_obj: Map object that holds humans, vampires and food

    Returns:
        list: X and Y coordinates of an object on the map
    """
    while True:
        position = [randrange(1, MAP_SIZE_MAX_X - 1), randrange(1, MAP_SIZE_MAX_Y - 1)]
        if is_position_valid(map_obj, position):
            break
    return position

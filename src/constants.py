"""
File containing all the constants
"""

MAP_SIZE_MAX_X: int = 20
MAP_SIZE_MAX_Y: int = 20
MIN_HUMAN_AGE: int = 10
MAX_HUMAN_AGE: int = 50

SWEEP_MODE_ARG: str = "s"
RESULTS_DIR: str = "./Simulation Results"
CSV_FILE_PATH: str = f"{RESULTS_DIR}/results.csv"

DIRECTIONS: list[str] = ["left", "right", "up", "down"]
INITIAL_DATA: list[int] = [
    20,  # Default total number of humans
    5,  # Default total number of vampires
    50,  # Default total number of timestamps
]

HUMAN_INTERACTION_WEIGHT: list[int] = [
    60,  # 60% that human will help
    40,  # 40% that human will gain all health
]
HUMAN_VAMPIRE_INTERACTION_WEIGHT: list[int] = [
    30,  # 30% vampire gets killed
    70,  # 70% human becomes vampire
]

EDIBLES_DATA: dict[str, dict[str, str | int]] = {
    "food": {"marker": "X", "color": "orange", "health_capacity": 30},
    "water": {"marker": "D", "color": "blue", "health_capacity": 50},
    "garlic": {"marker": "*", "color": "black", "health_capacity": 100},
}

SWEEP_MODE_PARAMS: dict[str, int] = {
    'timestamps': 30,
    'min_humans': 10,
    'max_humans': 40,
    'min_vampires': 1,
    'max_vampires': 5,
}

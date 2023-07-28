from pathlib import Path
from constants import RESULTS_DIR


def log_data_to_csv(results: list[dict[str, int]], file_path: str) -> None:
    """
    Logs the result of sweep mode into a CSV file

    Args:
        results: Data of the simulation like final and initials humans and vampires
        file_path: Filepath to log data into
    """
    with open(file_path, "w") as log_file:
        log_file.write("Sweep No,Initial Humans,Remaining Humans,Initial Vampires,Remaining Vampires\n")
        for result in results:
            log_file.write(f"{result['sweep_count']},{result['initial_humans']},{result['initial_vampires']},\
            {result['remaining_humans']},{result['remaining_vampires']}\n")
            #log_file.write(f"{','.join(list(map(lambda attr: str(result[attr]), data_attrs)))}\n")


def print_info(msg: str) -> None:
    """
    Prints info log
    Args:
        msg: Message to be printed
    """
    stars = "*" * (len(msg) + 4)
    print(f"\n{stars}\n| {msg} |\n{stars}\n")


def print_error(msg: str) -> None:
    """
    Prints error log
    Args:
        msg: Message to be printed
    """
    stars = "X" * (len(msg) + 4)
    print(f"\n{stars}\n| {msg} |\n{stars}\n")


def mkdir_for_results() -> None:
    """Create a directory to save simulation results in"""
    Path(RESULTS_DIR).mkdir(exist_ok=True)

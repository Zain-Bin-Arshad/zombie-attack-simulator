from sys import argv
from simulation import Simulation
from logger import print_info, log_data_to_csv, mkdir_for_results
from constants import CSV_FILE_PATH, SWEEP_MODE_PARAMS, SWEEP_MODE_ARG, INITIAL_DATA


def is_sweep_mode() -> bool:
    """
    Check if user is trying to run the simulation in sweep mode

    Returns:
        bool: If sweep mode enabled or disabled
    """
    try:
        return argv[1] == SWEEP_MODE_ARG
    except IndexError:
        return False


def get_simulation_parameters() -> tuple:
    """
    Validates the user input and return. Fallback to the default values in case of error

    Returns:
        tuple: total_humans, total_vampires, timestamps
    """
    try:
        total_humans, total_vampires, timestamps = map(lambda x: int(argv[x]), list(range(1, 4)))
    except (ValueError, IndexError):
        total_humans, total_vampires, timestamps = INITIAL_DATA

    return total_humans, total_vampires, timestamps


def execute_sweep_mode():
    """
    Executes simulation in sweep mode
    """
    sweep_count, results = 0, []
    for humans_count in range(SWEEP_MODE_PARAMS['min_humans'], SWEEP_MODE_PARAMS['max_humans'] + 1):
        for vampires_count in range(SWEEP_MODE_PARAMS['min_vampires'], SWEEP_MODE_PARAMS['max_vampires'] + 1):
            sweep_count += 1
            print_info(f"Executing Sweep # {sweep_count} | Humans # {humans_count} | Vampires # {vampires_count}")
            simulation = Simulation(humans_count, vampires_count, SWEEP_MODE_PARAMS['timestamps'], sweep_count)
            simulation.run()
            results.append({
                "sweep_count": sweep_count,
                "initial_humans": humans_count,
                "initial_vampires": vampires_count,
                "remaining_humans": len(simulation.humans),
                "remaining_vampires": len(simulation.vampires),
            })
            print_info("Done!")
    log_data_to_csv(results, CSV_FILE_PATH)


def main():
    """
    Execute simulation as give by user
    """
    mkdir_for_results()
    if is_sweep_mode():
        execute_sweep_mode()
    else:
        total_humans, total_vampires, timestamps = get_simulation_parameters()
        simulation = Simulation(total_humans, total_vampires, timestamps)
        simulation.run()


if __name__ == "__main__":
    # Entry point of the program
    main()

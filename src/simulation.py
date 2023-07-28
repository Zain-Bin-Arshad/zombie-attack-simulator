from map_utils import *
from human import Human
from edible import Edible
from random import shuffle
from vampire import Vampire
from logger import print_info, print_error
import matplotlib.pyplot as plt
from constants import HUMAN_INTERACTION_WEIGHT, HUMAN_VAMPIRE_INTERACTION_WEIGHT, RESULTS_DIR


class Simulation:
    """
    Responsible for running simulation, plotting and saving graphs
    """
    def __init__(self, total_humans: int, total_vampires: int, timestamps: int, sweep_count: int = 0) -> None:
        """
        Initializes an object of class Simulation

        Args:
            total_humans: Initial number of humans
            total_vampires: Initial number of vampires
            timestamps: Number of steps the simulation will run for
            sweep_count: Current sweep count
        """
        self.timestamps: int = timestamps
        self.sweep_count: int = sweep_count
        self.total_humans: int = total_humans
        self.total_vampires: int = total_vampires
        self.map: MAP_TYPE = [[None] * MAP_SIZE_MAX_Y for _ in range(MAP_SIZE_MAX_X)]
        self.humans: list[Human] = create_obj_on_map(Human, self.map, total_humans)
        self.vampires: list[Vampire] = create_obj_on_map(Vampire, self.map, total_vampires)
        self.edibles: list[Edible] = create_obj_on_map(Edible, self.map)

    def plot_moving_objects_data(self, obj: HUMAN_OR_VAMPIRE_TYPE) -> None:
        """
        Plots Human or Vampire data as Scatter plot on the graph

        Args:
            obj: Object to plot on the graph
        """

        x_values, y_values = [], []
        objects = self.humans if obj is Human else self.vampires

        for obj in objects:
            x, y = obj.position
            x_values.append(x)
            y_values.append(y)
            plt.annotate(f"({x}, {y})", (x, y), fontsize=7)
        plt.scatter(x_values, y_values, marker=obj.marker, color=obj.color, label=obj.label)

    def plot_edibles_data(self) -> None:
        """
        Plots objects of Edible class on the graph
        """
        for edible in self.edibles:
            x, y = edible.position
            plt.annotate(edible.label, (x, y), fontsize=7)
            plt.scatter([x], [y], marker=edible.marker, color=edible.color)

    def display_and_save_graph(self, timestep: int) -> None:
        """
        Display graph to user and saves as a PNG file

        Args:
            timestep (int): Current time step
        """
        if self.sweep_count:
            plt.savefig(f"{RESULTS_DIR}/sweep_{self.sweep_count}_h_{self.total_humans}_v_{self.total_vampires}.png")
        else:
            plt.pause(1)
            plt.savefig(f"{RESULTS_DIR}/Timestep_{timestep}.png")
        plt.clf()

    def plot_graph(self, timestep: int) -> None:
        """
        Plot graph for displaying and saving later on

        Args:
            timestep (int): Current time step
        """
        plt.xlim(0, MAP_SIZE_MAX_X)
        plt.ylim(0, MAP_SIZE_MAX_Y)

        # if not in sweep mode or this is the last timestamp of sweep mode
        if not self.sweep_count or timestep == self.timestamps:
            if self.sweep_count:
                title = f"Timestep#{timestep} | Humans#{self.total_humans} | Vampires#{self.total_vampires}"
            else:
                title = f"Timestep # {timestep}"
            plt.title(title)
            self.plot_moving_objects_data(Human)
            self.plot_moving_objects_data(Vampire)
            self.plot_edibles_data()
            self.display_and_save_graph(timestep)

    def move_objects(self) -> None:
        """
        Start moving the objects around the graph
        """
        for moving_objects in [self.humans, self.vampires]:
            for moving_object in moving_objects:
                """
                'Position Finding Algorithm'
                - Object will select a random new position on the map
                - Object will return the new direction and position i.e. ["up", [4, 21]]
                - New position will be validated
                - If it is not valid then we will ask the object for another position
                - But this time we will tell him not to go i.e. "up" as it is not valid
                - If object has exhausted all of the 4 directions we will break the loop and won't move the object
                """
                exclude_directions = []
                while True:
                    direction, new_position = moving_object.get_new_position(exclude_directions)
                    exclude_directions.append(direction)
                    if is_position_valid(self.map, new_position) or len(set(exclude_directions)) == 4:
                        break

                # only update if an object is able to move
                if is_position_valid(self.map, new_position):
                    replace_map_position(self.map, moving_object)  # leave old position
                    moving_object.move(new_position)  # move, age and lose health
                    replace_map_position(self.map, moving_object, moving_object)  # occupy new position

    def vampire_vampire_interaction(self, first_vampire: Vampire, second_vampire: Vampire) -> None:
        """
        Start interaction of vampire with another vampire

        Args:
            first_vampire: First Vampire
            second_vampire: Second Vampire
        """
        first_vampire.health -= 20
        second_vampire.health -= 20
        print_info("Vampires just bit each other")

        # Filter out the dead vampires and remove them from the map
        for vampire in filter(lambda v: v.is_dead, [first_vampire, second_vampire]):
            if vampire in self.vampires:
                self.vampires.remove(vampire)
                replace_map_position(self.map, vampire)
                print_info("Vampire just got killed by another vampire")

    def execute_vampire_interactions(self) -> None:
        """
        Loops through all vampires and execute their interactions
        """
        vampires_list = self.vampires[:]  # copying as this list might get updated
        for vampire in vampires_list:
            # checks if vampire is still alive to interact
            if not vampire.is_dead:
                for neighbour in get_neighbors(self.map, vampire):
                    # vampire_human interaction is already taken care of in
                    # humans' interactions, and vampire doesn't interact with the food
                    # hence we will only consider vampire_vampire interaction
                    if neighbour is Vampire:
                        self.vampire_vampire_interaction(vampire, neighbour)

    def human_human_interaction(self, first_human: Human, second_human: Human) -> None:
        """
        Start interaction of human with another human

        Args:
            first_human: First Human
            second_human: Second Human
        """
        if get_weighted_choice(HUMAN_INTERACTION_WEIGHT) == "positive":  # human helped each other
            first_human.health += 10
            second_human.health += 10
            print_info("Humans helped each other and gained 10% health")
        else:  # one human got greedy and obtains 20 health
            interacting_objs = [first_human, second_human]
            shuffle(interacting_objs)
            gain_obj, lose_obj = interacting_objs
            gain_obj.health += 20
            lose_obj.health -= 20
            if lose_obj.is_dead:
                if lose_obj in self.humans:
                    self.humans.remove(lose_obj)
                    replace_map_position(self.map, lose_obj)
                    print_info("Human just got killed by another human")
            print_info("Human got greedy and obtained 20% health")

    def human_vampire_interaction(self, human: Human, vampire: Vampire) -> None:
        """
        Start interaction of human with vampire

        Args:
            human: Human object that will interact with a vampire
            vampire: Vampire object that will interact with a human
        """
        if get_weighted_choice(HUMAN_VAMPIRE_INTERACTION_WEIGHT) == "positive":  # human kills vampire
            self.vampires.remove(vampire)
            replace_map_position(self.map, vampire)
            print_info("Vampire got killed by a human")
        else:  # vampire bit human
            self.humans.remove(human)
            vampire = Vampire(human.position, human.health)
            self.vampires.append(vampire)
            replace_map_position(self.map, vampire, vampire)
            print_info("Human got bit and turned into vampire")

    def human_food_interaction(self, human: Human, food: Edible) -> None:
        """
        Starts interaction of human with food

        Args:
            human: Human object that will interact with the food
            food: Edible object
        """
        human.health += food.health_increase_capacity
        print_info(f"Human just {'drunk' if food.edible_type == 'water' else 'ate'} {food.edible_type}")

    def execute_human_interactions(self) -> None:
        """
        Loops through all humans and executes their interactions
        """
        humans_list = self.humans[:]  # copy since this list might get updated in the loop
        interaction_methods = {
            Human: self.human_human_interaction,
            Vampire: self.human_vampire_interaction,
            Edible: self.human_food_interaction,
        }
        for human in humans_list:
            for neighbor in get_neighbors(self.map, human):
                if neighbor and not human.is_dead and neighbor.is_dead:  # neighbor and human should be alive
                    interaction_methods[type(neighbor)](human, neighbor)

    def kill_all_humans(self) -> None:
        """
        Kill all humans as they can't live past 70 timestamps
        """
        for human in self.humans:
            human.health = 0
            replace_map_position(self.map, human)

        self.humans = []
        print_info("All humans died")

    def run(self) -> None:
        """
        Executes the simulation with one timestep at a time
        """
        try:
            for timestep in range(1, self.timestamps + 1):
                if timestep > 70 and self.humans:
                    self.kill_all_humans()  # humans can't live pass 70 timestamps

                print_info(f"Timestep # {timestep}")
                self.plot_graph(timestep)
                self.execute_human_interactions()
                self.execute_vampire_interactions()
                self.move_objects()
        except Exception as e:
            print_error(f"Something is not quite right...\n{e}")

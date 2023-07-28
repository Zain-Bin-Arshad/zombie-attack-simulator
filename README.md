# zombie-attack-simulator

So, after binging on "World War Z 🧟‍♂️", it hit me like a zombie apocalypse idea:

- Imagine if the scientists called me instead of Brad Pitt to save the world with simulations!
- I thought, why not create a simulation, making it useful and entertaining?
- Let's plot the crazy results on a graph, so we can have some fun visuals and even save them in a CSV file!
- But beware, the zombies might not be thrilled about this simulation invasion!
<p align="center">
  <img src="https://github.com/Zain-Bin-Arshad/zombie-attack-simulator/assets/49767636/8092f1fe-a1ee-43a9-9a6a-d01dad4e4bef" width="200">
</p>

## Demo
<p align="center">
  <img src="https://github.com/Zain-Bin-Arshad/zombie-attack-simulator/assets/49767636/8f4e17c4-8592-4274-874e-a053bf82581c" width="500">
</p>

## Assumptions
I formulated some guidelines before implementing this simulation.
### General
- We will have Humans, Vampires, Water, Garlic, and Food on a 2D map
- Humans and vampires will move with each `timestamp` and interact with each other
- Humans can live past 70 timestamps and will get killed
- Starting health of a human will be 100 and that of a zombie will be 50
- Most of the parameters can be modified inside `constants.py` file, i.e. how many steps they can take at a time
<p align="center">
<img width="104" alt="image" src="https://github.com/Zain-Bin-Arshad/zombie-attack-simulator/assets/49767636/8e4c15ac-7eac-4483-9b3b-c8e04ae8ea83">
</p>

### Interactions
- If humans interact, there is a 40% chance that they will help each other and a 60% that one of them will kill the other for health
- If humans interact with edibles, their health increases by water 50, food 30, and garlic  100
- If humans interact with vampires, there is a 70% chance that the human will become a vampire and  a 30% chance that the vampire will get killed
- If vampires interact with each other, both of them will lose 20 health

## Execution
Ensure that you have `python3` and `pip` installed. For ease of use, I am managing the execution via Makefile, however, you can run the program directly as well. Navigate to the code directory:
- `make install`: Creates a `venv`, activate it, and install `requirements.txt`
- `make sweep`: This will execute the program in sweep mode, we will discuss this later
- `make run ARGS="{initial_humans} {initial_vampires} {total_timestamps}"`: This is manual mode, more details are given below
- `make clean`: This will delete `__pycache__` and `Simulation Results` directories

### Manual Mode
This will run the simulation according to the command line arguments, i.e. `make run ARGS="7 2 20"`. In this simulation, there are:
- 7 humans, 2 vampires at the start, and the simulation will run for 20 timestamps
- Every interaction will be logged on the terminal
- Results will be saved in the `Simulation Results` directory with this format `Timestep_{timestep_number}.png`

<p align="center">
<img width="300" alt="image" src="https://github.com/Zain-Bin-Arshad/zombie-attack-simulator/assets/49767636/6ca36b5b-4f8e-4320-a50b-4021f1770861">
</p>


### Sweep Mode
Just run `make sweep` and see the magic happens. The simulation will run for all combinations of humans and vampires as per the `SWEEP_MODE_PARAMS`  variable inside `constants.py` for the given number of timestamps.
- Final plot will be saved in this format `{sweep_{sweep_count}_h_{total_humans}_v_{total_vampires}`
- `results.csv` will have the remaining humans and vampires count, something like this
<p align="center">
<img width="561" alt="image" src="https://github.com/Zain-Bin-Arshad/zombie-attack-simulator/assets/49767636/a14eefc0-fca3-4099-ba2a-ea7cb71d6a02">
</p>

## Note
- Thanks to the creators of [matplotlib](https://matplotlib.org/) for an awesome library  ❤️
- If you see any bugs feel free to post them on the issues page
- If you like what you see, I would love to hear any feedback and get connected

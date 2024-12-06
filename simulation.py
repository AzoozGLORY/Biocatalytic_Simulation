# simulation.py

from species import Species
from reactions import Reaction
import matplotlib.pyplot as plt

def run_simulation(species_list, reactions_list, time_end, delta_t):
    """
    Run the simulation.
    :param species_list: List of all species
    :param reactions_list: List of all reactions
    :param time_end: End time of the simulation
    :param delta_t: Time step
    :return: Tuple containing time points and species concentrations over time
    """
    time_points = [0]
    concentrations = {species.id: [species.current_concentration] for species in species_list}

    species_dict = {species.id: species for species in species_list}

    current_time = 0
    while current_time < time_end:
        for reaction in reactions_list:
            reaction.update_concentrations(species_dict, delta_t)
        current_time += delta_t
        time_points.append(current_time)
        for species in species_list:
            concentrations[species.id].append(species.current_concentration)

    return time_points, concentrations

def plot_results(time_points, concentrations, species_list):
    """
    Plot the simulation results.
    :param time_points: List of time points
    :param concentrations: Dictionary of species concentrations over time
    :param species_list: List of species
    """
    for species in species_list:
        plt.plot(time_points, concentrations[species.id], label=species.name)
    plt.xlabel('Time (minutes)')
    plt.ylabel('Concentration (mM)')
    plt.title('Biocatalytic Process Simulation')
    plt.legend()
    plt.grid(True)
    plt.show()

def main():
    # Define species
    E = Species(id='E', name='Enzyme', description='Catalyzes the conversion of S to P.', 
               initial_concentration=1.0, unit='mM', compartment='Reaction_Vessel', constant=True)
    S = Species(id='S', name='Substrate', description='Reactant converted to product P.', 
               initial_concentration=10.0, unit='mM', compartment='Reaction_Vessel', constant=False)
    P = Species(id='P', name='Product', description='Product formed from substrate S.', 
               initial_concentration=0.0, unit='mM', compartment='Reaction_Vessel', constant=False)
    
    species_list = [E, S, P]

    # Define reactions
    R1 = Reaction(
        id='R1',
        reactants=[(E, 1), (S, 1)],
        products=[(E, 1), (P, 1)],
        kinetic_law='Michaelis-Menten',
        parameters={'Vmax': 100, 'Km': 5},
        reversible=False
    )

    reactions_list = [R1]

    # Simulation parameters
    time_end = 60  # minutes
    delta_t = 1    # minute per step

    # Run simulation
    time_points, concentrations = run_simulation(species_list, reactions_list, time_end, delta_t)

    # Plot results
    plot_results(time_points, concentrations, species_list)

if __name__ == "__main__":
    main()

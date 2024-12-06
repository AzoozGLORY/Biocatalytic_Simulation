# reactions.py

class Reaction:
    def __init__(self, id, reactants, products, kinetic_law, parameters, reversible=False):
        """
        :param id: Reaction identifier
        :param reactants: List of tuples (Species, coefficient)
        :param products: List of tuples (Species, coefficient)
        :param kinetic_law: Type of kinetic law (e.g., 'Michaelis-Menten')
        :param parameters: Dictionary containing necessary parameters
        :param reversible: Boolean indicating if the reaction is reversible
        """
        self.id = id
        self.reactants = reactants
        self.products = products
        self.kinetic_law = kinetic_law
        self.parameters = parameters
        self.reversible = reversible

    def rate(self, species_dict):
        """
        Calculate the reaction rate based on the kinetic law and parameters.
        :param species_dict: Dictionary containing species with their IDs
        :return: Reaction rate
        """
        if self.kinetic_law == 'Michaelis-Menten':
            S = species_dict['S'].current_concentration  # Reactant concentration
            Vmax = self.parameters.get('Vmax', 100)  # Default value if not specified
            Km = self.parameters.get('Km', 5)
            rate = (Vmax * S) / (Km + S)
            return rate
        else:
            raise NotImplementedError(f"Kinetic law {self.kinetic_law} is not implemented.")

    def update_concentrations(self, species_dict, delta_t):
        """
        Update species concentrations based on the reaction rate and time step.
        :param species_dict: Dictionary containing species with their IDs
        :param delta_t: Time step
        """
        rate = self.rate(species_dict)
        for species, coeff in self.reactants:
            if not species.constant:
                species.current_concentration -= coeff * rate * delta_t
        for species, coeff in self.products:
            if not species.constant:
                species.current_concentration += coeff * rate * delta_t

# species.py

class Species:
    def __init__(self, id, name, description, initial_concentration, unit, compartment, constant):
        self.id = id
        self.name = name
        self.description = description
        self.initial_concentration = initial_concentration
        self.unit = unit
        self.compartment = compartment
        self.constant = constant
        self.current_concentration = initial_concentration

    def __repr__(self):
        return f"{self.name} ({self.id}): {self.current_concentration}{self.unit}"

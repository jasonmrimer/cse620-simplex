import math
import random


class ConstraintGenerator(object):
    def __init__(self, seed):
        self.seed = seed

    def random_in_range(self, multiplier, range_min, range_max):
        random.seed(self.seed * multiplier)
        return random.randint(range_min, range_max)

    def generate_random_coefficients(self, variable_count, multiplier):
        variables = []
        for x in range(variable_count):
            variables.append(self.random_in_range((x + 1) * multiplier, -10, 10))
        return variables

    def generate_random_constraints(self, constraint_count, variable_count):
        constraints = []
        for x in range(constraint_count):
            constraints.append(self.generate_random_coefficients(variable_count, x + 1))
        return constraints

    def generate_minimizer(self, constraint_count, variable_count):
        minimizer = []
        multiplier = (constraint_count + 1) * variable_count
        for x in range(variable_count):
            minimizer.append(self.random_in_range((x + 1) * multiplier, 0, 100))
        return minimizer

    def generate_constraint_resolutions(self, constraint_count):
        resolutions = []
        for x in range(constraint_count):
            resolutions.append(self.random_in_range(math.sqrt(self.seed) * x, 0, 100))
        return resolutions

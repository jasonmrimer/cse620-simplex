import random


class ConstraintGenerator(object):
    def __init__(self, seed):
        self.seed = seed

    def random_in_range(self, multiplier):
        random.seed(self.seed * multiplier)
        return random.randint(-10, 10)

    def generate_random_variables(self, variable_count, multiplier):
        variables = []
        for x in range(variable_count):
            variables.append(self.random_in_range((x + 1) * multiplier))

        return variables

    def generate_random_constraints(self, constraint_count, variable_count):
        constraints = []
        for x in range(constraint_count):
            constraints.append(self.generate_random_variables(variable_count, x + 1))
        return constraints

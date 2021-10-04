import random


class ConstraintGenerator(object):
    def __init__(self, seed):
        self.seed = seed

    def random_in_range(self, multiplier):
        random.seed(self.seed * multiplier)
        return random.randint(-10, 10)

    def generate_random_constraints(self, variable_count):
        constraints = []
        for x in range(variable_count):
            constraints.append(self.random_in_range(x))

        return constraints

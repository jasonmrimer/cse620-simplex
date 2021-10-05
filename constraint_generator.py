import math
import random


class ConstraintGenerator(object):
    def __init__(self, seed):
        self.seed = seed

    def random_in_range(self, multiplier, range_min, range_max):
        random.seed(self.seed * multiplier)
        return random.randint(range_min, range_max)

    def generate_random_coefficients(self, variable_count, multiplier):
        def multiplier_func(index):
            return multiplier * (index + 1)

        return self.looping_randomizer(
            multiplier_func,
            variable_count,
            -10,
            10
        )

    def generate_random_constraints(self, constraint_count, variable_count):
        constraints = []
        for x in range(constraint_count):
            constraints.append(
                self.generate_random_coefficients(variable_count, x + 1)
            )
        return constraints

    def generate_minimizer(self, constraint_count, variable_count):
        def multiplier_func(index):
            return (constraint_count + 1) * variable_count * (index + 1)

        return self.looping_randomizer(multiplier_func, variable_count, 0, 10)

    def generate_constraint_resolutions(self, constraint_count):
        seed = self.seed

        def multiplier_func(index):
            return math.sqrt(seed) * index

        return self.looping_randomizer(
            multiplier_func,
            constraint_count,
            0,
            100
        )

    def looping_randomizer(
            self,
            multiplier_func,
            variable_count,
            range_min,
            range_max
    ):
        coefficients = []
        for x in range(variable_count):
            coefficients.append(
                self.random_in_range(
                    multiplier_func(x), range_min, range_max
                )
            )
        return coefficients

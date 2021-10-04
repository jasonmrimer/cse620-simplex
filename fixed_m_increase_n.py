import unittest

import solver_coordinator
from constraint_generator import ConstraintGenerator


def feasible_solver_seed_finder(seed, solver):
    while (True):
        constraint_generator = ConstraintGenerator(seed)
        variable_count = 10

        minimizer = constraint_generator.generate_minimizer(variable_count)
        constraint_coefficients = constraint_generator.generate_random_constraints(2, variable_count)
        constraint_resolutions = constraint_generator.generate_constraint_resolutions(2)

        solver = solver_coordinator.main(
            minimizer,
            constraint_coefficients,
            constraint_resolutions
        )

        seed += 1

        if solver:
            break
    print(seed)
    return solver


class MyTestCase(unittest.TestCase):
    def test_main_random(self):
        seed = 1
        constraint_generator = ConstraintGenerator(seed)
        variable_count = 10

        minimizer = constraint_generator.generate_minimizer(variable_count)
        constraint_coefficients = constraint_generator.generate_random_constraints(2, variable_count)
        constraint_resolutions = constraint_generator.generate_constraint_resolutions(2)

        solver = solver_coordinator.main(
            minimizer,
            constraint_coefficients,
            constraint_resolutions
        )

        self.assertTrue(solver.Objective().Value())


if __name__ == '__main__':
    unittest.main()

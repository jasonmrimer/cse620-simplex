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


def run_solution(constraint_generator, solver, variable_count, constraint_count):
    minimizer = constraint_generator.generate_minimizer(variable_count)
    constraint_coefficients = constraint_generator.generate_random_constraints(constraint_count, variable_count)
    constraint_resolutions = constraint_generator.generate_constraint_resolutions(constraint_count)
    solver = solver_coordinator.main(
        minimizer,
        constraint_coefficients,
        constraint_resolutions
    )
    return solver


class MyTestCase(unittest.TestCase):
    def test_n_10(self):
        seed = 1
        constraint_count = 2
        variable_count = 10
        constraint_generator = ConstraintGenerator(seed)

        solver = None
        solver = run_solution(constraint_generator, solver, variable_count, constraint_count)

        self.assertTrue(solver.Objective().Value())

    def test_n_20(self):
        seed = 2
        constraint_count = 2
        variable_count = 20
        constraint_generator = ConstraintGenerator(seed)

        solver = None
        solver = run_solution(constraint_generator, solver, variable_count, constraint_count)

        self.assertTrue(solver.Objective().Value())
        print(solver.Objective().Value())

    def test_n_30(self):
        seed = 2
        constraint_count = 2
        variable_count = 30
        constraint_generator = ConstraintGenerator(seed)

        solver = None
        solver = run_solution(constraint_generator, solver, variable_count, constraint_count)

        self.assertTrue(solver.Objective().Value())
        print(solver.Objective().Value())

    def test_n_40(self):
        seed = 2
        constraint_count = 22
        variable_count = 40
        constraint_generator = ConstraintGenerator(seed)

        solver = None
        solver = run_solution(constraint_generator, solver, variable_count, constraint_count)

        self.assertTrue(solver.Objective().Value())
        print(solver.Objective().Value())


    def test_n_50(self):
        seed = 1
        constraint_count = 2
        variable_count = 50
        constraint_generator = ConstraintGenerator(seed)

        solver = None
        solver = run_solution(constraint_generator, solver, variable_count, constraint_count)

        self.assertTrue(solver.Objective().Value())
        print(solver.Objective().Value())


if __name__ == '__main__':
    unittest.main()

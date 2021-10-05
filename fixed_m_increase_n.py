import unittest

import solver_coordinator
from constraint_generator import ConstraintGenerator


def feasible_solver_seed_finder(
        seed,
        constraint_count,
        variable_count
):
    while (True):
        constraint_generator = ConstraintGenerator(seed)

        minimizer = constraint_generator.generate_minimizer(
            constraint_count,
            variable_count
        )
        constraint_coefficients = constraint_generator.generate_random_constraints(
            constraint_count,
            variable_count
        )
        constraint_resolutions = constraint_generator.generate_constraint_resolutions(
            constraint_count
        )

        solver = solver_coordinator.main(
            minimizer,
            constraint_coefficients,
            constraint_resolutions
        )

        seed += 1

        if solver:
            break

    print(f'found seed: {seed}')
    return solver


def run_solution(
        constraint_generator,
        variable_count,
        constraint_count
):
    minimizer = constraint_generator.generate_minimizer(
        constraint_count,
        variable_count
    )
    constraint_coefficients = constraint_generator.generate_random_constraints(
        constraint_count,
        variable_count
    )
    constraint_resolutions = constraint_generator.generate_constraint_resolutions(
        constraint_count
    )
    solver = solver_coordinator.main(
        minimizer,
        constraint_coefficients,
        constraint_resolutions
    )
    return solver


def print_solution(n, solver):
    print(
        f'optimal solution for n = {n}: {solver.Objective().Value()}')


class MyTestCase(unittest.TestCase):
    seed = 1

    def test_n_increasing(self):
        for n in range(10, 60, 10):
            constraint_generator = ConstraintGenerator(self.seed)
            constraint_count = 2
            variable_count = n
            solver = run_solution(
                constraint_generator,
                variable_count,
                constraint_count
            )
            self.assertIsNotNone(solver.Objective().Value())
            print_solution(n, solver)

    @unittest.skip
    def test_n_10(self):
        print('\nstart n10')
        constraint_count = 2
        variable_count = 10
        constraint_generator = ConstraintGenerator(self.seed)

        solver = None
        # feasible_solver_seed_finder(self.seed, solver, constraint_count, variable_count)

        solver = run_solution(constraint_generator, variable_count,
                              constraint_count)

        self.assertIsNotNone(solver.Objective().Value())
        print_solution(10, solver)

    @unittest.skip
    def test_n_20(self):
        print('\nstart n20')
        constraint_count = 2
        variable_count = 20
        constraint_generator = ConstraintGenerator(self.seed)

        solver = None
        solver = run_solution(constraint_generator, variable_count,
                              constraint_count)

        self.assertIsNotNone(solver.Objective().Value())
        print_solution(20, solver)

    @unittest.skip
    def test_n_30(self):
        print('\nstart n30')
        constraint_count = 2
        variable_count = 30
        constraint_generator = ConstraintGenerator(self.seed)

        solver = None
        solver = run_solution(constraint_generator, variable_count,
                              constraint_count)

        self.assertIsNotNone(solver.Objective().Value())
        print_solution(30, solver)

    @unittest.skip
    def test_n_40(self):
        print('\nstart n40')
        constraint_count = 2
        variable_count = 40
        constraint_generator = ConstraintGenerator(self.seed)

        solver = None
        solver = run_solution(constraint_generator, variable_count,
                              constraint_count)

        self.assertIsNotNone(solver.Objective().Value())
        print_solution(40, solver)

    @unittest.skip
    def test_n_50(self):
        print('\nstart n50')
        constraint_count = 2
        variable_count = 50
        constraint_generator = ConstraintGenerator(self.seed)

        solver = None
        solver = run_solution(constraint_generator, variable_count,
                              constraint_count)

        self.assertIsNotNone(solver.Objective().Value())
        print_solution(50, solver)


if __name__ == '__main__':
    unittest.main()

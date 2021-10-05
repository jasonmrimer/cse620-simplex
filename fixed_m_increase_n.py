import unittest

import solver_coordinator


def print_solution(n, solver):
    print(
        f'optimal solution for n = {n}: {solver.Objective().Value()}')


class MyTestCase(unittest.TestCase):
    seed = 1
    constraint_count = 2

    def test_n_increasing(self):
        for n in range(10, 60, 10):
            variable_count = n
            solver = solver_coordinator.main_refactored(
                self.seed,
                self.constraint_count,
                variable_count,
                False
            )

            self.assertIsNotNone(solver.Objective().Value())
            print_solution(n, solver)


if __name__ == '__main__':
    unittest.main()

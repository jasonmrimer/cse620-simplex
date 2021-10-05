import unittest

import solver_coordinator


class MyTestCase(unittest.TestCase):
    seed = 2
    print_details = False

    def test_m_increasing_n_increasing(self):
        for constraint_count in range(2, 15, 4):
            for variable_count in range(10, 51, 10):
                solution = solver_coordinator.main_refactored(
                    self.seed,
                    constraint_count,
                    variable_count,
                    self.print_details
                )
                print(f'wall time: {solution.wall_time}')

                # self.assertIsNotNone(solver.Objective().Value())
                print_solution(constraint_count, variable_count, solution.solver)


def print_solution(m, n, solver):
    print(
        f'optimal solution for m = {m} | n = {n}: '
        f'{solver.Objective().Value()}')


if __name__ == '__main__':
    unittest.main()

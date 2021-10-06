import unittest

import solver_coordinator


class SolutionSeed:
    def __init__(self, solution, seed):
        self.solution = solution
        self.seed = seed


def feasible_solver_seed_finder(
        seed,
        constraint_count,
        variable_count
):
    while True:
        # print('whilestart')
        solution = solver_coordinator.main_refactored(
            seed,
            constraint_count,
            variable_count,
            True
        )
        # print(f'objective: {solution}')
        if solution is not None:
            break

        seed += 1

    return SolutionSeed(solution, seed)


class MyTestCase(unittest.TestCase):
    print_details = False

    def test_m_increasing_n_increasing(self):
        for constraint_count in range(2, 15, 4):
            self.run_solver_with_configs(constraint_count, 4)
            for variable_count in range(10, 51, 10):
                self.run_solver_with_configs(constraint_count, variable_count)

    def run_solver_with_configs(self, constraint_count, variable_count):
        print(f'm = {constraint_count} | n = {variable_count}')
        seed = 1
        solutionSeed = feasible_solver_seed_finder(
            seed,
            constraint_count,
            variable_count
        )
        print(f'wall time: {solutionSeed.solution.wall_time}')
        # self.assertIsNotNone(solver.Objective().Value())
        print_solution(
            constraint_count,
            variable_count,
            solutionSeed.solution.solver
        )


def print_solution(m, n, solver):
    print(
        f'optimal solution for m = {m} | n = {n}: '
        f'{solver.Objective().Value()}\n')


if __name__ == '__main__':
    unittest.main()

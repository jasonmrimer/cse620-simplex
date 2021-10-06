import unittest

import solver_coordinator


class SolutionSeed:
    def __init__(self, solution, seed):
        self.solution = solution
        self.seed = seed


def feasible_solver_seed_finder(seed, constraint_count, variable_count,
                                should_print_results):
    while True:
        # print('whilestart')
        solution = solver_coordinator.main_refactored(
            seed,
            constraint_count,
            variable_count,
            should_print_results
        )
        # print(f'objective: {solution}')
        if is_feasible_solution(solution):
            break

        seed += 1

    return SolutionSeed(solution, seed)


def is_feasible_solution(solution):
    return solution is not None and solution.solver.Objective().Value() > 0


class MyTestCase(unittest.TestCase):
    print_details = False

    def test_m_increasing_n_increasing(self):
        should_print_results = True
        for constraint_count in range(2, 15, 4):
            self.run_solver_with_configs(constraint_count, 4,
                                         should_print_results)
            for variable_count in range(10, 51, 10):
                self.run_solver_with_configs(
                    constraint_count,
                    variable_count,
                    should_print_results
                )

    def test_multiple_times(self):
        constraint_count = 2
        variable_count = 30
        should_print_results = False
        for x in range(0, 10):
            self.run_solver_with_configs(
                constraint_count,
                variable_count,
                should_print_results
            )

    def run_solver_with_configs(self, constraint_count, variable_count,
                                should_print_results):
        # print(f'm = {constraint_count} | n = {variable_count}')
        seed = 200
        solutionSeed = feasible_solver_seed_finder(seed, constraint_count,
                                                   variable_count, True)
        # print(f'wall time: {solutionSeed.solution.wall_time}')
        # print(f'seed {solutionSeed.seed}')
        # print(f'{solutionSeed.solution.wall_time}')
        # self.assertIsNotNone(solver.Objective().Value())
        # print_solution(
        #     constraint_count,
        #     variable_count,
        #     solutionSeed.solution.solver
        # )


def print_solution(m, n, solver):
    print(
        f'optimal solution for m = {m} | n = {n}: '
        f'{solver.Objective().Value()}\n')


if __name__ == '__main__':
    unittest.main()

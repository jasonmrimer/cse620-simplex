import unittest

import solver_coordinator


class SolutionSeed:
    def __init__(self, solution, seed):
        self.solution = solution
        self.seed = seed


def feasible_solver_seed_finder(
        seed, constraint_count, variable_count,
        should_print_results
):
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

    def test_many_optima(self):
        constraint_count = 14
        variable_count = 50
        should_print_results = False
        for seed in range(1, 1001):
            self.run_solver_with_configs(
                constraint_count, variable_count, should_print_results, seed
            )

    def test_single_run_choose_m_n(self):
        constraint_count = 200
        variable_count = 200
        should_print_results = True
        self.run_solver_with_configs(
            constraint_count, variable_count, should_print_results, 1
        )

    def test_m_increasing_n_increasing(self):
        should_print_results = True
        for constraint_count in range(2, 15, 4):
            self.run_solver_with_configs(
                constraint_count, 4, should_print_results, 1
            )
            for variable_count in range(10, 51, 10):
                self.run_solver_with_configs(
                    constraint_count, variable_count, should_print_results, 1
                )

    def test_multiple_times(self):
        constraint_count = 2
        variable_count = 2
        should_print_results = False
        for x in range(0, 10):
            self.run_solver_with_configs(
                constraint_count, variable_count, should_print_results, 1
            )

    def run_solver_with_configs(
            self, constraint_count, variable_count, should_print_results, seed
    ):
        # print(f'm = {constraint_count} | n = {variable_count}')
        solutionSeed = feasible_solver_seed_finder(
            seed,
            constraint_count,
            variable_count,
            should_print_results
        )
        # print(f'wall time\n{solutionSeed.solution.wall_time}')
        # print(f'seed {solutionSeed.seed}')
        # print(f'{solutionSeed.solution.wall_time}')
        # self.assertIsNotNone(solver.Objective().Value())
        print(f'{solutionSeed.solution.solver.Objective().Value()}')
        # print_solution(solutionSeed.solution.solver)


def print_solution(solver):
    print(
        f'optimal solution\n{solver.Objective().Value()}\n'
    )


if __name__ == '__main__':
    unittest.main()

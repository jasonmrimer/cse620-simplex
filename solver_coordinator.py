from time import time

from ortools.linear_solver import pywraplp

from constraint_generator import ConstraintGenerator
from solution import Solution
from solution_printer import print_constraint_equation, \
    print_minimizer_equation, print_pretty_solution


def main_refactored(
        seed,
        constraint_count,
        variable_count,
        should_print_results=False
):
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
    solver = main(
        minimizer,
        constraint_coefficients,
        constraint_resolutions,
        should_print_results
    )

    return solver


def no_solution(status):
    return status != pywraplp.Solver.OPTIMAL


def main(
        minimizer,
        constraint_coefficients,
        constraint_resolutions,
        should_print_results=False
):
    solver = pywraplp.Solver.CreateSolver('GLOP')

    variables = set_variables(constraint_coefficients, solver)

    set_constraint_equations(
        solver,
        constraint_resolutions,
        constraint_coefficients,
        variables
    )

    setup_minimizer(solver, minimizer, variables)

    start = time()
    status = solver.Solve()
    end = time()

    if no_solution(status):
        if should_print_results:
            print('The problem does not have an optimal solution.')
        return None

    print_results(
        constraint_coefficients,
        constraint_resolutions,
        minimizer,
        variables,
        should_print_results
    )

    return Solution(solver, (end - start))


def print_results(
        constraint_coefficients, constraint_resolutions, minimizer, variables,
        should_print
):
    if should_print:
        print_minimizer_equation(minimizer, variables)
        print_constraint_equation(
            variables,
            constraint_coefficients,
            constraint_resolutions
        )
        print_pretty_solution(variables)


def setup_minimizer(solver, minimizer, variables):
    objective = solver.Objective()
    for i in range(len(variables)):
        objective.SetCoefficient(variables[i], minimizer[i])
    objective.SetMinimization()
    return objective


def set_constraint_equations(
        solver,
        constraint_resolutions,
        constraint_coefficients,
        variables
):
    constraint_list = []
    for i in range(len(constraint_resolutions)):
        constraint_list.append(
            solver.Constraint(
                constraint_resolutions[i],
                solver.infinity()
            )
        )
        for j in range(len(variables)):
            constraint_list[i].SetCoefficient(
                variables[j],
                constraint_coefficients[i][j]
            )


def set_variables(constraint_coefficients, solver):
    variables = []
    for i in range(len(constraint_coefficients[0])):
        variables.append(solver.NumVar(0, solver.infinity(), f'x{i + 1}'))
    return variables


if __name__ == '__main__':
    main()

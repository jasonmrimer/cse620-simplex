import datetime
from time import time

from ortools.linear_solver import pywraplp

from constraint_generator import ConstraintGenerator
from solution import Solution


def main_refactored(
        seed,
        constraint_count,
        variable_count,
        print_results=False
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
        print_results
    )

    return solver


def no_solution(status):
    return status != pywraplp.Solver.OPTIMAL


def print_minimizer_equation(variables, minimizer):
    pass


def main(
        minimizer,
        constraint_coefficients,
        constraint_resolutions,
        print_results=False
):
    solver = pywraplp.Solver.CreateSolver('GLOP')

    variables = set_variables(constraint_coefficients, solver)

    set_constraint_equations(
        solver,
        constraint_resolutions,
        constraint_coefficients,
        variables
    )

    objective = setup_minimizer(solver, minimizer, variables)

    start = time()
    status = solver.Solve()
    end = time()

    if no_solution(status):
        if print_results:
            print('The problem does not have an optimal solution.')
        return None

    if print_results:
        print_equation(variables, constraint_coefficients)
        # print_constraints(
        #     constraint_resolutions,
        #     constraint_coefficients,
        #     variables
        # )
        print_minimizer_equation(variables, minimizer)
        print_minimizer(variables, objective)
        print_solution(variables)

    return Solution(solver, (end - start))


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


def print_constraints(
        constraint_resolutions,
        constraint_coefficients,
        variables
):
    for i in range(len(constraint_resolutions)):
        print(f'constraint {i + 1} res: {constraint_resolutions[i]}')
        for j in range(len(variables)):
            print(
                f'coefficient: {variables[j].name()}: '
                f'{constraint_coefficients[i][j]}'
            )


def print_minimizer(variables, objective):
    for variable in variables:
        print(
            f'minimizer: {variable.name()}: '
            f'{objective.GetCoefficient(variable)}'
        )


def print_solution(variables):
    for variable in variables:
        print(f'solution: {variable.name()}: {variable.solution_value()}')


def determine_sign(number):
    return '+' if number > 0 else '—'


def print_equation(variables, coefficients):
    print('eequation')
    SUB = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
    pretty_variables = []
    for variable in variables:
        pretty_variables.append(variable.name().translate(SUB))

    for i in range(len(coefficients)):
        equation = f'{coefficients[i][0]}{pretty_variables[0]}'
        for j in range(1, len(variables)):
            sign = determine_sign(coefficients[i][j])
            equation += f' {sign} {abs(coefficients[i][j])}{pretty_variables[j]}'
        print(equation)


if __name__ == '__main__':
    main()

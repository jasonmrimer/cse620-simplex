from ortools.linear_solver import pywraplp


def main(
        minimizer,
        constraint_coefficients,
        constraint_resolutions,
        print_results=False
):
    solver = pywraplp.Solver.CreateSolver('GLOP')

    variables = []
    for i in range(len(constraint_coefficients[0])):
        variables.append(solver.NumVar(0, solver.infinity(), f'x{i + 1}'))

    constraint_list = []
    for i in range(len(constraint_resolutions)):
        constraint_list.append(
            solver.Constraint(
                constraint_resolutions[i],
                constraint_resolutions[i]
            )
        )
        for j in range(len(variables)):
            constraint_list[i].SetCoefficient(
                variables[j],
                constraint_coefficients[i][j]
            )

    objective = solver.Objective()
    for i in range(len(variables)):
        objective.SetCoefficient(variables[i], minimizer[i])

    objective.SetMinimization()

    status = solver.Solve()
    if status != pywraplp.Solver.OPTIMAL:
        print('The problem does not have an optimal solution.')
        return None

    if print_results:
        print_constraints(
            constraint_resolutions,
            constraint_coefficients,
            variables
        )
        print_minimizer(variables, objective)
        print_solution(variables)

    return solver


def print_constraints(constraint_resolutions, constraint_coefficients,
                      variables):
    for i in range(len(constraint_resolutions)):
        print(f'constraint {i + 1} res: {constraint_resolutions[i]}')
        for j in range(len(variables)):
            print(
                f'coefficient: {variables[j].name()}: {constraint_coefficients[i][j]}')


def print_minimizer(variables, objective):
    for variable in variables:
        print(
            f'minimizer: {variable.name()}: '
            f'{objective.GetCoefficient(variable)}'
        )


def print_solution(variables):
    for variable in variables:
        print(f'solution: {variable.name()}: {variable.solution_value()}')


if __name__ == '__main__':
    main()

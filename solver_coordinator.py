from ortools.linear_solver import pywraplp


def main(
        minimizer,
        constraint_coefficients,
        constraint_resolutions
):
    solver = pywraplp.Solver.CreateSolver('GLOP')

    # create variables for solver with x# names
    variables = []
    for i in range(len(constraint_coefficients[0])):
        variables.append(solver.NumVar(0, solver.infinity(), f'x{i + 1}'))

    constraint_list = []
    for i in range(len(constraint_resolutions)):
        constraint_list.append(solver.Constraint(0, constraint_resolutions[i]))
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
    else:
        print('Solution:')
        print('Objective value =', solver.Objective().Value())
        for x in variables:
            print(f'{x.name()} = {x.solution_value()}')
    # print('x1 =', variables[0].solution_value())
    # print('x2 =', variables[1].solution_value())
    # print('x3 =', variables[2].solution_value())
    # print('x4 =', variables[3].solution_value())
        return solver


if __name__ == '__main__':
    main()

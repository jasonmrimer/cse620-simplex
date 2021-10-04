from ortools.linear_solver import pywraplp


def main():
    # Create the linear solver with the GLOP backend.
    solver = pywraplp.Solver.CreateSolver('GLOP')

    # Create the variables x and y.
    x1 = solver.NumVar(0, solver.infinity(), 'x1')
    x2 = solver.NumVar(0, solver.infinity(), 'x2')
    x3 = solver.NumVar(0, solver.infinity(), 'x3')
    x4 = solver.NumVar(0, solver.infinity(), 'x4')

    print('Number of variables =', solver.NumVariables())

    solver.Add(x1 + 2 * x2 - x3 - x4 == 1)
    solver.Add(-1 * x1 - 5 * x2 + 2 * x3 + 3 * x4 == 1)
    solver.Minimize(x1 + x2 + x3 + x4)

    print('Number of constraints =', solver.NumConstraints())

    status = solver.Solve()

    # print('Solution:')
    # print('Objective value =', solver.Objective().Value())
    # print('x1 =', x1.solution_value())
    # print('x2 =', x2.solution_value())
    # print('x3 =', x3.solution_value())
    # print('x4 =', x4.solution_value())
    if status != pywraplp.Solver.OPTIMAL:
        print('The problem does not have an optimal solution.')
    else:
        return solver


if __name__ == '__main__':
    main()

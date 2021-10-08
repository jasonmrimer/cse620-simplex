def printable_equation(coefficients, variables):
    subscripter = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
    pretty_variables = []
    for variable in variables:
        pretty_variables.append(variable.name().translate(subscripter))

    equation = f'{coefficients[0]}{pretty_variables[0]}'
    for j in range(1, len(variables)):
        sign = determine_sign(coefficients[j])
        equation += f'{sign}{abs(coefficients[j])}{pretty_variables[j]}'
    return equation


def determine_sign(number):
    return '+' if number > 0 else '-'


def print_constraint_equation(variables, coefficients, resolutions=None):
    print(f'constraints')
    for i in range(len(coefficients)):
        equation = printable_equation(coefficients[i], variables)
        equation += f'≥{resolutions[i]}'
        print(equation)


def print_minimizer_equation(coefficients, variables):
    print('minimizer')
    print(printable_equation(coefficients, variables))


def solution_prettier(variable):
    subscripter = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
    solution = f'{variable.name().translate(subscripter)}={variable.solution_value()}'
    return solution


def print_pretty_solution(variables):
    pretty_solution = solution_prettier(variables[0])
    for i in range(1, len(variables)):
        pretty_solution += f', {solution_prettier(variables[i])}'
    print(f'solution\n{pretty_solution}')


def print_minimizer(variables, objective):
    for variable in variables:
        print(
            f'minimizer: {variable.name()}: '
            f'{objective.GetCoefficient(variable)}'
        )


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
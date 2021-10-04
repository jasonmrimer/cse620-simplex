from unittest import TestCase

from constraint_generator import ConstraintGenerator


class TestConstraintGenerator(TestCase):
    seed = 20

    def test_random_in_range(self):
        # test the consistency of using a seed for randomizer
        constraint_generator = ConstraintGenerator(self.seed)
        self.assertEqual(-6, constraint_generator.random_in_range(1))

    def test_generate_random_variables(self):
        # test the generator for a given number of variables
        constraint_generator = ConstraintGenerator(self.seed)
        variables = constraint_generator.generate_random_coefficients(4, 1)
        self.assertEqual(4, len(variables))
        self.assertEqual(-6, variables[0])
        self.assertEqual(4, variables[1])
        self.assertEqual(-1, variables[2])
        self.assertEqual(-2, variables[3])

    def test_generate_random_constraints(self):
        # test generation of several constraint equations
        constraint_generator = ConstraintGenerator(self.seed)
        constraints = constraint_generator.generate_random_constraints(2, 4)
        self.assertEqual(2, len(constraints))

        self.assertEqual(4, len(constraints[0]))
        self.assertEqual(-6, constraints[0][0])
        self.assertEqual(4, constraints[0][1])
        self.assertEqual(-1, constraints[0][2])
        self.assertEqual(-2, constraints[0][3])

        self.assertEqual(4, len(constraints[1]))
        self.assertEqual(4, constraints[1][0])
        self.assertEqual(-2, constraints[1][1])
        self.assertEqual(6, constraints[1][2])
        self.assertEqual(-7, constraints[1][3])

    def test_generate_minimizer(self):
        constraint_generator = ConstraintGenerator(self.seed)
        minimizer = constraint_generator.generate_minimizer(4)
        self.assertEqual(4, len(minimizer))
        self.assertEqual(-1, minimizer[0])
        self.assertEqual(5, minimizer[1])
        self.assertEqual(-1, minimizer[2])
        self.assertEqual(-10, minimizer[3])

    def test_generate_constraint_resolutions(self):
        constraint_generator = ConstraintGenerator(self.seed)
        resolutions = constraint_generator.generate_constraint_resolutions(4)
        self.assertEqual(4, len(resolutions))
        self.assertEqual(1, resolutions[0])
        self.assertEqual(-9, resolutions[1])
        self.assertEqual(-1, resolutions[2])
        self.assertEqual(-4, resolutions[3])

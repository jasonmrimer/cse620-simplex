from unittest import TestCase

from constraint_generator import ConstraintGenerator


class TestConstraintGenerator(TestCase):
    def test_random_number_generator(self):
        constraint_generator = ConstraintGenerator(20)
        self.assertEqual(-6, constraint_generator.random_in_range(1))

    def test_number_of_variables_generated_as_given(self):
        constraint_generator = ConstraintGenerator(20)
        constraints = constraint_generator.generate_random_constraints(4)
        self.assertEqual(4, len(constraints))
        self.assertEqual(2, constraints[0])
        self.assertEqual(-6, constraints[1])
        self.assertEqual(4, constraints[2])
        self.assertEqual(-1 , constraints[3])


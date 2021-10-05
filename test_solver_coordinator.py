import unittest
from unittest import TestCase

import lecture_sample
import solver_coordinator
from constraint_generator import ConstraintGenerator


class MyTestCase(unittest.TestCase):
    # test with lecture example
    def test_main(self):
        expected_precision_decimal_places = 6
        minimizer = [1, 1, 1, 1]
        constraint_coefficients = [
            [1, 2, -1, -1],
            [-1, -5, 2, 3]
        ]
        constraint_resolutions = [
            1,
            1
        ]

        solver = solver_coordinator.main(
            minimizer,
            constraint_coefficients,
            constraint_resolutions
        )

        self.assertAlmostEqual(
            3.0,
            solver.Objective().Value(),
            expected_precision_decimal_places,
            'optimal value not equal'
        )

        self.assertAlmostEqual(
            2.0,
            solver.LookupVariable('x1').solution_value(),
            expected_precision_decimal_places,
            'x1 value not within expected range'
        )
        self.assertAlmostEqual(
            0.0,
            solver.LookupVariable('x2').solution_value(),
            expected_precision_decimal_places,
            'x2 value not within expected range'
        )
        self.assertAlmostEqual(
            0.0,
            solver.LookupVariable('x3').solution_value(),
            expected_precision_decimal_places,
            'x3 value not within expected range'
        )
        self.assertAlmostEqual(
            1.0,
            solver.LookupVariable('x4').solution_value(),
            expected_precision_decimal_places,
            'x4 value not within expected range'
        )

    def test_main_random(self):
        expected_precision_decimal_places = 3
        constraint_generator = ConstraintGenerator(26)

        minimizer = constraint_generator.generate_minimizer(2, 4)
        constraint_coefficients = constraint_generator.generate_random_constraints(2, 4)
        constraint_resolutions = constraint_generator.generate_constraint_resolutions(2)

        solver = solver_coordinator.main(
            minimizer,
            constraint_coefficients,
            constraint_resolutions
        )

        self.assertAlmostEqual(
            -5.2857,
            solver.Objective().Value(),
            expected_precision_decimal_places,
            'optimal value not equal'
        )

        self.assertAlmostEqual(
            0.571,
            solver.LookupVariable('x1').solution_value(),
            expected_precision_decimal_places,
            'x1 value not within expected range'
        )
        self.assertAlmostEqual(
            0.0,
            solver.LookupVariable('x2').solution_value(),
            expected_precision_decimal_places,
            'x2 value not within expected range'
        )
        self.assertAlmostEqual(
            0.4285,
            solver.LookupVariable('x3').solution_value(),
            expected_precision_decimal_places,
            'x3 value not within expected range'
        )
        self.assertAlmostEqual(
            0.0,
            solver.LookupVariable('x4').solution_value(),
            expected_precision_decimal_places,
            'x4 value not within expected range'
        )


if __name__ == '__main__':
    unittest.main()

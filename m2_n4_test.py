import unittest

import lecture_sample


class MyTestCase(unittest.TestCase):
    def test_given_sample_proves_correct(self):
        solver = lecture_sample.main()

        self.assertEqual(2.9999999999999996, solver.Objective().Value())
        self.assertEqual(1.9999999999999998, solver.LookupVariable('x1').solution_value())
        expected_precision_decimal_places = 6

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


if __name__ == '__main__':
    unittest.main()

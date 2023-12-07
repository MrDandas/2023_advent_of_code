import unittest
import wait_for_it

class WaitForItTest(unittest.TestCase):

    def test_part_simple(self):
        self.assertEqual(4, wait_for_it.WaitForIt.solve_part_1_impl(7, 9))
        self.assertEqual(2, wait_for_it.WaitForIt.solve_part_1_impl(3, 0))
        self.assertEqual(3, wait_for_it.WaitForIt.solve_part_1_impl(4, 2))
        self.assertEqual(2, wait_for_it.WaitForIt.solve_part_1_impl(5, 5))
        self.assertEqual(5, wait_for_it.WaitForIt.solve_part_1_impl(6, 3))
        self.assertEqual(5, wait_for_it.WaitForIt.solve_part_1_impl(6, 4))
        self.assertEqual(3, wait_for_it.WaitForIt.solve_part_1_impl(6, 6))

    def test_part_1(self):
        content = \
            """
            Time:      7  15   30
            Distance:  9  40  200
            """
        # The first race lasts 7 milliseconds. The record distance in this race is 9 millimeters.
        # The second race lasts 15 milliseconds. The record distance in this race is 40 millimeters.
        # The third race lasts 30 milliseconds. The record distance in this race is 200 millimeters.

        print(f'+++ Testing [{self.__class__}]: +++')
        print(f'> Input: {content}')

        self.assertEqual(288, wait_for_it.WaitForIt.solve_part_1(content[1:-1].split('\n')))


if __name__ == '__main__':
    unittest.main()

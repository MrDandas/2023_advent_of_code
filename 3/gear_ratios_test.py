import unittest
import gear_ratios
from util.part_enum import Part


class GearRatiosTest(unittest.TestCase):

    def test_part_2(self):
        content = (['.......497........',
                    '436........765*...',
                    '...*982...........',
                    '...*........11111.',
                    '..1...........+...'],
                   [(0, 7, 9, 497), (1, 0, 2, 436), (1, 11, 13, 765), (2, 4, 6, 982), (3, 12, 16, 11111), (4, 2, 2, 1)],
                   [(1, 14), (2, 3), (3, 3), (4,14)],
                   436 + 765 + 982 + 11111 + 1)

        print(f'+++ Testing [{self.__class__}]: +++')
        nums, specs, number_sum = gear_ratios.GearRatios.solve(content[0], part=Part.ONE)
        self.assertEqual(content[1], nums, f'input value [{content[1]}]. Numbers not found correct')
        self.assertEqual(content[2], specs, f'input value [{content[2]}]. Special chars not found correct')
        self.assertEqual(content[3], number_sum, f'input value [{content[3]}]. Sum is not correct')
        print(f' -- -- -- -- -- -- -- -- -- -- -- -- -- -- --\n')

    def test_part_2(self):
        content = (['.......497........',
                    '436........765*...',
                    '...*982...........',
                    '...*........11111.',
                    '..1...........+...'],
                   [(0, 7, 9, 497), (1, 0, 2, 436), (1, 11, 13, 765), (2, 4, 6, 982), (3, 12, 16, 11111), (4, 2, 2, 1)],
                   [(1, 14), (2, 3), (3, 3)],
                   (436 * 982) + (982 * 1))

        print(f'+++ Testing [{self.__class__}]: +++')
        nums, specs, number_sum = gear_ratios.GearRatios.solve(content[0], part=Part.TWO)
        self.assertEqual(content[1], nums, f'input value [{content[1]}]. Numbers not found correct')
        self.assertEqual(content[2], specs, f'input value [{content[2]}]. Special chars not found correct')
        self.assertEqual(content[3], number_sum, f'input value [{content[3]}]. Sum is not correct')
        print(f' -- -- -- -- -- -- -- -- -- -- -- -- -- -- --\n')


if __name__ == '__main__':
    unittest.main()

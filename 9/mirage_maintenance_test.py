import unittest
from mirage_maintenance import MirageMaintenance


class MirageMaintenanceTest(unittest.TestCase):

    def test_parser(self):
        content = \
            """ \
0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45\
            """

        print(f'+++ Testing [{self.__class__}]: +++')
        print(f'> Input: {content}')

        self.assertEqual([[0, 3, 6, 9, 12, 15], [1, 3, 6, 10, 15, 21], [10, 13, 16, 21, 30, 45]],
                         MirageMaintenance.parse(content[1:-1].split('\n')))

    def test_part_1(self):
        content = \
            """ \
0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45\
            """

        print(f'+++ Testing [{self.__class__}]: +++')
        print(f'> Input: {content}')

        self.assertEqual(18+28+68, MirageMaintenance.solve_1(MirageMaintenance.parse(content[1:-1].split('\n'))))

    def test_part_2(self):
        content = \
            """ \
0 3 6 9 12 15\
            """

        print(f'+++ Testing [{self.__class__}]: +++')
        print(f'> Input: {content}')

        self.assertEqual(5, MirageMaintenance.solve_2(MirageMaintenance.parse(content[1:-1].split('\n'))))


if __name__ == '__main__':
    unittest.main()

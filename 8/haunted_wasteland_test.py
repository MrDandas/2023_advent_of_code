import unittest
from haunted_wasteland import HauntedWasteland

class HauntedWastelandTest(unittest.TestCase):

    def test_part_1(self):
        content = \
            """
RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)
            """

        print(f'+++ Testing [{self.__class__}]: +++')
        print(f'> Input: {content}')

        self.assertEqual(2, HauntedWasteland.solve(content[1:-1].split('\n')))

    def test_part_2(self):
        content = \
            """
LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)
            """
        print(f'+++ Testing [{self.__class__}]: +++')
        print(f'> Input: {content}')

        self.assertEqual(6, HauntedWasteland.solve(content[1:-1].split('\n')))


if __name__ == '__main__':
    unittest.main()

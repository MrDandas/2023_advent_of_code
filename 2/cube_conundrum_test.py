import unittest
import cube_conundrum


class CubeConundrumTest(unittest.TestCase):

    def test_complete(self):
        game_bag = {'red': 12, 'green': 13, 'blue': 14}

        content = [
            (['Game 1: 2 green'], 1, 2),
            (['Game 1: 2 green, 6 blue, 7 red; 12 green, 6 blue, 3 red; 5 red, 18 green, 4 blue'], 0, 18 * 6 * 7),
            (['Game 1: 2 green, 6 blue, 7 red; 12 green, 6 blue, 3 red; 5 red, 18 green, 4 blue', 'Game 5: 2 green'], 5,
             18 * 6 * 7 + 2),
            (['Game 2: 2 green, 6 blue, 7 red; ', 'Game 5: 2 green'], 7, 2 * 6 * 7 + 2),
            (['Game 2: 22 green, 6 blue, 7 red; ', 'Game 5: 2 green'], 5, 22 * 6 * 7 + 2),
            (['Game 2: 2 green, 6 blue, 7 red; ', 'Game 5: 22 green'], 2, 2 * 6 * 7 + 22)
        ]

        for i in content:
            print(f'+++ Testing [{self.__class__}]: {i} +++')
            self.assertEqual(i[1], cube_conundrum.CubeConundrum.solve(i[0],
                                                                      game_bag=game_bag,
                                                                      part=cube_conundrum.Part.ONE),
                             f'input value [{i[0]}] was not calculated correctly')
            self.assertEqual(i[2], cube_conundrum.CubeConundrum.solve(i[0], game_bag=game_bag,
                                                                      part=cube_conundrum.Part.TWO),
                             f'input value [{i[0]}] was not calculated correctly')
            print(f' -- -- -- -- -- -- -- -- -- -- -- -- -- -- --\n')


if __name__ == '__main__':
    unittest.main()

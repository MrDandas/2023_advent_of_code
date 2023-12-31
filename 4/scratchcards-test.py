import unittest
import scratchcards
from util.part_enum import Part


class ScratchcardsTest(unittest.TestCase):

    # def test_part_1_simple(self):
    #     content = ((['Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53'], [41, 48, 83, 86, 17],
    #                 [83, 86, 6, 31, 17, 9, 48, 53], [17, 48, 83 ,86], 8),
    #                (['Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19'], [13, 32, 20, 16, 61],
    #                 [61, 30, 68, 82, 17, 32, 24, 19], [32, 61], 2),
    #                (['Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1'], [1, 21, 53, 59, 44],
    #                 [69, 82, 63, 72, 16, 21, 14, 1], [1, 21], 2),
    #                (['Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83'], [41, 92, 73, 84, 69],
    #                 [59, 84, 76, 51, 58, 5, 54, 83], [84], 1),
    #                (['Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36'], [87, 83, 26, 28, 32],
    #                 [88, 30, 70, 12, 93, 22, 82, 36], [], 0),
    #                (['Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11'], [31, 18, 13, 56, 72],
    #                 [74, 77, 10, 23, 35, 67, 36, 11], [], 0))
    #
    #     print(f'+++ Testing [{self.__class__}]: +++')
    #     for i in content:
    #         print(f'> Input: {i}')
    #
    #         card_registry, total = scratchcards.Scratchcards.solve(i[0], part=Part.ONE)
    #         self.assertEqual(set(i[1]), card_registry[1][1], f'Winning numbers are different')
    #         self.assertEqual(set(i[2]), card_registry[1][2], f'Scratchcard numbers are different')
    #         self.assertEqual(set(i[3]), card_registry[1][3], f'Scratchcard matching numbers are different')
    #         self.assertEqual(i[4], total, f'Scratchcard value is different')
    #         print(f' -- -- -- -- -- -- -- -- -- -- -- -- -- -- --\n')

    def test_part_2_simple(self):
        # 4,2,2,1,2,0
        content = (['Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53',
                    'Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19',
                    'Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1',
                    'Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83',
                    'Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 28 32',
                    'Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11'])

        print(f'+++ Testing [{self.__class__}]: +++')
        print(f'> Input: {content}')

        processed_cards = scratchcards.Scratchcards.solve(content, part=Part.TWO)
        self.assertEqual(44, processed_cards, f'Scratchcard value is different')
        print(f' -- -- -- -- -- -- -- -- -- -- -- -- -- -- --\n')

if __name__ == '__main__':
    unittest.main()

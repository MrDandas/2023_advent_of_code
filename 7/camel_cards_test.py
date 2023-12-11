import unittest
from camel_cards import Label
from camel_cards import Card
from camel_cards import CamelCards
from camel_cards import CARDS


class CamelCardsTest(unittest.TestCase):

    # def test_part_simple(self):
    #     self.assertEqual(4, wait_for_it.WaitForIt.solve_part_1_impl(7, 9))
    #     self.assertEqual(2, wait_for_it.WaitForIt.solve_part_1_impl(3, 0))
    #     self.assertEqual(3, wait_for_it.WaitForIt.solve_part_1_impl(4, 2))
    #     self.assertEqual(2, wait_for_it.WaitForIt.solve_part_1_impl(5, 5))
    #     self.assertEqual(5, wait_for_it.WaitForIt.solve_part_1_impl(6, 3))
    #     self.assertEqual(5, wait_for_it.WaitForIt.solve_part_1_impl(6, 4))
    #     self.assertEqual(3, wait_for_it.WaitForIt.solve_part_1_impl(6, 6))
    def test_labels(self):
        self.assertEqual(Label.HIGH_CARD, CamelCards.find_labels("23456"))
        self.assertEqual(Label.HIGH_CARD, CamelCards.find_labels("A3456"))
        self.assertEqual(Label.HIGH_CARD, CamelCards.find_labels("56K78"))

        self.assertEqual(Label.ONE_PAIR, CamelCards.find_labels("J234J"))
        self.assertEqual(Label.ONE_PAIR, CamelCards.find_labels("JJ234"))
        self.assertEqual(Label.ONE_PAIR, CamelCards.find_labels("J2344"))

        self.assertEqual(Label.TWO_PAIRS, CamelCards.find_labels("22335"))
        self.assertEqual(Label.TWO_PAIRS, CamelCards.find_labels("23235"))

        self.assertEqual(Label.THREE_OF_A_KIND, CamelCards.find_labels("333QJ"))
        self.assertEqual(Label.THREE_OF_A_KIND, CamelCards.find_labels("33J3Q"))
        self.assertEqual(Label.THREE_OF_A_KIND, CamelCards.find_labels("AQ333"))

        self.assertEqual(Label.FULL_HOUSE, CamelCards.find_labels("AA333"))
        self.assertEqual(Label.FULL_HOUSE, CamelCards.find_labels("A333A"))
        self.assertEqual(Label.FULL_HOUSE, CamelCards.find_labels("Q333Q"))
        self.assertEqual(Label.FULL_HOUSE, CamelCards.find_labels("Q3Q33"))

        self.assertEqual(Label.FOUR_OF_A_KIND, CamelCards.find_labels("AAAA1"))
        self.assertEqual(Label.FOUR_OF_A_KIND, CamelCards.find_labels("1AAAA"))

        self.assertEqual(Label.FIVE_OF_A_KIND, CamelCards.find_labels("AAAAA"))


    def test_card_cmp(self):
        self.assertEqual(CARDS['T'], CARDS['T'])
        self.assertGreater(CARDS['A'], CARDS['J'])
        self.assertLess(CARDS['2'], CARDS['J'])


    def test_part_1(self):
        content = \
            """
32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
"""

        print(f'+++ Testing [{self.__class__}]: +++')
        print(f'> Input: {content}')

        self.assertEqual(483 * 5 + 684 * 4 + 28 * 3 + 220 * 2 + 765 * 1,
                         CamelCards.solve_part_1(content[1:-1].split('\n')))


if __name__ == '__main__':
    unittest.main()

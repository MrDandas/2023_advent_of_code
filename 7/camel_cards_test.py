import unittest
from camel_cards import Label
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

    def test_upgrade(self):
        """
        UPGRADES = {
          # there are 3 special cases when JJ(JJJ respectively) form another PAIR/TRIPLE
          # -> JJ XX Y can be turned into FOUR_OF_A_KIND
          # -> XXX JJ can be turned into FIVE_OF_A_KIND
          # -> JJJ XX can be turned into FIVE_OF_A_KIND
          Label.HIGH_CARD: [Label.ONE_PAIR],
          Label.ONE_PAIR: [Label.THREE_OF_A_KIND],
          Label.TWO_PAIRS: [Label.FULL_HOUSE],
          Label.THREE_OF_A_KIND: [Label.FOUR_OF_A_KIND],
          Label.FULL_HOUSE: [Label.FOUR_OF_A_KIND],
          Label.FOUR_OF_A_KIND: [Label.FIVE_OF_A_KIND]}
        """
        self.assertEqual(Label.ONE_PAIR, CamelCards.find_labels("5JK78", upgrade=True))
        self.assertEqual(Label.ONE_PAIR, CamelCards.find_labels("J2345", upgrade=True))

        self.assertEqual(Label.THREE_OF_A_KIND, CamelCards.find_labels("223J6", upgrade=True))

        self.assertEqual(Label.FULL_HOUSE, CamelCards.find_labels("2323J", upgrade=True))

        self.assertEqual(Label.FOUR_OF_A_KIND, CamelCards.find_labels("33AJJ", upgrade=True))

        self.assertEqual(Label.FOUR_OF_A_KIND, CamelCards.find_labels("333QJ", upgrade=True))
        self.assertEqual(Label.FOUR_OF_A_KIND, CamelCards.find_labels("33J3Q", upgrade=True))

        self.assertEqual(Label.FIVE_OF_A_KIND, CamelCards.find_labels("33J3J", upgrade=True))
        self.assertEqual(Label.FIVE_OF_A_KIND, CamelCards.find_labels("JJJ33", upgrade=True))

        self.assertEqual(Label.FIVE_OF_A_KIND, CamelCards.find_labels("J3333", upgrade=True))
        self.assertEqual(Label.FIVE_OF_A_KIND, CamelCards.find_labels("JJJJJ", upgrade=True))

    def test_card_cmp(self):
        self.assertEqual(CARDS['T'], CARDS['T'])
        self.assertGreater(CARDS['A'], CARDS['J'])
        self.assertLess(CARDS['J'], CARDS['2'])

    def test_part_1(self):
        content = \
            """\
            32T3K 765\n\
            T55J5 684\n\
            KK677 28\n\
            KTJJT 220\n\
            QQQJA 483\
            """

        print(f'+++ Testing [{self.__class__}]: +++')
        print(f'> Input: {content}')

        self.assertEqual(483 * 5 + 684 * 4 + 28 * 3 + 220 * 2 + 765 * 1, CamelCards.solve(content[1:-1].split('\n')))

    def test_part_2(self):
        content = \
            """\
            32T3K 765\n\
            T55J5 684\n\
            KK677 28\n\
            KTJJT 220\n\
            QQQJA 483\
            """

        print(f'+++ Testing [{self.__class__}]: +++')
        print(f'> Input: {content}')

        self.assertEqual(220 * 5 + 483 * 4 + 684 * 3 + 28 * 2 + 765 * 1,
                         CamelCards.solve(content[1:-1].split('\n'), upgrade_joker=True))


if __name__ == '__main__':
    unittest.main()

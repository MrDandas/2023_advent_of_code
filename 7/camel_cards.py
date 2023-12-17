import functools
import re
from enum import Enum
from timeit import default_timer


class Label(Enum):
    HIGH_CARD = 1  # 5 groups
    ONE_PAIR = 2  # 2 groups
    TWO_PAIRS = 3  # 3 groups
    THREE_OF_A_KIND = 4  # 2 groups
    FULL_HOUSE = 5  # 2 groups
    FOUR_OF_A_KIND = 6  # 2 groups
    FIVE_OF_A_KIND = 7  # 1 group


UPGRADES = {
    Label.HIGH_CARD: Label.ONE_PAIR,
    Label.ONE_PAIR: Label.THREE_OF_A_KIND,
    Label.TWO_PAIRS: Label.FULL_HOUSE,
    Label.THREE_OF_A_KIND: Label.FOUR_OF_A_KIND,
    Label.FULL_HOUSE: Label.FOUR_OF_A_KIND,
    Label.FOUR_OF_A_KIND: Label.FIVE_OF_A_KIND,
    Label.FIVE_OF_A_KIND: Label.FIVE_OF_A_KIND
}

CARDS = {
    'J': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'T': 10,
    'Q': 11,
    'K': 12,
    'A': 13,
}

HAND_SIZE = 5


class CamelCards(object):

    @staticmethod
    def compare_hands(left_hand: tuple[str, Label, int], right_hand: tuple[str, Label, int]):
        diff = left_hand[1].value - right_hand[1].value

        # same labels, compare the cards
        if diff == 0:
            for left_card, right_card in zip(left_hand[0], right_hand[0]):
                if left_card == right_card:
                    continue
                else:
                    return CARDS[left_card] - CARDS[right_card]
        else:
            return diff

    @staticmethod
    def find_labels(hand: str, upgrade: bool = False):
        sorted_hand = ''.join(sorted(hand))

        groups = [m.group(0) for m in re.finditer(r"(\w)\1*", sorted_hand)]

        # HIGH_CARD = 1         # 5 groups (1,1,1,1,1)
        # ONE_PAIR = 2          # 4 groups (2,1,1,1)
        # TWO_PAIRS = 3         # 3 groups (2,2,1)
        # THREE_OF_A_KIND = 4   # 3 groups (3,1,1)
        # FULL_HOUSE = 5        # 2 groups (3,2)
        # FOUR_OF_A_KIND = 6    # 2 groups (4,1)
        # FIVE_OF_A_KIND = 7    # 1 group  (5)
        label = None

        if len(groups) == 1:
            label = Label.FIVE_OF_A_KIND
        elif len(groups) == 2:
            if len(groups[0]) == 4 or len(groups[1]) == 4:
                label = Label.FOUR_OF_A_KIND
            else:  # 3
                label = Label.FULL_HOUSE
        elif len(groups) == 3:
            if len(groups[0]) == 3 or len(groups[1]) == 3 or len(groups[2]) == 3:
                label = Label.THREE_OF_A_KIND
            else:  # 2
                label = Label.TWO_PAIRS
        elif len(groups) == 4:
            label = Label.ONE_PAIR
        elif len(groups) == 5:
            label = Label.HIGH_CARD

        print_str = f'{hand} -> {groups} -> {label}'
        if upgrade:
            # there are special cases when JJ(JJJ respectively) form another PAIR/TRIPLE
            # -> JJ X Y Z   ->  XXXX Y  :   THREE_OF_A_KIND
            # -> JJ XX Y    ->  XXXX Y  :   FOUR_OF_A_KIND
            # -> JJ XXX     ->  XXXXX   :   FIVE_OF_A_KIND
            # -> JJJ X Y    ->  XXXX Y  :   FOUR_OF_A_KIND
            # -> JJJ XX     ->  XXXXX   :   FIVE_OF_A_KIND

            j_count = len([i for i, letter in enumerate(sorted_hand) if letter == 'J'])
            orig_label = label

            if j_count == 1 or j_count == 4 or j_count == 5:
                label = UPGRADES[label]
            elif j_count == 2:
                if len(groups) == 4:
                    label = Label.THREE_OF_A_KIND
                if len(groups) == 3:
                    label = Label.FOUR_OF_A_KIND
                if len(groups) == 2:
                    label = Label.FIVE_OF_A_KIND
            elif j_count == 3:
                if len(groups) == 3:
                    label = Label.FOUR_OF_A_KIND
                if len(groups) == 2:
                    label = Label.FIVE_OF_A_KIND

            print_str = f'{hand} -> {groups} -> {label} (original: {orig_label})'

        #print(print_str)

        return label

    @staticmethod
    def solve(lines: list[str], upgrade_joker: bool = False):
        hands = [
            # (original_hand, label, bet)
        ]
        for line in lines:
            line_split = line.split()
            hands.append((line_split[0], CamelCards.find_labels(line_split[0], upgrade_joker), int(line_split[1])))

        sorted_hands = sorted(hands, key=functools.cmp_to_key(CamelCards.compare_hands), reverse=True)

        res = 0
        for i in range(0, len(sorted_hands)):
            res += sorted_hands[i][2] * (len(sorted_hands) - i)

        return res


if __name__ == '__main__':
    with open('input.txt') as file:
        input_lines = file.readlines()

        start = default_timer()
        print(f'Solution PART1: {CamelCards.solve(input_lines)}; took: {default_timer() - start}')
        print(f'Solution PART2: {CamelCards.solve(input_lines, upgrade_joker=True)}; took: {default_timer() - start}')

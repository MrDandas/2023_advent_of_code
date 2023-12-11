import functools
import re
from enum import Enum
from functools import total_ordering


@total_ordering
class OrderedEnum(Enum):
    def __eq__(self, other):
        if isinstance(other, Label):
            return self.value == other.value

        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Label):
            return self.value > other.value

        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Label):
            return self.value < other

        return NotImplemented


class Label(OrderedEnum):
    HIGH_CARD = 1  # 5 groups
    ONE_PAIR = 2  # 2 groups
    TWO_PAIRS = 3  # 3 groups
    THREE_OF_A_KIND = 4  # 2 groups
    FULL_HOUSE = 5  # 2 groups
    FOUR_OF_A_KIND = 6  # 2 groups
    FIVE_OF_A_KIND = 7  # 1 group

CARDS = {
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'T': 10,
    'J': 11,
    'Q': 12,
    'K': 13,
    'A': 14,
}


class Card(OrderedEnum):
    TWO = '2'
    THREE = '3'
    FOUR = '4'
    FIVE = '5'
    SIX = '6'
    SEVEN = '7'
    EIGHT = '8'
    NINE = '9'
    TEN = 'T', 10
    JACK = 'J', 11
    QUEEN = 'Q', 12
    KING = 'K', 13
    ACE = 'A', 14

    def __init__(self, rep, val=None):
        self.rep = rep
        self.val = val if val is not None else int(rep)


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
    def find_labels(hand: str):
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

        # print(f'{hand} -> {groups} -> {label}')

        return label


    @staticmethod
    def solve_part_1(lines: list[str]):
        hands = [
            # (original_hand, label, bet)
        ]
        for line in lines:
            line_split = line.split()
            hands.append((line_split[0], CamelCards.find_labels(line_split[0]), int(line_split[1])))

        sorted_hands = sorted(hands, key=functools.cmp_to_key(CamelCards.compare_hands), reverse=True)

        res = 0
        for i in range(0, len(sorted_hands)):
            print(sorted_hands[i])
            res += sorted_hands[i][2] * (len(sorted_hands) - i)

        return res

if __name__ == '__main__':
    with open('input.txt') as file:
        input_lines = file.readlines()

        print(f'Solution Part.ONE: {CamelCards.solve_part_1(input_lines)}')
        # print(f'Solution Part.TWO: {CamelCards.solve_part_2(input_lines)}')

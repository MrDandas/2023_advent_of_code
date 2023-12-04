from typing import Tuple, Dict, Set, Union, Any

from util.part_enum import Part


class Scratchcards(object):

    @staticmethod
    def parse_line(*, line: str, part: Part) -> tuple[str, set[int], set[int]]:
        # Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
        card_id = line.split(':')[0].split()[1]
        winning_numbers = set([int(s) for s in line.split(':')[1].split('|')[0].split() if s.isdigit()])
        my_numbers = set([int(s) for s in line.split(':')[1].split('|')[1].split() if s.isdigit()])

        return card_id, winning_numbers, my_numbers

    @staticmethod
    def solve(lines: list[str], *, part: Part = Part.ONE):
        """
        For example:


        Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
        Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
        Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
        Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
        Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
        Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
        In the above example, card 1 has five winning numbers (41, 48, 83, 86, and 17) and eight numbers you have (83, 86, 6, 31, 17, 9, 48, and 53). Of the numbers you have, four of them (48, 83, 17, and 86) are winning numbers! That means card 1 is worth 8 points (1 for the first match, then doubled three times for each of the three matches after the first).

        Card 2 has two winning numbers (32 and 61), so it is worth 2 points.
        Card 3 has two winning numbers (1 and 21), so it is worth 2 points.
        Card 4 has one winning number (84), so it is worth 1 point.
        Card 5 has no winning numbers, so it is worth no points.
        Card 6 has no winning numbers, so it is worth no points.
        So, in this example, the Elf's pile of scratchcards is worth 13 points.
        """
        card_registry = {}
        cards_to_process = []
        for line in lines:
            card_id, winning, my_numbers = Scratchcards.parse_line(line=line, part=Part.ONE)
            matches = winning & my_numbers
            card_sum = len(matches) if len(matches) < 2 else pow(2, len(matches) - 1)
            card_registry[int(card_id)] = (int(card_id), winning, my_numbers, matches, card_sum)
        cards_to_process.extend(card_registry.values())

        if part == Part.ONE:
            part_1_sum = sum([x[4] for x in cards_to_process])
            return card_registry, part_1_sum

        if part == Part.TWO:
            if len(cards_to_process) == 0:
                return card_registry, 0

            processed_count = 0
            while processed_count < len(cards_to_process):
                card = cards_to_process[processed_count]
                # print(f'+ [{processed_count}] -- Processing card {card[0]}; [{len(card[3])}] matches')

                # add new copies to the queue
                if len(card[3]) > 0:
                    # card no.1 is on index 0
                    card_first = card[0] + 1
                    card_last = min(card[0] + len(card[3]), len(card_registry))

                    for i in range(card_first, card_last + 1):
                        # print(f'+ [{processed_count}] -- Adding card {card_registry[i][0]}')
                        cards_to_process.append(card_registry[i])

                processed_count += 1

            return processed_count


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    with open('input.txt') as file:
        input_lines = file.readlines()

        print(f'Solution Part.ONE: {Scratchcards.solve(input_lines, part=Part.ONE)[1]}')
        print(f'Solution Part.TWO: {Scratchcards.solve(input_lines, part=Part.TWO)}')

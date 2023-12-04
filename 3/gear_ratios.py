from util.part_enum import Part

SPECIAL_CHARS = "!\"#$%&\'()*+,-/:;<=>?@[\\]^_`{|}~"
SCAN_AREA = (1, 1)


class GearRatios(object):
    """
    parses the input lines producing 2 tuples - numbers(row, l_idx, r_idx, value) and special_chars(row, idx)
    """

    @staticmethod
    def parse_input(*, input_lines: list[str]) -> tuple[(int, int, int, int), (int, int)]:

        numbers = []  # (row, l_idx, r_idx, value)
        special_characters = []  # (row, idx)
        for i in range(0, len(input_lines)):
            l_idx, r_idx = -1, -1
            in_number = False
            for j in range(0, len(input_lines[i])):
                if input_lines[i][j].isdigit():
                    # save indices
                    if in_number:
                        r_idx = j
                    else:
                        l_idx = j
                        in_number = True
                else:
                    in_number = False

                    if l_idx != -1:

                        # case, when number has 1 digit
                        if r_idx == -1:
                            r_idx = l_idx

                        # extract the number
                        numbers.append((i, l_idx, r_idx, int(input_lines[i][l_idx:r_idx + 1])))

                        # reset indices
                        l_idx, r_idx = -1, -1

                    # if we hit special char, mark its position
                    if input_lines[i][j] in SPECIAL_CHARS:
                        special_characters.append((i, j))

        return numbers, special_characters

    @staticmethod
    def solve(lines: list[str], *, part: Part = Part.ONE) -> tuple:

        """
        467..114..
        ...*......
        ..35..633.
        ......#...
        617*......
        .....+.58.
        ..592.....
        ......755.
        ...$.*....
        .664.598..

        In this schematic, two numbers are not part numbers because they are not adjacent to a symbol: 114 (top right) and 58 (middle right).
        Every other number is adjacent to a symbol and so is a part number; their sum is 4361.



        1* 0 1 2 3 4 5 6     00 01 02 03  04  05 06     row_idx - 1 [l_id - 1 ; r_id +1]
        2* 0 1 2 3 4 5 6 ==> 00 02 04 06 [08] 10 12 ==> row_idx     [l_id - 1 ; r_id +1]
        3* 0 1 2 3 4 5 6     00 03 06 09  12  15 18     row_idx + 1 [l_id - 1 ; r_id +1]

           . . 3 . . . .
           . . . . . . .
           . . . . . . .
        """

        numbers, special_characters = GearRatios.parse_input(input_lines=lines)
        numbers_near_special_chars = set()
        phase_1_sum = 0
        for sc in special_characters:

            # calculate row/line distances
            row_limits = (max(0, sc[0] - SCAN_AREA[0]), min(len(lines), sc[0] + SCAN_AREA[0]))
            line_limits = (max(0, sc[1] - SCAN_AREA[1]), min(len(lines[0]), sc[1] + SCAN_AREA[1]))

            # mark in number in vicinity
            # cases:
            # 1 - number ends in area           ==> line_limits[0] <= n[2] <= line_limits[1]
            # 2 - number starts in area         ==> line_limits[0] <= n[1] <= line_limits[1]
            # 3 - number is bigger then area    ==> n[1] <= line_limits[0] and n[2] >= line_limits[1]

            for n in numbers:
                row_fit = row_limits[0] <= n[0] <= row_limits[1]
                case_1 = line_limits[0] <= n[2] <= line_limits[1]
                case_2 = line_limits[0] <= n[1] <= line_limits[1]
                case_3 = n[1] <= line_limits[0] and n[2] >= line_limits[1]

                if row_fit and (case_1 or case_2 or case_3):
                    numbers_near_special_chars.add(n)

        phase_1_sum = sum([x[3] for x in numbers_near_special_chars])
        print(f'Numbers: {numbers}')
        print(f'Special Characters: {special_characters}')
        print(f'Part 1 Sum: {phase_1_sum}')

        if part == Part.ONE:
            return numbers, special_characters, phase_1_sum


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    with open('input.txt') as file:
        input_lines = file.readlines()

        game_bag = {'red': 12, 'green': 13, 'blue': 14}

        print(f'Solution Part.ONE: {GearRatios.solve(input_lines, part=Part.ONE)}')
        print(f'Solution Part.TWO: {GearRatios.solve(input_lines, part=Part.TWO)}')

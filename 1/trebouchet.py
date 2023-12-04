from util.part_enum import Part


class Trebouchet(object):

    @staticmethod
    def solve(inputs: list[str], part: Part) -> int:

        numbers: dict[str, int] = {
            "1": 1,
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9,
        }

        if part is Part.TWO:
            numbers |= {
                "one": 1,
                "two": 2,
                "three": 3,
                "four": 4,
                "five": 5,
                "six": 6,
                "seven": 7,
                "eight": 8,
                "nine": 9
            }

        calibration_sum = 0

        for line in inputs:
            line = line.strip()

            l_idx = len(line)
            l_val = ''

            for value in numbers:
                idx = line.find(value)
                if l_idx > idx >= 0:
                    l_idx = idx
                    l_val = value

            r_idx = -1
            r_val = ''

            for value in numbers:
                idx = line.rfind(value)
                if idx > r_idx and idx >= 0:
                    r_idx = idx
                    r_val = value

            if r_val == '' and l_val == '':
                continue

            calibration_sum += int(numbers[l_val]) * 10 + int(numbers[r_val])

        return calibration_sum


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    with open('input.txt') as file:
        lines = file.readlines()

        print(f'Solution Part.ONE: {Trebouchet.solve(lines, Part.ONE)}')
        print(f'Solution Part.TWO: {Trebouchet.solve(lines, Part.TWO)}')

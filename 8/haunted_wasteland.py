import re
from timeit import default_timer


class HauntedWasteland(object):

    @staticmethod
    def loop(steps):
        while True:
            yield from steps

    @staticmethod
    def walk(directions: dict[str, tuple[str, str]], steps: list[int]):

        counter = 0
        pos = 'AAA'
        for i in HauntedWasteland.loop(steps):
            print(f'[{counter}] : {pos} -> {directions[pos]} ---> {directions[pos][i]}')
            if pos == 'ZZZ':
                break
            counter += 1
            pos = directions[pos][i]
        return counter

    @staticmethod
    def solve(lines: list[str]):
        steps = [1 if char == 'R' else 0 for char in lines[0].strip()]
        directions = {}
        for line in lines[1:]:
            if line[0].isalpha():
                # AAA = (BBB, CCC)
                beg, lhs, rhs = re.findall(r"[A-Z]+", line)
                directions[beg] = (lhs, rhs)

        return HauntedWasteland.walk(directions, steps)


if __name__ == '__main__':
    with open('input.txt') as file:
        input_lines = file.readlines()

        start = default_timer()
        print(f'Solution PART1: {HauntedWasteland.solve(input_lines)}; took: {default_timer() - start} ms')

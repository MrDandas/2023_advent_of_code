import math
import re
from timeit import default_timer
from collections.abc import Callable
from math import lcm


class HauntedWasteland(object):

    @staticmethod
    def loop(steps):
        while True:
            yield from steps

    @staticmethod
    def walk(directions: dict[str, tuple[str, str]], steps: list[int], starting_pos: str,
             end_fn: Callable[[str], bool]):

        counter = 0
        pos = starting_pos
        for i in HauntedWasteland.loop(steps):
            #print(f'[{counter}] : {pos} -> {directions[pos]} ---> {directions[pos][i]}')
            if end_fn(pos):
                break
            counter += 1
            pos = directions[pos][i]
        return counter

    @staticmethod
    def parse(lines: list[str]):
        steps_ = [1 if char == 'R' else 0 for char in lines[0].strip()]
        directions_ = {}
        for line in lines[1:]:
            if line[0].isalpha():
                # AAA = (BBB, CCC)
                beg, lhs, rhs = re.findall(r"[A-Z0-9]+", line)
                directions_[beg] = (lhs, rhs)

        return steps_, directions_

    @staticmethod
    def solve(lines: list[str]):
        steps, directions = HauntedWasteland.parse(lines)

        is_end: Callable[[str], bool] = lambda x: (x == 'ZZZ')

        return HauntedWasteland.walk(directions, steps, 'AAA', is_end)

    @staticmethod
    def solve_2(lines: list[str]):
        steps, directions = HauntedWasteland.parse(lines)
        all_starts = [d for d in directions.keys() if d[2] == 'A']
        is_end: Callable[[str], bool] = lambda x: (x[2] == 'Z')

        start_to_cycle = {}
        for s in all_starts:
            start_to_cycle[s] = HauntedWasteland.walk(directions, steps, s, is_end)

        return math.lcm(*start_to_cycle.values())


if __name__ == '__main__':
    with open('input.txt') as file:
        input_lines = file.readlines()
        start = default_timer()

        print(f'Solution PART 1: {HauntedWasteland.solve(input_lines)}; took: {default_timer() - start} ms')
        print(f'Solution PART 2: {HauntedWasteland.solve_2(input_lines)}; took: {default_timer() - start} ms')

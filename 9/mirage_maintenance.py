from timeit import default_timer


class MirageMaintenance(object):

    @staticmethod
    def parse(lines: list[str]) -> list[list[int]]:
        import re
        return [list(map(int, re.findall(r"-?\d+", x))) for x in lines]

    @staticmethod
    def find_reducts(serie: list[int], accumulator: list[list[int]]):

        new_series = [0 for i in range(len(serie) - 1)]
        for i in range(1, len(serie)):
            new_series[i - 1] = (serie[i] - serie[i - 1])

        if all(x == 0 for x in new_series):
            return

        accumulator.append(new_series)

        MirageMaintenance.find_reducts(new_series, accumulator)

    @staticmethod
    def solve_1(series: list[list[int]]):

        grand_sum = 0
        for i in range(0, len(series)):
            accumulator = [series[i]]
            MirageMaintenance.find_reducts(series[i], accumulator)

            for a in accumulator:
                grand_sum += a[-1]

        return grand_sum

    @staticmethod
    def solve_2(series: list[list[int]]):
        grand_sum = 0
        for i in range(0, len(series)):
            accumulator = [series[i]]
            MirageMaintenance.find_reducts(series[i], accumulator)

            part_sum = 0
            for j in range(0, len(accumulator)):
                part_sum = accumulator[len(accumulator) - j - 1][0] - part_sum
            grand_sum += part_sum

        return grand_sum


if __name__ == '__main__':
    with open('input.txt') as file:
        input_lines = file.readlines()
        start = default_timer()

        series = MirageMaintenance.parse(input_lines)

        print(f'Solution PART 1: {MirageMaintenance.solve_1(series)}; took: {default_timer() - start} ms')
        print(f'Solution PART 2: {MirageMaintenance.solve_2(series)}; took: {default_timer() - start} ms')

from util.part_enum import Part

COLORS = [
    'red',
    'green',
    'blue'
]


class CubeConundrum(object):

    @staticmethod
    def parse_line(line: str) -> (int, list[(str, int)]):
        line = line.strip()
        line_parts = line.partition(':')
        game_id = [int(s) for s in line_parts[0].split() if s.isdigit()][0]  # Game $ID

        cubes = []
        for game_parts in line_parts[2].partition(';'):
            if game_parts == ';':
                continue

            cube_count = -1
            for s in game_parts.split():

                if s.isdigit():
                    cube_count = int(s)
                    continue

                for c in COLORS:
                    if c in s:
                        cubes.append((c, cube_count))
                        cube_count = -1
                        break

        return game_id, cubes

    """
    :returns 0 if game is not possible with given 'game_bag'
    :returns n, where n is game_id of game if it was possible to play with given 'game_bag' 
    """

    @staticmethod
    def part_1_validate_game(*, game_bag: dict[str, int], game_id: int, cubes: tuple[str, int]) -> int:
        for color, cube_count in cubes:
            if game_bag[color] < cube_count:
                return 0

        return game_id

    @staticmethod
    def part_2_find_lowest_cube_sets(*, cubes: tuple[str, int]) -> int:

        fewest_cubes = {}

        for color, cube_count in cubes:
            try:
                fewest_cubes[color] = max(fewest_cubes[color], cube_count)
            except KeyError:
                fewest_cubes[color] = cube_count

        from functools import reduce
        return reduce(lambda x, y: x*y, fewest_cubes.values())

    @staticmethod
    def solve(inputs: list[str], *, game_bag: dict[str, int], part: Part = Part.ONE) -> int:

        """
        Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
        Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
        Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
        Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
        Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
        """
        sum_of_game_ids = 0
        power_of_game_ids = 0
        for line in inputs:
            game_id, cubes = CubeConundrum.parse_line(line)

            if part == Part.ONE:
                sum_of_game_ids += CubeConundrum.part_1_validate_game(game_bag=game_bag, game_id=game_id, cubes=cubes)
            if part == Part.TWO:
                power_of_game_ids += CubeConundrum.part_2_find_lowest_cube_sets(cubes=cubes)

        return sum_of_game_ids if part == Part.ONE else power_of_game_ids


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    with open('input.txt') as file:
        lines = file.readlines()

        game_bag = {'red': 12, 'green': 13, 'blue': 14}

        print(f'Solution Part.ONE: {CubeConundrum.solve(lines, game_bag=game_bag, part=Part.ONE)}')
        print(f'Solution Part.TWO: {CubeConundrum.solve(lines, game_bag=game_bag, part=Part.TWO)}')

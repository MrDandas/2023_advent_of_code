import concurrent
from concurrent.futures import ThreadPoolExecutor


class Almanac(object):
    """
    seeds: 79 14 55 13

    seed-to-soil map:
    50 98 2
    52 50 48

    soil-to-fertilizer map:
    0 15 37
    37 52 2
    39 0 15

    fertilizer-to-water map:
    49 53 8
    0 11 42
    42 0 7
    57 7 4

    water-to-light map:
    88 18 7
    18 25 70

    light-to-temperature map:
    45 77 23
    81 45 19
    68 64 13

    temperature-to-humidity map:
    0 69 1
    1 0 69

    humidity-to-location map:
    60 56 37
    56 93 4

    Seed 79, soil 81, fertilizer 81, water 81, light 74, temperature 78, humidity 78, location 82.
    Seed 14, soil 14, fertilizer 53, water 49, light 42, temperature 42, humidity 43, location 43.
    Seed 55, soil 57, fertilizer 57, water 53, light 46, temperature 82, humidity 82, location 86.
    Seed 13, soil 13, fertilizer 52, water 41, light 34, temperature 34, humidity 35, location 35.

    map:
        dst_1 src_1 len
        dst_2 src_2 len
    """

    @staticmethod
    def solve_part_1(lines: list[str]):
        seed_locations = []

        almanac, seeds = Almanac.parse_input(lines)

        for seed in seeds:
            print(f'$^\n + Almanac : New Seed [{seed}] Entering transformation')

            seed_location = seed
            for garden_maps in almanac:
                for row in garden_maps:
                    if row[1] <= seed_location < row[1] + row[2]:
                        old = seed_location
                        seed_location += row[0] - row[1]
                        print(f' + Almanac : Seed Location Changed [{old}] ===> [{seed_location}]')
                        break

            seed_locations.append(seed_location)

        return seed_locations

    @staticmethod
    def solve_part_2_brute(lines: list[str]):

        almanac, seeds = Almanac.parse_input(lines)

        min_seed = seeds[0]

        for i in range(0, len(seeds) // 2):
            seed_range = range(seeds[2 * i], seeds[2 * i] + seeds[2 * i + 1])
            for seed in seed_range:
                seed_location = seed
                for garden_maps in almanac:
                    for row in garden_maps:
                        if row[1] <= seed_location < row[1] + row[2]:
                            seed_location += row[0] - row[1]
                            break

                min_seed = min(min_seed, seed_location)

        return min_seed

    @staticmethod
    def solve_part_2(lines):

        almanacs, seeds = Almanac.parse_input(lines)

        seed_locations = []
        for i in range(0, len(seeds), 2):
            ranges = [[seeds[i], seeds[i + 1] + seeds[i]]]
            results = []

            for amap in almanacs:
                while ranges:
                    current_seed_range_start, current_seed_range_end = ranges.pop()

                    for dest, amap_start, range_length in amap:
                        offset = dest - amap_start
                        amap_end = amap_start + range_length

                        if amap_end <= current_seed_range_start or current_seed_range_end <= amap_start:
                            continue

                        if current_seed_range_start < amap_start:
                            ranges.append([current_seed_range_start, amap_start])
                            current_seed_range_start = amap_start

                        if amap_end < current_seed_range_end:
                            ranges.append([amap_end, current_seed_range_end])
                            current_seed_range_end = amap_end

                        results.append([current_seed_range_start + offset, current_seed_range_end + offset])
                        break
                    else:
                        results.append([current_seed_range_start, current_seed_range_end])

                ranges = results
                results = []

            seed_locations += ranges

        return min(loc[0] for loc in seed_locations)

    @staticmethod
    def parse_input(lines: list[str]):
        almanac_str_maps = [
            'seed-to-soil',
            'soil-to-fertilizer',
            'fertilizer-to-water',
            'water-to-light',
            'light-to-temperature',
            'temperature-to-humidity',
            'humidity-to-location'
        ]

        almanac = []
        seeds = []

        map_idx = 0
        for l in lines:
            l.strip()
            if len(l) <= 1:
                continue
            if l.find('seeds') != -1:
                seeds = [int(s) for s in l.split(':')[1].split() if s.isdigit()]
                continue

            if l[0].isalpha():
                for i in range(0, len(almanac_str_maps)):
                    if l.find(almanac_str_maps[i]) != -1:
                        map_idx = i
                        almanac.insert(map_idx, [])
                        continue

            if l[0].isdigit():
                row = [int(s) for s in l.split() if s.isdigit()]

                """
                [
                    [
                        [dest_start, source_start, len],
                        [dest_start, source_start, len],
                        [dest_start, source_start, len]
                    ],
                    [
                        [dest_start, source_start, len],
                        [dest_start, source_start, len],
                        [dest_start, source_start, len]
                    ]
                    ...                    
                ]
                """
                almanac[map_idx].append([row[0], row[1], row[2]])

                continue

        return almanac, seeds


if __name__ == '__main__':
    with open('input.txt') as file:
        input_lines = file.readlines()

        # print(f'Solution Part.ONE: {min(Almanac.solve_part_1(input_lines))}')
        # print(f'Solution Part.TWO: {Almanac.solve_part_2_brute(input_lines)}')
        print(f'Solution Part.TWO: {Almanac.solve_part_2(input_lines)}')

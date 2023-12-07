import math


class WaitForIt(object):

    @staticmethod
    def solve_part_1_impl(time, distance):
        # length = power * ( time - power )
        # max possible length is where 1.derivation of function
        #  [y=-x^2 + x*t || length = - power^2 + power*time] is equal 0
        # max: 2x + t = 0 ==> 2*power - time = 0 => time = 2 * power => power = time / 2
        # max_length = ( time / 2 ) * ( time - time / 2) => max_length = ( time / 2 ) ^ 2
        # my equation: -2 * power^2 + time * power - record_distance
        # roots of quadratic equation: x = (-b ± √ (b2 - 4ac) )/2a
        # my roots : power = (-time + sqrt(power(time, 2) - 4 * (-2) * (-record_distance)) / 2 * (-2)

        # x=b+- sqrt(b**2 - 4ac) / 2a
        # x1-x2: x1-2=sqrt(b**2 - 4c) ==> x1-2 = (time**2 - 4 * distance)

        delta = math.sqrt(time ** 2.0 - 4.0 * distance)
        x1 = math.ceil((time + delta) / 2.0 - 1.0)
        x2 = math.floor((time - delta) / 2.0 + 1.0)

        return x1 - x2 + 1

    @staticmethod
    def solve_part_1(lines: list[str]):
        race_times = [int(s) for s in lines[0].split() if s.isdigit()]
        race_records = [int(s) for s in lines[1].split() if s.isdigit()]

        total = 1
        for t, r in zip(race_times, race_records):
            print(f'total: {total}')
            total *= WaitForIt.solve_part_1_impl(t, r)

        return total


if __name__ == '__main__':
    with open('input.txt') as file:
        input_lines = file.readlines()

        print(f'Solution Part.ONE: {WaitForIt.solve_part_1(input_lines)}')

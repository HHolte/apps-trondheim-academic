from re import split
from functools import reduce


def solve_second_task(data):
    summ = 0
    for line in data:
        line_stripped = line.strip()
        id, game = split(":", line_stripped[4:])
        summ += get_power_of_set(game)
    return summ


def get_power_of_set(game):
    minimum_set = {"red": 0, "blue": 0, "green": 0}
    cubes = split("; |,", game)
    for cube_type in cubes:
        n_cubes, color = cube_type.strip().split(" ")
        minimum_set[color] = int(n_cubes) if int(n_cubes) > minimum_set[color] else minimum_set[color]
    minimum_set_power = reduce(lambda x, y: x * y, minimum_set.values())
    return minimum_set_power


def main():
    data = open("day2/test_data.txt")

    solution = solve_second_task(data)
    print("Solution second task: ", solution)

    data.close()


if __name__ == "__main__":
    main()

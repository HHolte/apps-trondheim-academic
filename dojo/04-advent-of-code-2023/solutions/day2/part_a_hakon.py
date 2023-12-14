from re import split

def solve_first_task(data, cube_configuration: dict[str, int]):
    cube_configuration = {
        "red": 12,
        "green": 13,
        "blue": 14,
    }
    summ = 0
    for line in data:
        line_stripped = line.strip()
        id, game = split(":", line_stripped[4:])
        summ += int(id) if game_is_possible_with_configuration(game, cube_configuration) else 0
    return summ


def game_is_possible_with_configuration(game: str, cube_configuration: dict[str, int]):
    cubes = split("; |,", game)
    for cube_type in cubes:
        n_cubes, color = cube_type.strip().split(" ")
        if int(n_cubes) > cube_configuration[color]:
            return False
    return True

def main():
    data = open("day2/test_data.txt")

    solution = solve_first_task(data)
    print("Solution first task: ", solution)

    data.close()


if __name__ == "__main__":
    main()

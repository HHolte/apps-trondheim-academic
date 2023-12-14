from day6.part_a_hakon import get_number_of_ways_to_win


def solve_first_task(data: str):
    times = data.readline().split(":")[1].strip().split(" ")
    distances = data.readline().split(":")[1].strip().split(" ")
    time = int("".join(number for number in times if number != ""))
    distance = int("".join(number for number in distances if number != ""))
    return get_number_of_ways_to_win(time, distance)


def main():
    data = open("day6/test_data.txt", "r")

    solution = solve_first_task(data)
    print("Solution to second task: ", solution)

    data.close()


if __name__ == "__main__":
    main()

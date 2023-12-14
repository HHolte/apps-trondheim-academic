def get_number_of_ways_to_win(time: int, distance: int):
    for i in range(1, time):
        if i * (time - i) > distance:
            return (time + 1) - 2 * i
    return 0


def solve_first_task(data: str):
    times = data.readline().split(":")[1].strip().split(" ")
    distances = data.readline().split(":")[1].strip().split(" ")
    times = [int(element) for element in times if element != ""]
    distances = [int(element) for element in distances if element != ""]
    target_value = 1
    for time, distance in zip(times, distances):
        target_value *= get_number_of_ways_to_win(time, distance)
    return target_value


def main():
    data = open("day6/test_data.txt", "r")

    solution = solve_first_task(data)
    print("Solution to first task: ", solution)

    data.close()


if __name__ == "__main__":
    main()

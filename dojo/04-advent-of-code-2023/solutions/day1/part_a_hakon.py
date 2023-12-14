def solve_first_task(file):
    summ = 0
    for line in file:
        number = ""
        for value in line:
            if value.isdigit():
                number += value
                break
        for value in line[::-1]:
            if value.isdigit():
                number += value
                break
        summ += int(number)
    return summ


def main():
    data = open("day1/test_data.txt", "r")

    solution = solve_first_task(data)
    print("Solution first task: ", solution)

    data.close()


if __name__ == "__main__":
    main()

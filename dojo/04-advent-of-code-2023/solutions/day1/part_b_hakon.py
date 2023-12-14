from enum import Enum
from re import finditer


class StringToNumber(Enum):
    one = 1
    two = 2
    three = 3
    four = 4
    five = 5
    six = 6
    seven = 7
    eight = 8
    nine = 9


def solve_second_task(file):
    summ = 0
    for line in file:
        (first_index, first_number), (last_index, last_number) = get_string_numbers(line)
        for i in range(len(line)):
            if line[i].isdigit():
                if first_index == -1 or i < first_index:
                    first_index = i
                    first_number = line[i]
                if last_index == -1 or i > last_index:
                    last_index = i
                    last_number = line[i]
        number = str(first_number) + str(last_number)
        summ += int(number)
    return summ


def get_string_numbers(string: str):
    index_and_value = {}
    for name in StringToNumber._member_names_:
        if name in string:
            indices_of_name = [index.start() for index in finditer(name, string)]
            for index in indices_of_name:
                index_and_value[index] = StringToNumber[name].value
    if len(index_and_value) == 0:
        return (-1, 0), (-1, 0)
    first_index = min(index_and_value.keys())
    last_index = max(index_and_value.keys())
    first_number = index_and_value[first_index]
    last_number = index_and_value[last_index]
    return (first_index, first_number), (last_index, last_number)


def main():
    data = open("day1/test_data.txt", "r")

    solution = solve_second_task(data)
    print("Solution second task: ", solution)

    data.close()


if __name__ == "__main__":
    main()

def solve_second_task(data):
    first_line = data.readline()
    first_line_stripped = first_line.strip()
    length_of_lines = len(first_line_stripped)
    prev_numbers, prev_indices, prev_symbol_indices = get_numbers_and_symbols(length_of_lines, first_line_stripped)
    prev_symbol_indices = {index: [] for index in prev_symbol_indices}
    summ = 0
    for line in data:
        line_stripped = line.strip()
        numbers, indices, symbol_indices = get_numbers_and_symbols(length_of_lines, line_stripped)
        symbol_indices = {index: [] for index in symbol_indices}

        # Find adjacent numbers in current and below line to symbols in top line
        for symbol_index in prev_symbol_indices.keys():
            for index, number in zip(prev_indices + indices, prev_numbers + numbers):
                if index - symbol_index == 1 or (0 <= symbol_index - index <= len(number)):
                    prev_symbol_indices[symbol_index].append(number)

        # Find adjacent numbers in above line to symbols in bottom line
        for symbol_index in symbol_indices.keys():
            for index, number in zip(prev_indices, prev_numbers):
                if index - symbol_index == 1 or (0 <= symbol_index - index <= len(number)):
                    symbol_indices[symbol_index].append(number)

        # Find gears in top line
        for index, adjacent_numbers in prev_symbol_indices.items():
            if len(adjacent_numbers) == 2:
                summ += int(adjacent_numbers[0]) * int(adjacent_numbers[1])

        # Move "window": bottom line becomes top line
        prev_numbers, prev_indices, prev_symbol_indices = numbers, indices, symbol_indices

    # Do checks within final line
    for symbol_index in prev_symbol_indices.keys():
        for index, number in zip(prev_indices, prev_numbers):
            if index - symbol_index == 1 or (0 <= symbol_index - index <= len(number)):
                prev_symbol_indices[symbol_index].append(number)

    for index, adjacent_numbers in prev_symbol_indices.items():
        if len(adjacent_numbers) == 2:
            summ += int(adjacent_numbers[0]) * int(adjacent_numbers[1])

    return summ


def get_numbers_and_symbols(length_of_line, line):
    numbers = []
    indices = []
    symbol_indices = []
    number = ""
    for index in range(length_of_line):
        if line[index].isdigit():
            number += line[index]
        else:
            if line[index] == "*":
                symbol_indices.append(index)
            if len(number) > 0:
                numbers.append(number)
                indices.append(index - len(number))
                number = ""
        if index == length_of_line - 1 and len(number) > 0:
            numbers.append(number)
            indices.append(index - len(number) + 1)

    return numbers, indices, symbol_indices


def main():
    data = open("day3/test_data.txt")

    solution = solve_second_task(data)
    print("Solution to second task: ", solution)

    data.close()


if __name__ == "__main__":
    main()

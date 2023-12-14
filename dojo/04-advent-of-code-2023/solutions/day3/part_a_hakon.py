def solve_first_task(data):
    first_line = data.readline()
    first_line_stripped = first_line.strip()
    length_of_lines = len(first_line_stripped)
    prev_numbers, prev_indices, prev_symbol_indices = get_numbers_and_symbols(length_of_lines, first_line_stripped)
    summ = 0
    for line in data:
        line_stripped = line.strip()
        numbers, indices, symbol_indices = get_numbers_and_symbols(length_of_lines, line_stripped)
        for number, index in zip(prev_numbers, prev_indices):
            for symbol_index in prev_symbol_indices + symbol_indices:
                if (symbol_index - index <= len(number) and symbol_index - index >= 0) or index - symbol_index == 1:
                    summ += int(number)
                    break
        to_remove = []
        index_and_numbers = {index: number for index, number in zip(indices, numbers)}
        for index, number in index_and_numbers.items():
            for symbol_index in prev_symbol_indices + symbol_indices:
                if (symbol_index - index <= len(number) and symbol_index - index >= 0) or index - symbol_index == 1:
                    summ += int(number)
                    to_remove.append(index)
                    break
        for key in to_remove:
            del index_and_numbers[key]
        prev_numbers = index_and_numbers.values()
        prev_indices = index_and_numbers.keys()
        prev_symbol_indices = symbol_indices
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
            if line[index] != ".":
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

    solution = solve_first_task(data)
    print("Solution to first task: ", solution)

    data.close()


if __name__ == "__main__":
    main()

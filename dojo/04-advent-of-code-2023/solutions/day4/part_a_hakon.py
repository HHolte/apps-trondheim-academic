from re import split


def solve_first_task(data):
    total_points = 0
    for line in data:
        line_stripped = line.strip()
        total_points += score_card(line_stripped)
    return total_points


def score_card(card: str):
    n_correct = 0
    _, numbers = split(":", card)
    winning_numbers, our_numbers = numbers.split("|")
    winning_numbers = winning_numbers.strip().split(" ")
    our_numbers = our_numbers.strip().split(" ")
    winning_numbers = [int(number) for number in winning_numbers if number != ""]
    our_numbers = [int(number) for number in our_numbers if number != ""]
    for number in winning_numbers:
        if number in our_numbers:
            n_correct += 1
    return 2**(n_correct - 1) if n_correct > 0 else 0


def main():
    data = open("day4/test_data.txt", "r")

    solution = solve_first_task(data)
    print("Solution to first task: ", solution)

    data.close()


if __name__ == "__main__":
    main()

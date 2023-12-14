from re import split


def solve_second_task(data):
    card_overview = {}
    for line in data:
        line = line.strip()
        card_number, numbers = split(":", line)
        card_number = int(card_number[5:])
        points_on_card = score_card(numbers)
        card_overview[card_number] = 1 if card_number not in card_overview else card_overview[card_number] + 1
        for number in range(card_number + 1, card_number + points_on_card + 1):
            if number in card_overview:
                card_overview[number] += card_overview[card_number]
            else:
                card_overview[number] = card_overview[card_number]
    total_cards = sum(card_overview.values())
    return total_cards


def score_card(numbers: str):
    n_correct = 0
    winning_numbers, our_numbers = numbers.split("|")
    winning_numbers = winning_numbers.strip().split(" ")
    our_numbers = our_numbers.strip().split(" ")
    winning_numbers = [int(number) for number in winning_numbers if number != ""]
    our_numbers = [int(number) for number in our_numbers if number != ""]
    for number in winning_numbers:
        if number in our_numbers:
            n_correct += 1
    return n_correct


def main():
    data = open("day4/test_data.txt", "r")

    solution = solve_second_task(data)
    print("Solution to second task: ", solution)

    data.close()


if __name__ == "__main__":
    main()

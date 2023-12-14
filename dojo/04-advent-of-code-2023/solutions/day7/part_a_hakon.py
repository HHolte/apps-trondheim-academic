from math import floor


to_value = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "T": 10, "J": 11, "Q": 12, "K": 13, "A": 14}


def get_type(hand: str):
    uniques = "".join(set(hand))
    if len(uniques) == 1:
        return 21
    elif len(uniques) == 2:
        temp = hand.replace(uniques[0], "")
        return 20 if len(temp) == 1 or len(temp) == 4 else 19
    elif len(uniques) == 3:
        temp = hand.replace(uniques[0], "")
        if len(temp) == 2:
            return 18
        elif len(temp) == 3:
            return 17
        temp = temp.replace(uniques[1], "")
        return 18 if len(temp) == 1 or len(temp) == 3 else 17
    elif len(uniques) == 4:
        return 16
    else:
        return 15


def cardwise_compare_hands(first_hand: str, second_hand: str):
    for i in range(len(first_hand)):
        if to_value[first_hand[i]] > to_value[second_hand[i]]:
            return True
        if to_value[first_hand[i]] < to_value[second_hand[i]]:
            return False
    return True


def compare_hands(first_hand: str, second_hand: str):
    first_hand_type = get_type(first_hand)
    second_hand_type = get_type(second_hand)
    if first_hand_type > second_hand_type:
        return True
    if first_hand_type == second_hand_type:
        cardwise_compare_result = cardwise_compare_hands(first_hand, second_hand)
        return cardwise_compare_result
    return False


def binary_sort_hand_into_list(hand: str, rank_list: list[str]):
    length_of_list = len(rank_list)
    if length_of_list == 0:
        return [hand]
    index = floor(length_of_list / 2)
    value_at_middle = rank_list[index].split(" ")[0]
    if compare_hands(hand.split(" ")[0], value_at_middle):
        if length_of_list == 1:
            rank_list.append(hand)
            return rank_list
        return rank_list[:index + 1] + binary_sort_hand_into_list(hand, rank_list[index + 1:])
    else:
        if length_of_list == 1:
            rank_list.insert(0, hand)
            return rank_list
        return binary_sort_hand_into_list(hand, rank_list[:index]) + rank_list[index:]


def solve_first_task(data):
    rank_list = []
    for line in data:
        hand_and_bid = line.strip()
        rank_list = binary_sort_hand_into_list(hand_and_bid, rank_list)
    out_value = 0
    for i in range(0, len(rank_list)):
        out_value += (i + 1) * int(rank_list[i].split(" ")[1])
    return out_value


def main():
    data = open("day7/test_data.txt", "r")

    solution = solve_first_task(data)
    print("Solution to first task: ", solution)

    data.close()


if __name__ == "__main__":
    main()

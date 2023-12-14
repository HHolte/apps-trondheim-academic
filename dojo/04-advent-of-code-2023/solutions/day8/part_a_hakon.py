def solve_first_task(data):
    instructions = data.readline().strip()
    nodes = {}
    for line in data:
        line = line.strip()
        if line == "":
            continue
        node, neighbors = line.replace(" ", "").split("=")
        left_element, right_element = neighbors.replace("(", "").replace(")", "").split(",")
        nodes[node] = (left_element, right_element)
    current_position = "AAA"
    target_position = "ZZZ"
    instruction_index = 0
    number_of_steps = 0
    while current_position != target_position:
        neighbors = nodes[current_position]
        current_position = neighbors[0] if instructions[instruction_index] == "L" else neighbors[1]
        instruction_index = instruction_index + 1 if instruction_index < len(instructions) - 1 else 0
        number_of_steps += 1
    return number_of_steps


def main():
    data = open("day8/test_data.txt", "r")

    solution = solve_first_task(data)
    print("Solution to first task: ", solution)

    data.close()


if __name__ == "__main__":
    main()

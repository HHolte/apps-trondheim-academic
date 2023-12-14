from math import lcm


def get_number_of_steps(start: str, nodes: dict[str, tuple[str, str]], instructions: str):
    number_of_steps = 0
    current_position = start
    instruction_index = 0
    while current_position[-1] != "Z":
        neighbors = nodes[current_position]
        current_position = neighbors[0] if instructions[instruction_index] == "L" else neighbors[1]
        instruction_index = instruction_index + 1 if instruction_index < len(instructions) - 1 else 0
        number_of_steps += 1
    return number_of_steps


def solve_second_task(data):
    instructions = data.readline().strip()
    nodes = {}
    starts = []
    for line in data:
        line = line.strip()
        if line == "":
            continue
        node, neighbors = line.replace(" ", "").split("=")
        left_element, right_element = neighbors.replace("(", "").replace(")", "").split(",")
        nodes[node] = (left_element, right_element)
        if node[-1] == "A":
            starts.append(node)
    all_number_of_steps = []
    for pos in starts:
        number_of_steps = get_number_of_steps(pos, nodes, instructions)
        all_number_of_steps.append(number_of_steps)
    number_of_steps = lcm(*all_number_of_steps)
    return number_of_steps


def main():
    data = open("day8/test_data.txt", "r")

    solution = solve_second_task(data)
    print("Solution to second task: ", solution)

    data.close()


if __name__ == "__main__":
    main()

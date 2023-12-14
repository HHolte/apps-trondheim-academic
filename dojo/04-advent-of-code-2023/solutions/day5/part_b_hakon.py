from day5.part_a_hakon import Mapper, CategoryMapper
from copy import deepcopy


def get_seed_bins(seed_specification: list[int]):
    seed_bins = []
    seed_index = 0
    while seed_index < len(seed_specification):
        seed = seed_specification[seed_index]
        seed_range_length = seed_specification[seed_index + 1]
        seed_bins.append((seed, seed + seed_range_length))
        seed_index += 2
    return seed_bins


def solve_second_task(data: str):
    first_line = data.readline().strip()
    seeds = first_line.split(":")[1].strip().split(" ")
    seed_specification = [int(seed) for seed in seeds]
    all_mappers: list[CategoryMapper] = []
    current_mapper = CategoryMapper()
    for line in data:
        if line[0].isdigit():
            numbers_in_line = line.strip().split(" ")
            current_mapper.mappers.append(Mapper(numbers_in_line))
        else:
            if len(current_mapper.mappers) > 0:
                all_mappers.append(deepcopy(current_mapper))
                current_mapper.remove_all_mappers()
    all_mappers.append(current_mapper)

    seed_bins = get_seed_bins(seed_specification)
    location = 0
    seed_found = False
    while not seed_found:
        location += 1
        mapped_value = location
        for mapper in all_mappers[::-1]:
            mapped_value = mapper.inverse_map_value(mapped_value)
        for bin in seed_bins:
            if bin[0] <= mapped_value < bin[1]:
                seed_found = True
                break
    return location


def main():
    data = open("day5/test_data.txt", "r")

    solution = solve_second_task(data)
    print("Solution to second task: ", solution)

    data.close()


if __name__ == "__main__":
    main()

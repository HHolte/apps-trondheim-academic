class Mapper:
    destination_start: int
    source_start: int
    range_length: int

    def __init__(self, numbers_in_line: list[str]):
        self.destination_start, self.source_start, self.range_length = [int(number) for number in numbers_in_line]


class CategoryMapper:
    mappers: list[Mapper] = []

    def map_value(self, source_value: int):
        for mapper in self.mappers:
            if mapper.source_start <= source_value < mapper.source_start + mapper.range_length:
                return source_value + (mapper.destination_start - mapper.source_start)
        return source_value

    def inverse_map_value(self, destination_value: int):
        for mapper in self.mappers:
            if mapper.destination_start <= destination_value < mapper.destination_start + mapper.range_length:
                return destination_value + (mapper.source_start - mapper.destination_start)
        return destination_value

    def remove_all_mappers(self):
        self.mappers = []


def solve_first_task(data: str):
    first_line = data.readline().strip()
    seeds = first_line.split(":")[1].strip().split(" ")
    values_to_map = [int(seed) for seed in seeds]
    current_mapper = CategoryMapper()
    for line in data:
        if line[0].isdigit():
            numbers_in_line = line.strip().split(" ")
            current_mapper.mappers.append(Mapper(numbers_in_line))
        else:
            if len(current_mapper.mappers) > 0:
                values_to_map = [current_mapper.map_value(value) for value in values_to_map]
                current_mapper.remove_all_mappers()
    values_to_map = [current_mapper.map_value(value) for value in values_to_map]
    return min(values_to_map)


def main():
    data = open("day5/test_data.txt", "r")

    solution = solve_first_task(data)
    print("Solution to first task: ", solution)

    data.close()


if __name__ == "__main__":
    main()

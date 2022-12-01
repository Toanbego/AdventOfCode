

def read_data(path="puzzle_input.txt"):
    """Reads puzzle input"""
    fin = open(path, "r")
    lines = [line.strip() for line in fin.readlines() if line.strip()]
    cave_edges = {}
    for i in lines:
        cave = i.split("-")
        if cave[0] not in list(cave_edges.keys()):
            cave_edges[cave[0]] = [cave[1]]
        else:
            cave_edges[cave[0]].append(cave[1])
        if cave[1] not in list(cave_edges.keys()):
            cave_edges[cave[1]] = [cave[0]]
        else:
            cave_edges[cave[1]].append(cave[0])
    return cave_edges


class Counter:
    def __init__(self):
        self.count = 0

    def traverse(self, edges, currentCave, pathSoFar):
        if not canVisit(pathSoFar, currentCave):
            return []

        currentPath = pathSoFar.copy()
        currentPath.append(currentCave)
        if currentCave == "end":
            self.count += 1
            return [currentCave]

        possible_paths = []
        for vertex in edges[currentCave]:
            possible_paths_with_next_cave = self.traverse(edges, vertex, currentPath)
            possible_paths.append(possible_paths_with_next_cave)
        return possible_paths


def isBigCave(cave):
    if cave == cave.upper():
        return True
    else:
        return False


def canVisit(path, nextCave):
    return nextCave not in path or isBigCave(nextCave)


def task1(data):
    """Write the code for task 1 here"""
    counter = Counter()

    _ = counter.traverse(data, "start", [])

    return counter.count


def task2(data):
    """Write the code for task 2 here"""



if __name__ == '__main__':
    puzzle_input = read_data()
    if task1(read_data("test_input.txt")) == 10:
        print(f"Solution to task 1: {task1(puzzle_input)}")
    if task2(read_data("test_input.txt")) == "":
        print(f"Solution to task 2: {task2(puzzle_input)}")




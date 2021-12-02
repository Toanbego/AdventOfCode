
def read_data(path="puzzle_input.txt"):
    """Reads puzzle input"""
    fin = open(path, "r")
    lines = [line.strip() for line in fin.readlines() if line.strip()]
    return lines


def find_adjacent_neighbors(active_points, x, y, z):
    """ Finds the number of neighbours == # for an element in a 3 dimensional space """
    active_neighbors = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            for k in range(-1, 2):
                for h in range(-1, 2):
                    if not (i==0 and j==0 and k==0):
                        if(x + i, y + j, z + k) in active_points:
                            active_neighbors += 1

    return active_neighbors


def get_initial_active_points(data):
    """ Finds the number elements == # for 3 dimensional space """
    active_points = set()
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[j][i] == "#":
                active_points.add((i, j, 0))
    return active_points


def get_initial_active_points2(data):
    """ Finds the number elements == # for 4 dimensional space  """
    active_points = set()
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[j][i] == "#":
                active_points.add((i, j, 0, 0))
    return active_points


def find_adjacent_neighbors2(active_points, x, y, z, w):
    """ Finds the number of neighbours == # for an element in a 4 dimensional space """
    active_neighbors = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            for k in range(-1, 2):
                for h in range(-1, 2):
                    if not (i == 0 and j == 0 and k == 0 and h == 0):
                        if(x + i, y + j, z + k, w + h) in active_points:
                            active_neighbors += 1

    return active_neighbors


def task1(data):
    """Write the code for task 1 here"""

    active_points = get_initial_active_points(data)

    cycles = 6
    for cycle in range(cycles):
        new_active_points = set()

        for x in range(-10 - cycle, cycle + 10):
            for y in range(-10 - cycle, cycle + 10):
                for z in range(-2 - cycle, cycle + 2):
                    neighbor_count = find_adjacent_neighbors(active_points, x, y, z)

                    # Rule 1
                    if (x, y, z) in active_points and (neighbor_count == 2 or neighbor_count == 3):
                        new_active_points.add((x, y, z))
                    # Rule 2
                    if (x, y, z) not in active_points and neighbor_count == 3:
                        new_active_points.add((x, y, z))

        active_points = new_active_points

    return len(active_points)

def task2(data):
    """Write the code for task 2 here"""

    active_points = get_initial_active_points2(data)

    cycles = 6
    # Loop through 6 cycles
    for cycle in range(cycles):
        new_active_points = set()

        # Check each position
        for x in range(-10 - cycle, cycle + 10):
            for y in range(-10 - cycle, cycle + 10):
                for z in range(-2 - cycle, cycle + 2):
                    for w in range(-2 - cycle, cycle + 2):

                        # Find neighbors
                        neighbor_count = find_adjacent_neighbors2(active_points, x, y, z, w)

                        # Rule 1
                        if (x, y, z, w) in active_points and (neighbor_count == 2 or neighbor_count == 3):
                            new_active_points.add((x, y, z, w))
                        # Rule 2
                        if (x, y, z, w) not in active_points and neighbor_count == 3:
                            new_active_points.add((x, y, z, w))

        active_points = new_active_points

    return len(active_points)


def main():
    puzzle_input = read_data()

    print(f"Solution to task 1: {task1(puzzle_input)}")
    print(f"Solution to task 2: {task2(puzzle_input)}")


main()
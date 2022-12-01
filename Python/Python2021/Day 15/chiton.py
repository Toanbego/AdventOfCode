import numpy as np


class Data:

    def __init__(self, inputs):
        """Reads puzzle input"""
        self.inputs = inputs
        self.data = {}
        for i in range(len(inputs)):
            if "puzzle" not in list(self.data.keys()):
                self.data["puzzle"] = self.parse_data(inputs[i])
            else:
                self.data[f"test_input{i}"] = self.parse_data(inputs[i])

    def parse_data(self, path):

        fin = open(path, "r")
        lines = [line.strip() for line in fin.readlines() if line.strip()]
        array = np.array([[int(i) for i in line] for line in lines])
        return array


class Pathfinder:
    def __init__(self, data):
        self.data = data
        self.open_list = []
        self.closed_list = []

        self.start_node = []
        # self.G, self.H, self.F = 0, 0, 0

    def F(self):
        F = []
        for i in self.open_list:
            F.append(self.G(i))
        return min(F)

        # Create the f, g, and h values
        child.g = current_node.g + 1
        child.h = ((child.position[0] - end_node.position[0]) ** 2) + ((child.position[1] - end_node.position[1]) ** 2)
        child.f = child.g + child.h

    def G(self, i):
        """Get euclidean distance"""
        return np.linalg.norm(np.array(self.open_list[i]) - np.array([0, 0]))

    def H(self, i):
        """Get euclidean distance"""
        return np.linalg.norm(np.array(self.open_list[i]) - np.array([0, 0]))

class Node():
    """A node class for A* Pathfinding"""

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position


def get_adjacent_points(pos, data):
    y, x = pos[0], pos[1]
    adjacent = []
    adjacent_idx_x, adjacent_idx_y = [-1, 1, 0, 0], [0, 0, -1, 1]
    for dx, dy in zip(adjacent_idx_x, adjacent_idx_y):
        # Make sure within range
        if dy > (len(data) - 1) or dy < 0 or dx > (len(data[len(data) - 1]) - 1) or dx < 0:
            continue
        adjacent.append([y + dy, x + dx])
    return adjacent

def task1(data):
    """Write the code for task 1 here"""
    pathfinder = Pathfinder(data)

    # Create start and end node
    start_node = Node(None, (0, 0))
    start_node.g = start_node.h = start_node.f = 0
    end_node = Node(None, (len(data)-1, len(data[0] - 1)))
    end_node.g = end_node.h = end_node.f = 0

    closed_list = []
    open_list = [start_node]

    while len(open_list) > 0:
        current_node = open_list[0]
        current_index = 0
        for index, item in enumerate(open_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index
        # Pop current off open list, add to closed list
        open_list.pop(current_index)
        closed_list.append(current_node)

        # Found the goal
        if current_node == end_node:
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1]  # Return reversed path

        # Generate children
        # adj = get_adjacent_points(current_node.position, data)
        # children = []
        # for i in adj:
        #     children.append(Node(i))
        children = [Node(current_node, i) for i in get_adjacent_points(current_node.position, data)]
        for child in children:
            # Child is on the closed list
            for closed_child in closed_list:
                if child == closed_child:
                    continue

            # Create the f, g, and h values
            child.g = current_node.g + 1
            child.h = ((child.position[0] - end_node.position[0]) ** 2) + \
                      ((child.position[1] - end_node.position[1]) ** 2)
            child.f = child.g + child.h

            # Child is already in the open list
            for open_node in open_list:
                if child == open_node and child.g > open_node.g:
                    continue

            # Add the child to the open list
            open_list.append(child)









def task2(data):
    """Write the code for task 2 here"""


def main():
    puzzle_input = Data(["puzzle_input.txt", "test_input.txt"])

    assert task1(puzzle_input.data["test_input1"]) == ""
    print(f"Solution to task 1: {task1(puzzle_input.data['puzzle'])}")

    # assert task2(puzzle_input.data["test_input1"]) == "", "Failed test"
    print(f"Solution to task 2: {task2(puzzle_input.data['puzzle'])}")


main()

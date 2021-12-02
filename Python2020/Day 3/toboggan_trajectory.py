import numpy as np


def read_data(path):
    """ Reads puzzle input """
    with open(path, 'r') as f:
        data = f.read().split('\n')
    return data


def format_data(data):
    """
    Formats puzzle input into an array of True/False.
    True = Tree
    False = Clear path
    :param data: List of data points as read from read_data()
    :return:
    """
    return np.array([np.array(list(line)) == '#' for line in data])


def count_trees_in_path(toboggan_map, path=(3, 1)):
    """
    Counts the number of trees through a given path
    :param toboggan_map: Map of toboggan route
    :param path: path to take trough the map
    :return:
    """
    tree_count = 0
    x_position = 0
    y_position = 0
    map_length_x = len(toboggan_map[0])
    map_length_y = len(toboggan_map)

    # Traverse downhill
    while y_position < map_length_y:

        # If the element at the position is True, there is a tree there.
        if toboggan_map[y_position][x_position]:
            tree_count += 1

        # Update position. If x position is at the "end of array", reset it to left side again
        y_position += path[1]
        x_position = (x_position + path[0]) % map_length_x

    return tree_count


if __name__ == '__main__':

    puzzle_input = read_data('puzzle_input.txt')
    puzzle_input = format_data(puzzle_input)

    # Check all paths for trees.
    paths = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    trees_per_path_product = 1
    for path in paths:
        count = count_trees_in_path(puzzle_input, path=path)
        trees_per_path_product *= count
        print(f"Trees encountered for path {path}: {count}")
    print(f"Multiplying each tree count: {trees_per_path_product}")





import numpy as np


def read_data(path):
    """ Reads puzzle input """
    with open(path, 'r') as f:
        data = f.read().split('\n')
    return data


def format_data(data):
    """
    Formats puzzle input into an array of True False.
    True = Tree
    False = Clear path
    :param data:
    :return:
    """
    return np.array([np.array(list(line)) == '#' for line in data])

def print_position(map_snapshot, next_map_snapshot, position, counter):
    """

    :param map_snapshot:
    :param position:
    :return:
    """
    map_snapshot = map_snapshot*1
    next_map_snapshot = next_map_snapshot*1
    next_map_snapshot = next_map_snapshot.astype(str)
    # map_snapshot = list(map_snapshot)
    if map_snapshot[position[1]] == 1:
        map_snapshot = map_snapshot.astype(str)
        map_snapshot[position[1]] = 'T'
    else:
        map_snapshot = map_snapshot.astype(str)
        map_snapshot[position[1]] = 'X'
    next_map_snapshot = next_map_snapshot.astype(str)


    print(*map_snapshot , sep=", ")
    print(*next_map_snapshot, sep=", ")
    print("-----------------------------------------------")


def count_trees_in_path(toboggan_map, path=(3, 1)):
    """
    Counts the number of trees through a given path
    :param toboggan_map: Map of toboggan route
    :param path: path to take trough the map
    :return:
    """

    tree_count = 0
    position = [0, 0]

    i = 0
    map_length_east = len(toboggan_map[0])
    map_length_south = len(toboggan_map)

    # Traverse downhill
    while position[0] < map_length_south:
        # print_position(toboggan_map[position[0]], toboggan_map[position[0]+1], position, counter=tree_count)

        # Check for trees
        if toboggan_map[position[0]][position[1]]:
            tree_count += 1
        next_position = [position[0] + path[1], position[1] + path[0]]
        if next_position[1] > map_length_east-1:
            next_position[1] = next_position[1]-map_length_east

        position = next_position

    return tree_count



if __name__ == '__main__':
    puzzle_input = read_data('puzzle_input.txt')
    puzzle_input = format_data(puzzle_input)

    paths = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    trees_per_path_product = 1
    for path in paths:
        count = count_trees_in_path(puzzle_input, path=path)
        trees_per_path_product *= count
        print(f"Trees encountered for path {path}: {count}")
    print(f"Multiplying each tree count: {trees_per_path_product}")





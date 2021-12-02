
import numpy as np

def read_data(path="puzzle_input.txt"):
    fin = open(path, "r")
    lines = [line.strip() for line in fin.readlines() if line.strip()]
    return lines


def change_direction(direction_change, direction, degrees):
    if degrees == 180:
        if direction == 'E':
            return 'W'
        elif direction == 'S':
            return 'N'
        elif direction == 'N':
            return 'S'
        elif direction == 'W':
            return 'E'

    elif degrees == 270:
        if direction_change == 'R':
            direction_change = 'L'
        elif direction_change == 'L':
            direction_change = 'R'

    if direction_change == 'R':
        if direction == 'E':
            return 'S'
        elif direction == 'S':
            return 'W'
        elif direction == 'W':
            return 'N'
        elif direction == 'N':
            return 'E'

    elif direction_change == 'L':
        if direction == 'E':
            return 'N'
        elif direction == 'N':
            return 'W'
        elif direction == 'W':
            return 'S'
        elif direction == 'S':
            return 'E'


def rotate_waypoint(way_pos, direction_change, degrees):
    if degrees == 180:
        tmp_s, tmp_n, tmp_e, tmp_w = way_pos['S'], way_pos['N'], way_pos['E'], way_pos['W']
        way_pos['S'], way_pos['N'], way_pos['E'], way_pos['W'] = tmp_n, tmp_s, tmp_w, tmp_e

    elif degrees == 270:
        if direction_change == 'R':
            direction_change = 'L'
        elif direction_change == 'L':
            direction_change = 'R'

    if direction_change == 'R':
        tmp_s, tmp_n, tmp_e, tmp_w = way_pos['S'], way_pos['N'], way_pos['E'], way_pos['W']
        way_pos['S'], way_pos['N'], way_pos['E'], way_pos['W'] = tmp_e, tmp_w, tmp_n, tmp_s
    elif direction_change == 'L':
        tmp_s, tmp_n, tmp_e, tmp_w = way_pos['S'], way_pos['N'], way_pos['E'], way_pos['W']
        way_pos['S'], way_pos['N'], way_pos['E'], way_pos['W'] = tmp_w, tmp_e, tmp_s, tmp_n
    return way_pos



def manhattan_value(position):
    north_south = np.abs(position['N'] - position['S'])
    east_west = np.abs(position['E'] - position['W'])
    print(north_south + east_west)


def part1(instructions):
    direction_dict = {'W': 0, 'E': 0, 'N': 0, 'S': 0}
    current_direction = 'E'
    for i, instruction in enumerate(instructions):
        inst = instruction[0]
        value = int(instruction[1:])
        if inst == 'F':
            direction_dict[current_direction] += value
        elif inst == 'S' or inst == 'N' or inst == 'E' or inst == 'W':
            direction_dict[inst] += value
        elif inst == 'L' or inst == 'R':
            current_direction = change_direction(inst, current_direction, value)

    print("Solution part 1: " + str(manhattan_value(direction_dict)))


def part2(instructions):
    direction_dict = {'W': 0, 'E': 0, 'N': 0, 'S': 0}
    waypoint_position = {'W': 0, 'E': 10, 'N': 1, 'S': 0}
    current_direction = 'E'
    for i, instruction in enumerate(instructions):
        inst = instruction[0]
        value = int(instruction[1:])

        if inst == 'F':
            for k in range(value):
                for waypoint in waypoint_position:
                    direction_dict[waypoint] += waypoint_position[waypoint]

        elif inst == 'S' or inst == 'N' or inst == 'E' or inst == 'W':
            waypoint_position[inst] += value

        elif inst == 'L' or inst == 'R':
            waypoint_position = rotate_waypoint(waypoint_position, inst, value)
            current_direction = change_direction(inst, current_direction, value)

    print("Solution part 2: " + str(manhattan_value(direction_dict)))


if __name__ == '__main__':
    puzzle_input = read_data("puzzle_input1.txt")

    part1(puzzle_input)
    part2(puzzle_input)






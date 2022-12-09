import numpy as np
import requests as req

convert_dir = {'R': 1, 'L': -1, 'U': 1, 'D': -1}

def submit_answer(answer, level):
    cookies = {"session": open("../../credentials", "r").readlines()[0]}
    response = req.post(
        url=f'https://adventofcode.com/2022/day/9/answer',
        cookies=cookies,
        data={"level": {level}, "answer": {answer}},
    )
    if "That's not the right answer" in response.text:
        print(f"{answer} is not correct level {level}")
    else:
        print(f"{answer} is the correct answer for level {level}")


class Data:

    def __init__(self, inputs):
        """Reads puzzle input"""
        self.data = {"test_input": self.parse_data(inputs[1]), f"puzzle": self.parse_data(inputs[0])}

    def parse_data(self, path):
        """This parses data"""
        file = open(path, "r")
        return [line.strip().split(" ") for line in file.readlines()]


def check_adjacent(head_pos, tail_pos):
    score = []
    score.append(abs(head_pos[1] - tail_pos[1]))  # Horizontal
    score.append(abs(head_pos[0] - tail_pos[0]))  # Vertical
    if 2 in score:
        return False
    else:
        return True

# def get_adjacent_points(y, x):
#     adjacent = []
#     adjacent_idx_x, adjacent_idx_y = [-1, 1, 0, 0, -1, 1, 1, -1], [0, 0, -1, 1, -1, 1, -1, 1]
#     for dx, dy in zip(adjacent_idx_x, adjacent_idx_y):
#         adjacent.append([y + dy, x + dx])
#     return adjacent

def task1(data):
    """Write the code for task 1 here"""
    tail_pos = [[0, 0], [0, 0]]
    head_pos = [0, 0]
    previous_pos = [0, 0]
    visited_pos = [[0, 0]]
    for direction, moves in data:
        for m in range(int(moves)):
            previous_pos[0], previous_pos[1] = tail_pos[0][0], tail_pos[0][1]
            if direction == 'R' or direction == 'L':
                tail_pos[0][1] += convert_dir[direction]
            elif direction == 'U' or direction == 'D':
                tail_pos[0][0] += convert_dir[direction]

            if check_adjacent(tail_pos[0], tail_pos[1]):
                continue
            else:
                tail_pos[1][0], tail_pos[1][1] = previous_pos[0], previous_pos[1]
                if tail_pos[1] not in visited_pos:
                    visited_pos.append([tail_pos[1][0], tail_pos[1][1]])
    return sum([1 for i in visited_pos])


def task2(data):
    """Write the code for task 2 here"""
    tail_pos = [[0, 0] for i in range(10)]
    previous_pos = [0, 0]
    visited_pos = [[0, 0]]
    for direction, moves in data:
        for m in range(int(moves)):

            previous_pos[0], previous_pos[1] = tail_pos[0][0], tail_pos[0][1]
            if direction == 'R' or direction == 'L':
                tail_pos[0][1] += convert_dir[direction]
            elif direction == 'U' or direction == 'D':
                tail_pos[0][0] += convert_dir[direction]

            adjacent_tails = [check_adjacent(tail_pos[idx-1], tail_pos[idx]) for idx in range(1, len(tail_pos))]
            for i in range(1, len(tail_pos)):
                if check_adjacent(tail_pos[i-1], tail_pos[i]):
                    continue
                else:
                    if abs(tail_pos[i - 1][0] - tail_pos[i][0]) > 1:
                        tail_pos[i][0] = tail_pos[i - 1][0] + (-1*convert_dir[direction])
                        tail_pos[i][1] = tail_pos[i - 1][1]
                    elif abs(tail_pos[i - 1][1] - tail_pos[i][1]) > 1:
                        tail_pos[i][1] = tail_pos[i - 1][1] + (-1*convert_dir[direction])
                        tail_pos[i][0] = tail_pos[i - 1][0]

            if tail_pos[-1] not in visited_pos:
                visited_pos.append([tail_pos[-1][0], tail_pos[-1][1]])

    return sum([1 for i in visited_pos])



def main():
    puzzle_input = Data(["puzzle_input.txt", "test_input.txt"])

    assert task1(puzzle_input.data["test_input"]) == 13  # Set example answer here
    submit_answer(task1(puzzle_input.data['puzzle']), 1)

    print(task2(puzzle_input.data["puzzle"]))  # Set example answer here
    submit_answer(task2(puzzle_input.data['puzzle']), 2)


main()

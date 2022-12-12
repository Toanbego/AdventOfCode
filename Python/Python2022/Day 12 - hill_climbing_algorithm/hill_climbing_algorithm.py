import numpy as np
import requests as req
import collections
import string

def submit_answer(answer, level):
    cookies = {"session": open("../../credentials", "r").readlines()[0]}
    response = req.post(
        url=f'https://adventofcode.com/2022/day/12/answer',
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
        return np.array([[c for c in line.strip()] for line in file.readlines()])

def bfs(grid, start, goal):
    alphabet = string.ascii_lowercase
    queue = collections.deque()
    queue.append((0, start[0], start[1]))
    seen = set([start])
    width, height = grid.shape[1], grid.shape[0]
    while queue:

        c, x, y = queue.popleft()

        for x2, y2 in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
            if x2 < 0 or x2 >= width or y2 < 0 or y2 >= height:
                continue
            if (x2, y2) in seen:
                continue
            if alphabet.index(grid[y2][x2]) - alphabet.index(grid[y][x]) > 1:
                continue
            if x2 == goal[0] and y2 == goal[1]:
                return c + 1


            seen.add((x2, y2))
            queue.append((c + 1, x2, y2))
    return c

def bfs2(grid, start):
    alphabet = string.ascii_lowercase
    queue = collections.deque()
    queue.append((0, start[0], start[1]))
    seen = set([start])
    width, height = grid.shape[1], grid.shape[0]
    while queue:

        c, x, y = queue.popleft()

        for x2, y2 in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
            if x2 < 0 or x2 >= width or y2 < 0 or y2 >= height:
                continue
            if (x2, y2) in seen:
                continue
            if alphabet.index(grid[y2][x2]) - alphabet.index(grid[y][x]) < -1:
                continue
            if grid[y2][x2] == 'a':
                return c + 1

            seen.add((x2, y2))
            queue.append((c + 1, x2, y2))
    return c



def task1(data):
    """Write the code for task 1 here"""
    start = (int(np.where(data=='S')[1]), int(np.where(data=='S')[0]))
    data[start[1]][start[0]] = 'a'
    goal = (int(np.where(data == 'E')[1]), int(np.where(data == 'E')[0]))
    data[goal[1]][goal[0]] = 'z'

    c = bfs(data, start, goal)
    return c



def task2(data):
    """Write the code for task 2 here"""
    start = (int(np.where(data=='S')[1]), int(np.where(data=='S')[0]))
    data[start[1]][start[0]] = 'a'
    goal = (int(np.where(data == 'E')[1]), int(np.where(data == 'E')[0]))
    data[goal[1]][goal[0]] = 'z'
    return bfs2(data, goal)



def main():
    puzzle_input = Data(["puzzle_input.txt", "test_input.txt"])

    assert task1(puzzle_input.data["test_input"]) == 31  # Set example answer here
    submit_answer(task1(puzzle_input.data['puzzle']), 1)
    puzzle_input = Data(["puzzle_input.txt", "test_input.txt"])
    assert task2(puzzle_input.data["test_input"]) == 29  # Set example answer here
    submit_answer(task2(puzzle_input.data['puzzle']), 2)


main()

import numpy as np
import requests as req


def submit_answer(answer, level):
    cookies = {"session": open("../../credentials", "r").readlines()[0]}
    response = req.post(
        url=f'https://adventofcode.com/2025/day/4/answer',
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
        return [line.strip() for line in file.readlines()]
    
def moore(arr, x, y):
    rows, cols = arr.shape
    neighbors = []

    for dx in (-1, 0, 1):
        for dy in (-1, 0, 1):
            if dx == 0 and dy == 0:
                continue  

            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols:
                neighbors.append(str(arr[nx, ny]))

    return neighbors

def task1(data):
    """Write the code for task 1 here"""
    data = [[y for y in x] for x in data]
    grid = np.array(data)

    accessable_rolls = 0
    threshold = 4
    
    coords = np.argwhere(grid == "@")
    for (x, y) in coords:
        n = moore(grid, x, y)
        count = n.count("@")
        if count < threshold:
            accessable_rolls += 1
    
    return accessable_rolls
    

            
            




def task2(data):
    """Write the code for task 2 here"""
    data = [[y for y in x] for x in data]
    grid = np.array(data)

    accessable_rolls = 0
    threshold = 4
    
    while True:
        coords = np.argwhere(grid == "@")
        removeable_rolls = []
        for (x, y) in coords:
            n = moore(grid, x, y)
            count = n.count("@")
            if count < threshold:
                accessable_rolls += 1
                removeable_rolls.append([x, y])

        if len(removeable_rolls) == 0:
            break
        else:
            for x, y in removeable_rolls:
                grid[x, y] = "."

    
    return accessable_rolls
    



def main():
    puzzle_input = Data(["puzzle_input.txt", "test_input.txt"])

    print(task1(puzzle_input.data["test_input"]))


    print(task1(puzzle_input.data['puzzle']))



    print(task2(puzzle_input.data["test_input"]))  # Set example answer here
    print(task2(puzzle_input.data['puzzle']))


main()

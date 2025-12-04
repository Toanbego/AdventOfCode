import numpy as np
import requests as req
from copy import deepcopy





def submit_answer(answer, level):
    cookies = {"session": open("../../credentials", "r").readlines()[0]}
    response = req.post(
        url=f'https://adventofcode.com/2025/day/3/answer',
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

def task1(data):
    """Write the code for task 1 here"""
    total_joltage = 0


    for i in data:


        bank = [int(i) for i in i] 

        jolts = list(set(bank))
        jolts = sorted(jolts)
        jolts.reverse()
        
        max1 = jolts[0]
        for idx, i in enumerate(jolts):
            if bank.index(i) == len(bank)-1:
                max1 = jolts[idx+1]
                break
        
        max2 = max(bank[bank.index(max1)+1:])



        total_joltage += int(str(max1) + str(max2))


    return total_joltage





def task2(data):
    """Write the code for task 2 here"""
    total_joltage = []
    for i in data:
        bank_joltage = []
        bank = [int(i) for i in i] 
        leftover = 12
        n = len(bank)
        drops = n-leftover
        
        for b in bank:
            while bank_joltage and drops > 0 and bank_joltage[-1] < b:
                bank_joltage.pop()
                drops -= 1
            bank_joltage.append(b)
 
        total_joltage.append(int("".join(str(n) for n in bank_joltage[:leftover])))


        
       
    
    return sum(total_joltage)



def main():
    puzzle_input = Data(["puzzle_input.txt", "test_input.txt"])

    print(task1(puzzle_input.data["test_input"]))

    print(task1(puzzle_input.data['puzzle']))

    print(task2(puzzle_input.data["test_input"]))  # Set example answer here
    print(task2(puzzle_input.data['puzzle']))


main()

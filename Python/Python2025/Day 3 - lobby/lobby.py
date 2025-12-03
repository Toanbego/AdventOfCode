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

        # Conver to list of int
        #bank = np.array([int(i) for i in i], dtype=int)
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

def get_jolts(bank):
    jolts = list(set(bank))
    jolts = sorted(jolts)
    jolts.reverse()

    return jolts


def get_joltage_index(bank, jolts, joltage_per_bank):
    leftover = 12
    i = 0
    while len(joltage_per_bank) <12:

        if bank.index(jolts[i]) <= len(bank)-leftover:
            joltage_per_bank.append(jolts[i])
            jolts = get_jolts(bank[bank.index(jolts[i])+1:])
            leftover -= 1
        elif i == len(jolts)-1:
            i = 0
        else:
            i += 1

    return joltage_per_bank



def task2(data):
    """Write the code for task 2 here"""
    total_joltage = []
    for i in data:
        bank = [int(i) for i in i] 

        
        jolts = get_jolts(bank)
        
        joltage_per_bank = []

        joltage_per_bank = get_joltage_index(bank, jolts, joltage_per_bank)


                        
        
        total_joltage.append(int("".join(str(n) for n in joltage_per_bank)))

    
    return sum(total_joltage)



def main():
    puzzle_input = Data(["puzzle_input.txt", "test_input.txt"])

    print(task1(puzzle_input.data["test_input"]))

    print(task1(puzzle_input.data['puzzle']))

    print(task2(puzzle_input.data["test_input"]))  # Set example answer here
    return
    print(task2(puzzle_input.data['puzzle']))


main()

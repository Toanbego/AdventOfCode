import numpy as np
import requests as req
from collections import Counter 


# lst = "123123123"
# window = []
# for size in range(1, int(len(lst)/2)):

#     check = [lst[i:i + size] for i in range(0, len(lst), size)]
#     if len(set(check)) == 1:
#         print("add the sequence as invalid")
#         print(check)
#     s = ""





def submit_answer(answer, level):
    cookies = {"session": open("../../credentials", "r").readlines()[0]}
    response = req.post(
        url=f'https://adventofcode.com/2025/day/2/answer',
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
        file = open(f"Python2025/Day 2 - gift_shop/{path}", "r")
        return [line.strip() for line in file.readlines()]

def task1(data):
    """Write the code for task 1 here"""
    ranges = data[0].split(",")
    invalid_ids = 0
    for i in ranges:
        r1, r2 = int(i.split("-")[0]), int(i.split("-")[1])


        for x in range(r1,r2+1):
            
            x = str(x)
            if len(x) % 2 == 0:
                seq1, seq2 = x[0:int(len(x)/2)], x[int(len(x)/2):]
                # if seq1 == seq2:
                #     print(seq1 + "-" + seq2)
                invalid_ids = invalid_ids + int(x) if seq1 == seq2 else invalid_ids + 0
            
    return invalid_ids
        

def task2(data):
    """Write the code for task 2 here"""
    ranges = data[0].split(",")
    invalid_ids = 0
    for i in ranges:
        r1, r2 = int(i.split("-")[0]), int(i.split("-")[1])


        for x in range(r1,r2+1):
            is_repeating = False
            x = str(x)
       
            for size in range(1, int(len(x))):
                if size > len(x)/2:
                    break

                window = [x[i:i + size] for i in range(0, len(x), size)]
                if len(set(window)) == 1:
                    is_repeating = True



                if is_repeating:
                    invalid_ids += int(x)
                    break
               


            
    return invalid_ids



def main():
    puzzle_input = Data(["puzzle_input.txt", "test_input.txt"])

    print(task1(puzzle_input.data["test_input"]))
    print(task1(puzzle_input.data['puzzle']))
    
    print(task2(puzzle_input.data["test_input"]))  # Set example answer here
    print(task2(puzzle_input.data['puzzle']))


main()

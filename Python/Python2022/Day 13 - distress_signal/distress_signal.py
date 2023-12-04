import numpy as np
import requests as req

# if len(right) > len(left):
#     for l, r in zip(left, right[:len(left)]):
#         idx += 1
#         is_ordered += check_packet_order(l, r, is_ordered)
#         if is_ordered == 1:
#             return is_ordered
#     idx += 1
#
#     if idx > len(left):
#         return is_ordered + 1
#
# if len(right) < len(left):
#     idx += 1
#     for l, r in zip(left[:len(right)], right):
#         is_ordered += check_packet_order(l, r, is_ordered)
#         if is_ordered == 1:
#             return is_ordered
#
# elif len(left) == len(right):
#     for l, r in zip(left, right):
#         is_ordered += check_packet_order(l, r, is_ordered)
#         if is_ordered == 1:
#             return is_ordered

# def task12(data):
#     """Write the code for task 1 here"""
#
#     is_ordered = []
#     for c, pairs in enumerate(data):
#         p1, p2 = eval(pairs.split("\n")[0]), eval(pairs.split("\n")[1])
#         current_score = 0
#         print(c)
#         if c == 4:
#             print(c)
#         for i, packets in enumerate(zip(p1, p2)):
#             idx, left, right = i, packets[0], packets[1]
#             current_score += check_packet_order(left, right, current_score)
#             if current_score > 0:
#                 is_ordered.append(c+1)
#                 break
#         if len(p2) > len(p1):
#             is_ordered.append(c+1)
#     return sum(is_ordered)
#
#
#
#
#
#     return is_ordered

def submit_answer(answer, level):
    cookies = {"session": open("../../credentials", "r").readlines()[0]}
    response = req.post(
        url=f'https://adventofcode.com/2022/day/13/answer',
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
        return file.read().split("\n\n")


def check_packet_order(left, right, is_ordered):

    if isinstance(left, int) and isinstance(right, list):
        return check_packet_order([left], right, is_ordered)
    elif isinstance(left, list) and isinstance(right, int):
        return check_packet_order(left, [right], is_ordered)

    elif isinstance(left, list) and isinstance(right, list):
        if len(left) == 0 and len(right) > 0:
            return is_ordered + 1
        for i in range(min(len(left), len(right))):
            idx = i
            is_ordered += check_packet_order(left[i], right[i], is_ordered)
            if idx+1 == min(len(left), len(right)) and is_ordered == 0 and len(right) > len(left) and left[idx] == right[idx]:
                return is_ordered + 1
        return is_ordered

    elif isinstance(left, int) and isinstance(right, int):
        if right > left:
            return is_ordered + 1
        else:
            return is_ordered






def task1(data):
    ordered = []
    for c, pairs in enumerate(data):
        left, right = eval(pairs.split("\n")[0]), eval(pairs.split("\n")[1])
        is_ordered = check_packet_order(left, right, 0)
        if is_ordered > 1:
            print(c)
        # if is_ordered == 0 and len(left) < len(right):
        #     ordered.append(c + 1)
        if is_ordered > 0:
            ordered.append(c + 1)

    return sum(ordered)




def task2(data):
    """Write the code for task 2 here"""



def main():
    puzzle_input = Data(["puzzle_input.txt", "test_input.txt"])

    print(task1(puzzle_input.data["puzzle"]))
    # assert task1(puzzle_input.data["test_input"]) == 13  # Set example answer here
    # submit_answer(task1(puzzle_input.data['puzzle']), 1)
    #
    # assert task2(puzzle_input.data["test_input"]) == ""  # Set example answer here
    # submit_answer(task2(puzzle_input.data['puzzle']), 2)


main()

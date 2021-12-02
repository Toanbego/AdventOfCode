import numpy as np
import re

def read_data(path="puzzle_input.txt"):
    """Reads puzzle input"""
    fin = open(path, "r")
    lines = [line.strip() for line in fin.readlines() if line.strip()]
    return lines


def simplify_with_precedence(expr):
    """Solve expression in ordered precedence"""

    while len(expr) > 1:

        ordered, hold = [], []
        done = False

        while not done and len(expr) > 0:
            ch = expr.pop()
            if ch == '+':
                done = True
            hold.append(ch)

        if len(expr) == 0 and not done:
            result = simplify(hold)
            expr.append(result)

        else:
            ordered.append(expr.pop())
            for _ in range(2):
                ordered.append(hold.pop())

            result = simplify(ordered)
            hold.append(result)

            while len(hold) > 0:
                expr.append(hold.pop())

    return expr[0]

def simplify(expr):
    while len(expr) > 1:
        num1 = expr.pop()
        op = expr.pop()
        num2 = expr.pop()
        result = eval(f"{num1} {op} {num2}")
        expr.append(str(result))
    return expr[0]


def solve_stack(expr, precedence=False):
    """Solves math expressions by adding to stack"""
    stack = []

    for char in expr:
        if char.isdigit() or char in ["*", '+', "("]:
            stack.append(char)
        elif char == ')':
            ordered = []
            while stack[len(stack)-1] != '(':
                # Pop removes last value from stack and returns said value to ordered
                ordered.append(stack.pop())
            stack.pop()
            if precedence:
                result = simplify_with_precedence(ordered)
            else:
                result = simplify(ordered)
            stack.append(result)
    stack.reverse()
    if precedence:
        return simplify_with_precedence(stack)
    else:
        return simplify(stack)




def task1(data):
    """Write the code for task 1 here"""
    total = 0
    for expression in data:
        expression = expression.replace('(', '( ')
        expression = expression.replace(')', ' )')
        expr = expression.split(" ")

        result = solve_stack(expr)

        total += int(result)
    return total


def task2(data):
    """Write the code for task 2 here"""
    total = 0
    for expression in data:
        expression = expression.replace('(', '( ')
        expression = expression.replace(')', ' )')
        expr = expression.split(" ")

        result = solve_stack(expr, True)

        total += int(result)
    return total


def main():
    puzzle_input = read_data()
    test_data = ["1 + (2 * 3) + (4 * (5 + 6))",
                 "1 + 2 * 3 + 4 * 5 + 6"]
    assert(task1(test_data) == 122)


    print(f"Solution to task 1: {task1(puzzle_input)}")
    print(f"Solution to task 2: {task2(puzzle_input)}")


main()
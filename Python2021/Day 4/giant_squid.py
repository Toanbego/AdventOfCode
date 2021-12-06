import numpy as np


def read_data(path="puzzle_input.txt"):
    """Reads puzzle input"""
    fin = open(path, "r")
    lines = [line.strip() for line in fin.readlines() if line.strip()]
    return lines


def parse_bingo_data(data):
    """Split input data in number sequence and bingo boards"""
    boards = np.array([row.split() for row in data[1:]])
    return boards.reshape(int(boards.shape[0]/5), 5, 5).astype(int), list(map(int, data[0].split(",")))


def check_board(board, sequence):
    """Check board if its winning"""
    for i in range(len(board[0])):
        row_check = sum([1 for k in sequence if (k in board[i, :])])
        column_check = sum([1 for k in sequence if (k in board[:, i])])
        if row_check == 5:
            return board[i, :]
        elif column_check == 5:
            return board[:, i]
    return None


def calculate_score(board, sequence):
    """Calculate score of winning board"""
    return int(sequence[-1]) * sum([k for k in np.reshape(board, 25) if (k not in sequence)])


def task1(data):
    """Write the code for task 1 here"""
    # Extract sequence and boards from data input
    boards, numbers = parse_bingo_data(data)

    # Pull numbers from pool
    sequence = []
    for num in numbers:
        sequence.append(num)
        # Check boards for winners
        for board in boards:
            board_sequence = check_board(board, sequence)
            if board_sequence is not None:
                return calculate_score(board, sequence)


def task2(data):
    """Write the code for task 2 here"""
    # Extract sequence and boards from data input
    boards, numbers = parse_bingo_data(data)

    # Pull numbers from pool
    sequence = []
    win_order = []
    win_board_idx = []
    for num in numbers:
        sequence.append(num)
        # Check boards for winners
        for i, board in enumerate(boards):
            board_sequence = check_board(board, sequence)
            if board_sequence is not None:
                win_order.append(calculate_score(board, sequence))
                win_board_idx.append(i)
                boards[i] = np.empty(board.shape)
    return win_order[-1]


def main():
    puzzle_input = read_data()

    print(f"Solution to task 1: {task1(puzzle_input)}")
    print(f"Solution to task 2: {task2(puzzle_input)}")


main()

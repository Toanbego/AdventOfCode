"""
    xn(t) = t + n

    x0(t) = t + 0

    x1(t) = t + 1

    x1(t) = t + 1   =>   x1(t) = x0(t) + 1 => x0(t) = x1(t) - 1
    x2(t) = t + 2   =   x2(t) = x1(t) - 1 + 2   =   x2(t) = x0(t) + 1 - 1 + 2 = x0(t) = x2(t) - 2
    x3(t) = t + 3   =   x3(t) = x2(t) - 2 + 3   =   x3(t) = x0(t) + 2 - 2 + 3 = x3(t) = x0(t) + 3
    .
    .
    .
    xn(t) = t + n => x0(t) = xn(t) - n
                     t = xn(t) - n

---------------------------
    x0(t) = t + 0
    x1(t) = t + 1   =   x1(t) = x0(t) + 1       =   x1(t) = t + 1   t = x1(t) - 1
    x2(t) = t + 2   =   x2(t) = x1(t) - 1 + 2   =   x2(t) = t + 1 - 1 + 2   =   t = x2(t) - 2
    x3(t) = t + 3   =   x3(t) = x2(t) - 2 + 3   =   x3(t)

"""
from collections import *
from functools import reduce


def read_data(path="puzzle_input.txt"):
    """Reads puzzle input"""
    fin = open(path, "r")
    lines = [line.strip() for line in fin.readlines() if line.strip()]
    return lines


def check_buss_timestamp(timestamp_by_ID, departure_time):
    """Checks when all busses have passed the time input"""
    have_passed_departure_time = []
    for ID in timestamp_by_ID:
        if timestamp_by_ID[ID] >= departure_time:
            have_passed_departure_time.append(True)
        else:
            have_passed_departure_time.append(False)
    return all(have_passed_departure_time)


def task1(departure_time, bussIDs):
    """Write the code for task 1 here"""
    timestamps_by_ID = {}
    for ID in bussIDs:
        if ID == 'x':
            continue
        timestamps_by_ID[int(ID)] = 0

    while True:
        # Check buss timestamp:
        if check_buss_timestamp(timestamps_by_ID, departure_time):
            bus_times = {}

            for ID in timestamps_by_ID:
                bus_times[timestamps_by_ID[ID] - departure_time] = ID
            earliest_bus_time = min(list(bus_times.keys()))
            earliest_bus_timeID = bus_times[earliest_bus_time]
            return earliest_bus_time * earliest_bus_timeID

        # Increment timestamp
        for ID in timestamps_by_ID:
            if timestamps_by_ID[ID] < departure_time:
                timestamps_by_ID[ID] += ID


def chinese_remainder(n, a):
    """
    Solves and finds X for a system of congruences:
      X = a_1 (mod n_1)
      X = a_2 (mod n_2)
      ...
      X = a_N (mod n_N)
    """
    sum = 0
    prod = reduce(lambda a, b: a * b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod


def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1


def task2(bussIDs):
    """Write the code for task 2 here"""

    timestamps_by_ID = defaultdict(list)
    for offset, ID in enumerate(bussIDs):
        if ID == 'x':
            continue
        timestamps_by_ID['a'].append(int(ID))
        timestamps_by_ID['n'].append(-offset)

    return chinese_remainder(timestamps_by_ID['a'], timestamps_by_ID['n'])


def main():

    puzzle_input = read_data()
    departure_time = int(puzzle_input[0])
    bussIDs = puzzle_input[1].split(',')

    print(f"Solution to task 1: {task1(departure_time, bussIDs)}")
    print(f"Solution to task 2: {task2(bussIDs)}")

main()
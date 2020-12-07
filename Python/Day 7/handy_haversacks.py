import re



from collections import *
from functools import lru_cache
import heapq
import itertools
import math
import random
import sys


def main2():
    fin = open("puzzle_input.txt", "r")
    lines = [line.strip() for line in fin.readlines() if line.strip()]
    f = defaultdict(list)
    g = defaultdict(list)

    for line in lines:
        k, vs = line.split(" contain ")
        k = tuple(k.split()[:-1])
        if vs.startswith("no"):
            continue
        f[k] = [(int(v.split()[0]), tuple(v.split()[1:-1])) for v in vs.split(", ")]
        for _, v in f[k]:
            g[v].append(k)

    q = deque([("shiny", "gold")])
    s = set([tuple(q[0])])
    while q:
        u = q.popleft()
        for x in g[u]:
            if x not in s:
                q.append(x)
                s.add(x)

    print("part 1", len(s) - 1)

    @lru_cache()
    def solve(color):
        ans = 1
        for count, subcol in f[color]:
            ans += count * solve(subcol)

        return ans

    print("part 2", solve(("shiny", "gold")) - 1)



def read_data(path="puzzle_input.txt"):
    """ Reads puzzle input """
    with open(path, 'r') as f:
        data = f.read().split('\n')
    return data

def create_graph(rules):
    graph = defaultdict(list)
    for i, rule in enumerate(rules):
        if "no other bags" in rule:
            rules[i] = {" ".join(rule.split(" ")[0:2]), 0}
            continue
        r = rule.split(",")

        top_bag = tuple(r[0].split(" ")[0:2])
        for r in r[1:]:
            bag = tuple(r.split(" ")[2:4])
            graph[bag].append(top_bag)
    return graph


def solve_graph(rule):
    print(rule.keys())
    if "no other bags" in rule.keys():
        return
    # elif "shiny bag" in rule:
    #     bag_count +=



def main():
    puzzle_input = read_data()

    puzzle_input = create_graph(puzzle_input)
    bag_count = 0


main()










import re
from collections import *
from functools import lru_cache
import heapq
import itertools
import math
import random
import sys


def read_data():
    fin = open("puzzle_input.txt", "r")
    return [line.strip() for line in fin.readlines() if line.strip()]


def create_graph(lines):
    graph = defaultdict(list)
    for i, rule in enumerate(lines):
        if "no other bags" in rule:
            continue

        top_bag, bags = rule.split(" contain ")

        top_bag = tuple(top_bag.split(" ")[0:2])
        for bag in bags.split(", "):
            bag = tuple(bag.split(" ")[1:3])
            graph[bag].append(top_bag)

    return graph


def create_graph_with_count(lines):
    graph = defaultdict(list)
    for i, rule in enumerate(lines):
        if "no other bags" in rule:
            continue

        top_bag, bags = rule.split(" contain ")
        top_bag = tuple(top_bag.split(" ")[0:2])

        for bag in bags.split(", "):
            count, adjective, color = tuple(bag.split(" ")[0:3])
            bag = (int(count), (adjective, color))
            graph[top_bag].append(bag)

    return graph


def find_path(graph, start):
    """ Finds all related vertices from start point in  a directed graph. """
    keys = deque([start])
    path = set([tuple(keys[0])])
    while keys:
        key = keys.popleft()
        for vertice in graph[key]:
            if vertice not in path:
                keys.append(vertice)
                path.add(vertice)
    return path


def count_required_bags(color, graph):
    ans = 1
    for count, subcol in graph[color]:
        ans += count * count_required_bags(subcol, graph)

    return ans


def main():
    lines = read_data()

    graph = create_graph(lines)
    path = find_path(graph, ('shiny', 'gold'))
    print("The number of bag colors that contain at least one shiny bag: ", len(path) - 1)

    graph_with_count = create_graph_with_count(lines)
    answer = count_required_bags(('shiny', 'gold'), graph_with_count)
    print("The required bags inside the shiny gold bag: ", answer - 1)


main()



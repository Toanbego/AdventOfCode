import re


def read_data(path="puzzle_input.txt"):
    """ Reads puzzle input """
    with open(path, 'r') as f:
        data = f.read().split('\n')
    return data


def format_rules(rules):
    for i, rule in enumerate(rules):
        if "no other bags" in rule:
            rules[i] = [" ".join(rule.split(" ")[0:2]), "no other bags"]
        r = rule.split(",")

        sub_rules = [" ".join(r[0].split(" ")[0:2]), r[0].split(" ")[4]]
        for r in r[1:]:
            sub_rules.append(" ".join(r.split(" ")[2:4]))
            sub_rules.append(r[1])

        rules[i] = sub_rules
    return rules

def search_bag_rules(rule):
    if "no other bags." in rule:
        return
    else:
        pass


def main():
    puzzle_input = read_data()
    puzzle_input = format_rules(puzzle_input)

    for i in puzzle_input:
        search_bag_rules(i)

main()










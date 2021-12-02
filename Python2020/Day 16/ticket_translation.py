import numpy as np


def read_data(path="puzzle_input.txt"):
    """Reads puzzle input"""
    fin = open(path, "r")
    lines = [line.strip() for line in fin.readlines() if line.strip()]
    return lines


class TicketScanner:

    def __init__(self, data):
        self.data = data
        self.rules = self.scan_rules()
        self.nearby_tickets = self.scan_nearby_tickets()
        own_ticket_values = [ticket for ticket in self.data[self.data.index('your ticket:')+1:
                                                               self.data.index('nearby tickets:')]][0].split(",")
        self.own_ticket_values = [int(value) for value in own_ticket_values]

    def scan_rules(self):
        """Create a dict with rules set and parameters"""
        rules = {}
        for rule in self.data:
            if 'ticket' in rule:
                break
            rule_name, rule_parameters = rule.split(':')
            param1, param2 = rule_parameters.split(' or ')
            rules[rule_name] = {'range1': [int(param1.split('-')[0]), int(param1.split('-')[1])],
                                'range2': [int(param2.split('-')[0]), int(param2.split('-')[1])]}

        return rules

    def scan_nearby_tickets(self):
        """Create a list of valid tickets"""
        nearby_tickets_start = self.data.index('nearby tickets:')
        nearby_tickets = self.data[nearby_tickets_start+1:]
        return [[int(ticket) for ticket in ticket.split(',')] for ticket in nearby_tickets]

    def check_for_valid_tickets(self):
        """
        Check for the scanned tickets for valid ones. Returns a list of valid tickets as well as the
        invalid fields.
        :return: list: valid tickets, list: invalid fields
        """
        valid_tickets, invalid_field = [], []
        # Loop through tickets
        for ticket in self.nearby_tickets:
            rule_validated = []

            # Check each field in the ticket against each rules
            for field in ticket:

                for rule in self.rules:
                    check_for_valid_field = False

                    if self.rules[rule]['range1'][0] <= field <= self.rules[rule]['range1'][1] \
                    or self.rules[rule]['range2'][0] <= field <= self.rules[rule]['range2'][1]:

                        rule_validated.append(True)
                        check_for_valid_field = True
                        break
                # If a field was not valid, add to list
                if not check_for_valid_field:
                    rule_validated.append(False)
                    invalid_field.append(field)

            # If ticket matches all rules, it valid and added to the list.
            if all(rule_validated):
                valid_tickets.append(ticket)

        return valid_tickets, invalid_field

    def translate_ticket_fields(self, valid_tickets):
        """Translates your ticket by using all validated tickets found as reference"""
        # Dict to hold translates rules and our ticket value
        field_order = {}

        # Loop through several times until all rules have been translated
        while True:
            # Initialize a set of rules
            rules = self.rules

            # Loop through columns
            for i, col in enumerate(np.array(valid_tickets).T):

                # Set rule checker for all rules to zero
                rule_checker = {}
                for rule in rules:
                    rule_checker[rule] = 0

                # Check each field in the column against each rule
                for field in col:
                    for rule in rules:
                        if rules[rule]['range1'][0] <= field <= rules[rule]['range1'][1] \
                                or rules[rule]['range2'][0] <= field <= rules[rule]['range2'][1]:

                            # Add a point to the rule if it matches
                            rule_checker[rule] += 1

                # Find the rule(s) with highest score and its corresponding values
                max_field = max(list(rule_checker.values()))
                matching_field = list(rule_checker.keys())[list(rule_checker.values()).index(max_field)]

                # Sometimes, more than one rule has same high score. Move on to the next column instead
                count = list(rule_checker.values()).count(max_field)
                if count > 1:
                    continue

                # If the rule is found, add it to dict, and remove it from the rule set.
                field_order[matching_field] = int(self.own_ticket_values[i])
                rules.pop(matching_field, None)

                if len(rules) == 1:
                    return field_order


def task1(data):
    """Write the code for task 1 here"""
    ticket_scanner = TicketScanner(data)
    _, invalid_fields = ticket_scanner.check_for_valid_tickets()
    return sum(invalid_fields)


def task2(data):
    """Write the code for task 2 here"""
    ticket_scanner = TicketScanner(data)
    valid_tickets, _ = ticket_scanner.check_for_valid_tickets()
    translated_ticket = ticket_scanner.translate_ticket_fields(valid_tickets)
    departure_values = 1
    for rule in translated_ticket:
        if 'departure' in rule:
            departure_values *= translated_ticket[rule]
    return departure_values


def main():
    puzzle_input = read_data()
    print(f"Solution to task 1: {task1(puzzle_input)}")
    print(f"Solution to task 2: {task2(puzzle_input)}")


main()

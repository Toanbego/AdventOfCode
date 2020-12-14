import re
import requests
import argparse
import sys
import os


def parse_arguments():
    """
    Parse command line arguments
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('--day', '-d', type=str, default='ex', metavar=' ',
                        help='Pick a method for solving travelling salesman problem:\n'
                             'Current methods available:\n\n'
                             ' -m ex    -   Exhaustive search\n'
                             ' -m hc    -   Hill climber search\n'
                             ' -m ga    -   Genetic Algorithm\n'
                             ' -m hybrid    -   Hybrid algorithm')
    parser.add_argument('--route_length', '-r', type=int, default=10, metavar=' ',
                        help='Choose length of route.')
    parser.add_argument("--learning_model", "-l", type=str, default="lamarck", metavar='    ',
                        help='Choose either lamarckian or baldwinian learning method'
                             'Only usable for hybrid method')

    return parser.parse_args()


def create_directory(day):
    if f'Day {day}' in os.listdir(os.getcwd()):
        return
    else:
        os.mkdir(f'{os.getcwd()}/Day {day}')


def create_python_file(day):
    page = requests.get(f'https://adventofcode.com/2020/day/{day}').content
    python_file_name = re.findall(f'Day {day}: (.+) ---', str(page))[0].lower().replace(" ", "_")

    if f'{python_file_name}.py' in os.listdir(f'{os.getcwd()}/Day {day}'):
        return

    python_file = open(f'{os.getcwd()}/Day {day}/{python_file_name}.py', 'w')
    with open('template.txt', 'r') as f:
        for line in f.readlines():
            python_file.writelines(line)

def create_python_file(day):
    page = requests.get(f'https://adventofcode.com/2020/day/{day}/input').content
    filename = 'puzzle_input.txt'

    if f'{filename}' in os.listdir(f'{os.getcwd()}/Day {day}'):
        return

    python_file = open(f'{os.getcwd()}/Day {day}/{filename}', 'w')
    python_file.writelines('Paste input here')


def main():
    # Get day from user input
    day = sys.argv[1]
    assert 1 <= int(day) <= 25, "Please choose a day between 1 and 25."


    create_directory(day)
    create_python_file(day)

    puzzle_input = requests.get(f'https://adventofcode.com/2020/day/{day}/input').content
    print(puzzle_input)


main()



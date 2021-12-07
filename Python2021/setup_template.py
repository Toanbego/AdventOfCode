import re
import sys
import os
import requests as req


def create_directory(day):
    if f'Day {day}' in os.listdir(os.getcwd()):
        return
    else:
        os.mkdir(f'{os.getcwd()}/Day {day}')


def create_python_file(day):
    page = req.get(f'https://adventofcode.com/2021/day/{day}').content
    python_file_name = re.findall(f'Day {day}: (.+) ---', str(page))[0].lower().replace(" ", "_")

    if f'{python_file_name}.py' in os.listdir(f'{os.getcwd()}/Day {day}'):
        return

    python_file = open(f'{os.getcwd()}/Day {day}/{python_file_name}.py', 'w')
    with open('template.txt', 'r') as f:
        for line in f.readlines():
            python_file.writelines(line)


def get_input(day):
    """
    Function to automatically get input and save to file
    :return:
    """
    cookies = {"session": open("credentials", "r").readlines()[0]}
    data = req.get(f'https://adventofcode.com/2021/day/{day}/input', cookies=cookies)
    return data.text


def create_puzzle_input(day):
    if f'puzzle_input' in os.listdir(f'{os.getcwd()}/Day {day}'):
        return

    python_file = open(f'{os.getcwd()}/Day {day}/puzzle_input.txt', 'w')
    python_file.writelines(get_input(day))
    python_file = open(f'{os.getcwd()}/Day {day}/test_input.txt', 'w')
    python_file.writelines('Paste input here')


def main():
    day = sys.argv[1]
    assert 1 <= int(day) <= 25, "Please choose a day between 1 and 25."
    create_directory(day)
    create_python_file(day)
    create_puzzle_input(day)


main()



import re
import argparse
import sys
import os
import json
import requests as req
import urllib.request
import datetime


def get_input():
    """
    Function to automatically get input and save to file
    :return:
    """


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


def create_puzzle_input(day):
    filename = 'puzzle_input.txt'

    if f'{filename}' in os.listdir(f'{os.getcwd()}/Day {day}'):
        return

    python_file = open(f'{os.getcwd()}/Day {day}/{filename}', 'w')
    python_file.writelines('Paste input here')


def main():
    day = sys.argv[1]
    assert 1 <= int(day) <= 25, "Please choose a day between 1 and 25."
    create_directory(day)
    create_python_file(day)
    create_puzzle_input(day)


main()



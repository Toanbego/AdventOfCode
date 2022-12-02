import re
import sys
import os
import requests as req
import datetime


def create_directory(day, year, python_file_name):
    if f'Python{year}' not in os.listdir(os.getcwd()):
        os.mkdir(f'{os.getcwd()}/Python{year}')

    if f'Day {day} - {python_file_name}' not in os.listdir(f"{os.getcwd()}/Python{year}"):
        os.mkdir(f'{os.getcwd()}/Python{year}/Day {day} - {python_file_name}')


def create_python_file(day, year, python_file_name):

    if f'{python_file_name}.py' in os.listdir(f'{os.getcwd()}/Python{year}/Day {day} - {python_file_name}'):
        return

    python_file = open(f'{os.getcwd()}/Python{year}/Day {day} - {python_file_name}/{python_file_name}.py', 'w')
    with open('template.txt', 'r') as f:
        for line in f.readlines():
            python_file.writelines(line)


def get_input(day, year):
    """
    Function to automatically get input and save to file
    :return:
    """
    cookies = {"session": open("credentials", "r").readlines()[0]}
    data = req.get(f'https://adventofcode.com/{year}/day/{day}/input', cookies=cookies)
    return data.text


def create_puzzle_input(day, year, python_file_name):
    if f'puzzle_input' in os.listdir(f'{os.getcwd()}/Python{year}/Day {day} - {python_file_name}'):
        return

    python_file = open(f'{os.getcwd()}/Python{year}/Day {day} - {python_file_name}/puzzle_input.txt', 'w')
    python_file.writelines(get_input(day, year))
    python_file = open(f'{os.getcwd()}/Python{year}/Day {day} - {python_file_name}/test_input.txt', 'w')
    python_file.writelines('Paste input here')


def main():

    day = sys.argv[1]
    year = datetime.date.today().year if len(sys.argv) < 3 else sys.argv[2]
    page = req.get(f'https://adventofcode.com/{year}/day/{day}').content
    python_file_name = re.findall(f'Day {day}: (.+) ---', str(page))[0].lower().replace(" ", "_")
    assert 1 <= int(day) <= 25, "Please choose a day between 1 and 25."
    assert int(year) <= int(datetime.date.today().year), f"I like your spirit, but it is a bit early for the year {year}"
    create_directory(day, year, python_file_name)
    create_python_file(day, year, python_file_name)
    create_puzzle_input(day, year, python_file_name)


main()



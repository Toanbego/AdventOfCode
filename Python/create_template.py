import re
import requests
import argparse
import sys
import os

def create_directory(day):

    if f'Day {day}' in os.listdir(os.getcwd()):
        return
    else:
        os.mkdir(f'{os.getcwd()}/Day {day}')

def main():
    # Get day from user input
    day = sys.argv[1]
    assert 1 <= int(day) <= 25, "Please choose a day between 1 and 25."

    # page = requests.get('https://adventofcode.com/2020/day/1').content
    # title = re.findall(f'Day {1}: (.+) ---', str(page))[0]
    # title =
    create_directory(day)

    python_file_name = 'Shuttle Search'.lower().replace(' ', '_')
    print(python_file_name)
    # with open('')

main()



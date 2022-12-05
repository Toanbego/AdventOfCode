import requests as req
cookies = {"session": open("../../credentials", "r").readlines()[0]}


def submit_answer(day, year):
    response = req.post(
        url=f'https://adventofcode.com/{year}/day/{day}/answer',
        cookies=cookies,
        data={"level": 1, "answer": 416},
    )

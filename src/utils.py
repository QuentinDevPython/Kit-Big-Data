import json


def read_json(filename: str) -> dict:
    with open(filename, "r+", encoding="utf8") as file:
        data = json.load(file)
    return data


def write_json(filename: str, data: dict):
    with open(filename, "w+", encoding="utf8") as file:
        json.dump(data, file)

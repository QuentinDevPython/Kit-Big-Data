"""Utility functions."""

import json
from pathlib import Path


def read_json(filename: str) -> dict:
    """
    Read data from a JSON file.

    :param filename: The name of the JSON file to read.
    :type filename: str
    :return: The data read from the JSON file,
        represented as a dictionary.
    :rtype: dict
    """
    if not Path(Path(__file__).parent / "data/").exists():
        Path.mkdir(Path(__file__).parent / "data/")
    if not Path(Path(__file__).parent / "data" / "tasks.json").exists():
        Path.touch(Path(__file__).parent / "data" / "tasks.json")
        data = {}
        write_json(Path(__file__).parent / "data" / "tasks.json", data)
    with open(filename, "r+", encoding="utf-8") as file:
        data = json.load(file)
    return data


def write_json(filename: str, data: dict):
    """
    Write data to a JSON file.

    :param filename: The name of the JSON file to write to.
    :type filename: str
    :param data: The data to be written to the JSON file,
        represented as a dictionary.
    :type data: dict
    """
    with open(filename, "w+", encoding="utf-8") as file:
        json.dump(data, file)

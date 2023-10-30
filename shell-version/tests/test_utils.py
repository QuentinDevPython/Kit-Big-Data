import json
import os
from pathlib import Path

import pytest

from src.utils import read_json, write_json


@pytest.fixture
def json_file_1():
    file = Path(__file__).parent / "data" / "data1.json"
    return file


@pytest.fixture
def json_file_2():
    file = Path(__file__).parent / "data" / "data2.json"
    return file


def test_read_json(json_file_1):
    data = read_json(json_file_1)
    expected_data = {"key": "value"}
    assert data == expected_data


def test_write_json(json_file_2):
    data_to_write = {"key2": "value2"}
    write_json(json_file_2, data_to_write)

    with open(json_file_2, "r", encoding="utf8") as file:
        data = json.load(file)
    expected_data = data_to_write

    assert data == expected_data

    os.remove(json_file_2)

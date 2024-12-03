import pytest

from src.day_1.part_1 import Part1
from src.read_file import read_input_file


@pytest.fixture
def get_test_input():
    return read_input_file(r"C:\Users\marke\PycharmProjects\advent-of-code-2024-python\src\day_1\test_input.txt")


def test_split_list(get_test_input):
    p1 = Part1(get_test_input)
    list1, list2 = p1.split_lists()

    assert len(list1) == len(list2)
    assert list1 == [3, 4, 2, 1, 3, 3]
    assert list2 == [4, 3, 5, 3, 9, 3]

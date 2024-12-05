import pytest

from src.read_file import read_input_file
from src.template.part_2 import Part2


@pytest.fixture
def get_test_input():
    return read_input_file(r"C:\Users\marke\PycharmProjects\advent-of-code-2024-python\src\day_1\test_input.txt")


def test_solution(get_test_input):
    p2 = Part2(get_test_input)

    sol = p2.solution()

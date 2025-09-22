import pytest

from src.day_2.part_1 import Part1
from src.read_file import read_input_file


@pytest.fixture
def get_test_input():
  return read_input_file(
    r"C:\Users\marke\PycharmProjects\advent-of-code-2024-python\src\day_2\test_input.txt")


def test_solution(get_test_input):
  p1 = Part1(get_test_input)

  sol = p1.solution()

  assert sol == 2


@pytest.mark.parametrize("level, expected", [
  ([7, 6, 4, 2, 1], True),
  ([1, 2, 7, 8, 9], False),
  ([9, 7, 6, 2, 1], False),
  ([1, 3, 2, 4, 5], False),
  ([8, 6, 4, 4, 1], False),
  ([1, 3, 6, 7, 9], True),
])
def test_report_is_safe(level, expected):
  p1 = Part1(["not important string"])

  assert p1.is_safe(level) == expected

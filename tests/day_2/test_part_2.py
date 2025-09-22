import pytest

from src.day_2.part_2 import Part2
from src.read_file import read_input_file


@pytest.fixture
def get_test_input():
  return read_input_file(
      r"C:\Users\marke\PycharmProjects\advent-of-code-2024-python\src\day_2\test_input.txt"
  )


def test_solution(get_test_input):
  p2 = Part2(get_test_input)

  sol = p2.solution()

  assert sol == 4


@pytest.mark.parametrize("level, expected", [
  ([7, 6, 4, 2, 1], True),
  ([1, 2, 7, 8, 9], False),
  ([9, 7, 6, 2, 1], False),
  ([1, 3, 2, 4, 5], True),
  ([8, 6, 4, 4, 1], True),
  ([1, 3, 6, 7, 9], True),
  ([1, 4, 1, 4, 1], False),
  ([65, 68, 71, 72, 71], True),
  ([6, 9, 10, 7, 9, 12, 17], False),
])
def test_report_is_safe(level, expected):
  p2 = Part2(["not important string"])

  assert p2.is_safe(level) == expected

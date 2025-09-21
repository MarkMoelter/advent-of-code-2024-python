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

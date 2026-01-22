import pytest

from src.day_5.part_2 import Part2
from src.read_file import read_input_file


@pytest.fixture
def get_test_input():
  return read_input_file(
      r"C:\Users\marke\PycharmProjects\advent-of-code-2024-python\src\day_5\test_input.txt")


@pytest.skip(allow_module_level=True)
def test_solution(get_test_input):
  p2 = Part2(get_test_input)

  sol = p2.solution()

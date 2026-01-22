import pytest

from src.day_5.part_1 import Part1
from src.read_file import read_input_file


@pytest.fixture
def get_test_input():
  return read_input_file(
      r"C:\Users\marke\PycharmProjects\advent-of-code-2024-python\src\day_5\test_input.txt")


@pytest.skip(allow_module_level=True)
def test_solution(get_test_input):
  p1 = Part1(get_test_input)

  sol = p1.solution()

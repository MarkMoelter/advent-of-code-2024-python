import pytest

from src.day_1.part_2 import Part2
from src.read_file import read_input_file


@pytest.fixture
def get_test_input():
  return read_input_file(
    r"C:\Users\marke\PycharmProjects\advent-of-code-2024-python\src\day_1\test_input.txt")


def test_count_occurrences(get_test_input):
  p2 = Part2(get_test_input)

  right_list = p2.split_lists()[1]

  count_dict = p2.count_occurrences(right_list)

  assert count_dict[3] == 3
  assert count_dict[4] == 1


def test_solution(get_test_input):
  p2 = Part2(get_test_input)

  sol = p2.solution()

  assert sol == 31

import pytest

from src.day_4.part_1 import Part1
from src.read_file import read_input_file


@pytest.fixture
def get_test_input():
  return read_input_file(
      r"C:\Users\marke\PycharmProjects\advent-of-code-2024-python\src\day_4\test_input.txt")


def test_solution(get_test_input):
  p1 = Part1(get_test_input)

  sol = p1.solution()

  assert sol == 18


@pytest.mark.parametrize(
    "coordinates, expected_result", [
      ((0, 0), "M"),
      ((0, 2), "A"),
      ((9, 9), "X"),
    ])
def test_word_search_dict(get_test_input, coordinates, expected_result):
  p1 = Part1(get_test_input)

  p1.create_word_search_dict()

  assert p1.word_search_dict[coordinates] == expected_result


@pytest.mark.parametrize(
    "coordinates, letter_to_look_for, expected_result", [
      pytest.param((1, 1), "M", (2, 0), id="test getting correct coordinates"),
      pytest.param((0, 0), "S", (1, 1), id="test corners"),
    ]
)
def test_check_neighbors(get_test_input, coordinates, letter_to_look_for,
    expected_result):
  p1 = Part1(get_test_input)
  neighbors = p1.check_neighbors(coordinates, letter_to_look_for)

  assert expected_result in neighbors

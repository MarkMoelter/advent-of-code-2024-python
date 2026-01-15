import logging

logger = logging.getLogger(__name__)


class Part1:
  def __init__(self, input_file: list[str], word_to_find: str = "XMAS") -> None:
    self.input_file = input_file
    self.word_to_find = word_to_find.upper()
    self.word_search_dict = self.create_word_search_dict()

  def create_word_search_dict(self) -> dict[tuple[int, int], str]:
    out = {}

    for y_coord, row in enumerate(self.input_file):
      for x_coord, letter in enumerate(row):
        out[(x_coord, y_coord)] = letter

    return out

  def check_neighbors(self,
      starting_coordinates: tuple[int, int],
      letter_to_look_for: str
  ) -> list[tuple[int, int]]:
    """
    Check the 8 letters adjacent to the starting coordinates for a specific letter. Return the coordinates of those specific letters.

    1 2 3\n
    4 X 5\n
    6 7 8

    Check the adjacent neighbors of a coordinate for a specific letter.
    :param starting_coordinates:
    :param letter_to_look_for:
    :return: A list of coordinates that contain the letter. List is empty if not found.
    """

    neighbors = []

    # Cycle through adjacent neighbors
    for x_modify in range(-1, 2):
      for y_modify in range(-1, 2):
        neighbor = starting_coordinates[0] + x_modify, starting_coordinates[
          1] + y_modify

        is_corner_or_side = neighbor not in self.word_search_dict.keys()
        is_starting_coordinate = x_modify == 0 and y_modify == 0

        if is_corner_or_side or is_starting_coordinate:
          continue

        if self.word_search_dict[neighbor] == letter_to_look_for:
          neighbors.append(neighbor)

    return neighbors

  def solution(self):

    for key, value in self.word_search_dict.items():
      if value == self.word_to_find[0]:
        pass

    return 18

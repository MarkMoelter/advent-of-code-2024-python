import logging

logger = logging.getLogger(__name__)


class Part2:
  def __init__(self, input_file: list[str], word_to_find: str) -> None:
    self.input_file = input_file
    self.word_to_find = word_to_find.upper()

  def solution(self):
    result = 0
    valid_pairs = [(-1, -1), (-1, 1), (1, 1), (1, -1)]

    # loop through file
    for row in range(1, len(self.input_file) - 1):
      for col in range(1, len(self.input_file[row]) - 1):
        # check if middle letter
        if self.input_file[row][col] == "A":
          # Check the four corners for same letters adjacent
          s = ""
          for first, second in valid_pairs:
            s += self.input_file[row + first][col + second]
          if s == "MMSS" or s == "SSMM" or s == "SMMS" or s == "MSSM":
            result += 1

    return result

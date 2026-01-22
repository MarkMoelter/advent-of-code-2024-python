import logging

logger = logging.getLogger(__name__)


class Part1:
  def __init__(self, input_file: list[str], word_to_find: str = "XMAS") -> None:
    self.input_file = input_file
    self.word_to_find = word_to_find.upper()

  def solution(self):
    result = 0

    # loop through file
    for r_idx, row in enumerate(self.input_file):
      for c_idx, letter in enumerate(row):
        # check if starting letter
        if letter == self.word_to_find[0]:
          # get the direction of the
          for drow in range(-1, 2):
            for dcol in range(-1, 2):
              if drow == dcol == 0:
                continue
              # Check that direction for the word
              is_valid = True
              for i in range(len(self.word_to_find)):
                r2 = r_idx + drow * i
                c2 = c_idx + dcol * i

                is_inside = 0 <= r2 < len(
                    self.input_file) and 0 <= c2 < len(self.input_file[0])
                if not is_inside:
                  is_valid = False
                  break

                is_correct_letter = self.input_file[r2][c2] == \
                                    self.word_to_find[i]
                if not is_correct_letter:
                  is_valid = False
                  break
              if is_valid:
                result += 1

    return result

import logging

from src.day_2.part_1 import Part1

logger = logging.getLogger(__name__)


class Part2(Part1):
  def __init__(self, input_file: list[str]) -> None:
    super().__init__(input_file)

  @staticmethod
  def is_safe(report: list[int], tolerance: int = 1, min_differ: int = 1,
      max_differ: int = 3) -> bool:
    """
    Check if the report is safe.
    :param report: The report to check.
    :param tolerance: The number of bad levels that can be tolerated before failing.
    :param min_differ: The minimum separation distance between two adjacent values.
    :param max_differ: The maximum separation distance between two adjacent values.
    :return: A boolean indicating if the report is safe.
    """
    sign: str | None = None
    prev_sign: str | None = None

    # todo: iter through list, if not safe, pop the unsafe value off and decrement tolerance.
    #  True if it gets to end of list without returning false or tolerance dropping below 0
    #  False if tolerance drops below 0
    for idx, num in enumerate(report):

      # skip first num
      if idx == 0:
        continue

      # return false if tolerance falls below 0, this is the fail condition for previous recursive call
      if tolerance < 0:
        return False

      difference = num - report[idx - 1]

      # set sign for always incrementing and decrementing
      if difference > 0:
        sign = "inc"
      elif difference < 0:
        sign = "dec"

      if prev_sign is None:
        prev_sign = sign

      is_acceptable_difference = min_differ <= abs(difference) <= max_differ

      sign_matches_prev_sign = sign == prev_sign

      if not is_acceptable_difference or not sign_matches_prev_sign:
        report.pop(idx - 1)  # Remove previous value from report
        return Part2.is_safe(report, tolerance - 1)

    return True

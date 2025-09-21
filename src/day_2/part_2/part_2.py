import logging

from src.day_2.part_1 import Part1

logger = logging.getLogger(__name__)


class Part2(Part1):
  def __init__(self, input_file: list[str]) -> None:
    super().__init__(input_file)

  @staticmethod
  def is_safe(report: list[int], tolerance: int = 1) -> bool:
    """
    Check if the report is safe.
    :param report: The report to check.
    :param tolerance: The number of bad levels that can be tolerated before failing.
    :return: A boolean indicating if the report is safe.
    """
    threshold = 3
    report_change = []
    bad_levels = 0

    # Handle safe condition: adjacent levels differ by 1 to 3
    for idx, val in enumerate(report):
      # Skip last element
      if idx == len(report) - 1:
        continue
      # Handle
      if bad_levels > tolerance:
        return False

      difference = val - report[idx + 1]
      if abs(difference) > threshold or difference == 0:
        bad_levels += 1

      report_change.append(difference)

    # Handle safe condition: levels either all increase or all decrease
    neg_count, pos_count = 0, 0
    for num in report_change:
      if num > 0:
        pos_count += 1

      elif num < 0:
        neg_count += 1
    # Return False if both counts are greater than one, True otherwise
    return not (neg_count > 0 and pos_count > 0)

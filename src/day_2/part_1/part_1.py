import logging

logger = logging.getLogger(__name__)


class Part1:
  def __init__(self, input_file: list[str]) -> None:
    self.input_file = input_file

  @staticmethod
  def is_safe(report: list[int]) -> bool:
    """
    Check if the report is safe.
    :param report:
    :return:
    """
    threshold = 3
    report_change = []

    # Handle safe condition: adjacent levels differ by 1 to 3
    for idx, val in enumerate(report):
      if idx == len(report) - 1:
        continue

      difference = val - report[idx + 1]
      if abs(difference) > threshold or difference == 0:
        return False

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

  def solution(self) -> int:
    num_safe_reports = 0

    for line in self.input_file:
      report = list(map(int, line.split()))
      if self.is_safe(report):
        num_safe_reports += 1

    return num_safe_reports

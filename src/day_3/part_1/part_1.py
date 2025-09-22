import logging
import re

logger = logging.getLogger(__name__)


class Part1:
  def __init__(self, input_file: list[str]) -> None:
    self.input_file = input_file

  def solution(self) -> int:
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"

    sol = 0

    for line in self.input_file:
      for m in re.finditer(pattern, line):
        sol += int(m.group(1)) * int(m.group(2))

    return sol

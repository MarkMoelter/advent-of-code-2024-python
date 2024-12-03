import logging

from src.day_1.part_1 import Part1

logger = logging.getLogger(__name__)


class Part2(Part1):
    def __init__(self, input_file: list[str]) -> None:
        super().__init__(input_file)

    @staticmethod
    def count_occurrences(num_list: list[int]) -> dict[int, int]:
        """
        Count the number of times each number occurs in the list.
        :return: A dictionary mapping each number to the number of occurrences.
        """
        result = {}

        for num in num_list:
            if num in result:
                result[num] += 1
                continue

            result[num] = 1

        return result

    def solution(self) -> int:
        left, right = self.split_lists()

        occurrences = self.count_occurrences(right)

        total = 0

        for num in left:
            if num in occurrences:
                total += num * occurrences[num]

        return total

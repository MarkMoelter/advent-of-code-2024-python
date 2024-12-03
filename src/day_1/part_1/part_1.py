import logging
import math
import re

logger = logging.getLogger(__name__)


class Part1:
    def __init__(self, input_file: list[str]) -> None:
        self.input_file = input_file

    def split_lists(self) -> tuple[list[int], list[int]]:
        """
            Split the input file into two lists.
        """
        list1 = []
        list2 = []

        for line in self.input_file:
            # Replace multi spaces with a single space, so it can be split
            split_str = re.sub(r" +", r" ", line).split()

            # Validate the list only contains two values
            assert len(split_str) == 2

            # Convert the strings to ints
            split_int = list(map(int, split_str))

            list1.append(split_int[0])
            list2.append(split_int[1])

        return list1, list2

    def solution(self) -> int:
        left_list, right_list = self.split_lists()

        # Sort lists
        left_list.sort()
        right_list.sort()

        tot_distance = 0

        for val1, val2 in zip(left_list, right_list):
            tot_distance += abs(val1 - val2)

        return tot_distance

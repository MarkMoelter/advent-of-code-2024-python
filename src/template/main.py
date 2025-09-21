import logging

from src.read_file import read_input_file
from src.template.part_1 import Part1
from src.template.part_2 import Part2


def main():
  input_file = read_input_file()

  # part 1
  p1 = Part1(input_file)
  logging.info(p1.solution())

  # part 2
  p2 = Part2(input_file)
  logging.info(p2.solution())


if __name__ == '__main__':
  logging.basicConfig(level=logging.DEBUG)
  # logging.disable(logging.DEBUG)
  main()

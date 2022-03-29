"""
Own module
"""

import math
import sys


def circle_area(r):
    return math.pi * r ** 2


def circumference_of_the_wheel(r):
    return math.pi * r * 2


def main():
    print(sys.argv)
    print(circle_area(int(sys.argv[1])))
    print(circumference_of_the_wheel(int(sys.argv[2])))


if __name__ == "__main__":
    main()

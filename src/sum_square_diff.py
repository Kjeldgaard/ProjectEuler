#!/user/bin/env python3 -tt
"""
Sum square difference
https://projecteuler.net/problem=6
"""

# Imports
import sys
import argparse


def square_sum(number :int) -> int:
    return int((2 * number + 1) * number * (number + 1) / 6)


def sum_square(number :int) -> int:
    return int((number * (number + 1) / 2)**2)


def main(number :int):
    print(square_sum(number))
    print(sum_square(number))
    diff = sum_square(number) - square_sum(number)
    print(f"sum square diff: {diff}")
    return

# Main body
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Find sum square diff from 1 to n.')
    parser.add_argument('n', 
                        type = int,
                        help = 'Upper range.')

    args = parser.parse_args()
    main(args.n)

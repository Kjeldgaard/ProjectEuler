#!/user/bin/env python3 -tt
"""
Multiples of 3 and 5
https://projecteuler.net/problem=1
"""

# Imports
import sys
import argparse


def sum_of_multiples(number :int, divisor :int) -> int:
    max_multiple = int((number - 1) / divisor)
    times_multiple = float((max_multiple + 1) / 2) * max_multiple
    sum_of_multiples = int(divisor * times_multiple)
    return sum_of_multiples


def main(number :int, divisor1 :int, divisor2 :int):
    print(f"Number {number} and divisors {divisor1} and {divisor2}")
    sum_multiples = sum_of_multiples(number, divisor1)
    sum_multiples += sum_of_multiples(number, divisor2)
    overlapping = sum_of_multiples(int(number / divisor1), divisor2) * divisor1 
    sum_multiples -= overlapping
    print(f"Sum of multiples: {sum_multiples}")
    return

# Main body
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('n', 
                        type = int,
                        help = 'Number to find sum of dividers')
    parser.add_argument('d1',
                        type = int,
                        help = 'Divisor 1.')

    parser.add_argument('d2',
                        type = int,
                        help = 'Divisor 2.')

    args = parser.parse_args()
    main(args.n, args.d1, args.d2)

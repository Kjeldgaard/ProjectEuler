#!/user/bin/env python3 -tt
"""
Smallest multiple
https://projecteuler.net/problem=5
"""

# Imports
import sys
import argparse


def smallest_divisible(number: int) -> int:
    if number < 1:
        print(f"Number must be larger than 0.")
        sys.exit(1)

    if number == 1:
        return 1
    if number == 2:
        return 2
    
    for value in range(2, int(number / 2)):
        if number % value == 0:
            return value
    
    return number


def main(number :int):
    multiple = 1
    for value in range(1, number + 1):
        if multiple % value != 0:
            multiple *= smallest_divisible(value)

    print(f"Smallest number that is divisible of all number in range 1 to {number}: {multiple}")
    return

# Main body
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Find smallest multiple from 1 to n.')
    parser.add_argument('n', 
                        type = int,
                        help = 'Max number of multiple range.')

    args = parser.parse_args()
    main(args.n)

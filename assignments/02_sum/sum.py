#!/usr/bin/env python3
"""
Author : Kenneth Schackart <schackartk1@gmail.com>
Date   : 2021-09-15
Purpose: Print the sum of two integers
"""

import argparse
from typing import NamedTuple, List


class Args(NamedTuple):
    """ Command-line arguments """
    int: List[int]


# --------------------------------------------------
def get_args() -> Args:
    """ Get command-line arguments """

    parser = argparse.ArgumentParser(
        description='take it step by step',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('int',
                        metavar='int',
                        type=int,
                        help='Integers to be added',
                        nargs='+')

    args =  parser.parse_args()

    return Args(args.int)


# --------------------------------------------------
def main() -> None:
    """ Make a jazz noise here """

    args = get_args()

    nums = args.int

    nums.append(sum(nums))

    num_str = [str(x) for x in nums]

    print(' + '.join(num_str[:-1]) + ' = ' + num_str[-1])


# --------------------------------------------------
if __name__ == '__main__':
    main()

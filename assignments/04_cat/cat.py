#!/usr/bin/env python3
"""
Author : Kenneth Schackart <schackartk1@gmail.com>
Date   : 2021-09-22
Purpose: Python version of cat
"""

import argparse
from typing import NamedTuple, TextIO


class Args(NamedTuple):
    """ Command-line arguments """
    files: TextIO
    number: bool


# --------------------------------------------------
def get_args() -> Args:
    """ Get command-line arguments """

    parser = argparse.ArgumentParser(
        description='Python cat',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('files',
                        metavar='FILE',
                        help='Input file(s)',
                        nargs='+',
                        type=argparse.FileType('rt'))

    parser.add_argument('-n',
                        '--number',
                        help='Number the lines',
                        action='store_true')

    args = parser.parse_args()

    return Args(args.files, args.number)


# --------------------------------------------------
def main() -> None:
    """ The Good Stuff """

    args = get_args()
    files = args.files
    num = args.number

    line_num = 0

    for file in files:
        for line_num, line in enumerate(file):
            out_str = ''
            if num:
                out_str += f'{line_num + 1:6d}\t'
            out_str += f'{line.rstrip()}'

            print(out_str)


# --------------------------------------------------
if __name__ == '__main__':
    main()

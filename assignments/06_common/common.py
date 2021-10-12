#!/usr/bin/env python3
"""
Author : Kenneth Schackart <schackartk1@gmail.com>
Date   : 2021-10-12
Purpose: Find common words in 2 files
"""

import argparse
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Find common words in 2 files',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file_1',
                        metavar='FILE1',
                        help='Input file 1',
                        type=argparse.FileType('rt'))

    parser.add_argument('file_2',
                        metavar='FILE2',
                        help='Input file 2',
                        type=argparse.FileType('rt'))

    parser.add_argument('-o',
                        '--outfile',
                        help='Output file',
                        metavar='FILE',
                        type=argparse.FileType('wt'),
                        default=sys.stdout)

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    file_1 = args.file_1
    file_2 = args.file_2

    words = {}

    for file in [file_1, file_2]:
        words[file.name] = set()
        for line in file:
            for word in line.split():
                words[file.name].add(word)

    for common in words[file_1.name].intersection(words[file_2.name]):
        print(common, file=args.outfile)


# --------------------------------------------------
if __name__ == '__main__':
    main()

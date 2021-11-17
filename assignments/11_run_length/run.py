#!/usr/bin/env python3
"""
Author : Kenneth Schackart <schackartk1@gmail.com>
Date   : 2021-11-17
Purpose: DNA compression
"""

import argparse
import os


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='DNA compression',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('dna', metavar='str', help='DNA text or file')

    args = parser.parse_args()

    if os.path.isfile(args.dna):
        args.dna = open(args.dna).read().rstrip()

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    dna = args.dna

    for seq in dna.splitlines():
        print(rle(seq))


# --------------------------------------------------
def rle(seq):
    """Encode"""

    compressed = ''
    last_base = ''
    rep = 1

    for base in seq:
        if base != last_base:
            if rep > 1:
                compressed += str(rep)
            compressed += base
            rep = 1
        else:
            rep += 1
        last_base = base

    if rep > 1:
        compressed += str(rep)

    return compressed


# --------------------------------------------------
def test_rle():
    """Test rle"""

    assert rle('AA') == 'A2'
    assert rle('ACCGGGTTTT') == 'AC2G3T4'
    assert rle('AACCAA') == 'A2C2A2'


# --------------------------------------------------
if __name__ == '__main__':
    main()

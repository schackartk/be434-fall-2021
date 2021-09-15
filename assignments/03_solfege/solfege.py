#!/usr/bin/env python3
"""
Author : Kenneth Schackart <schackartk1@gmail.com>
Date   : 2021-09-15
Purpose: Do Rey Mi
"""

import argparse
from typing import NamedTuple, List


class Args(NamedTuple):
    """ Command-line arguments """
    syllable: List[str]


# --------------------------------------------------
def get_args() -> Args:
    """ Get command-line arguments """

    parser = argparse.ArgumentParser(
        description='take it step by step',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('syllable',
                        metavar='str',
                        nargs='+',
                        help='A syllable')

    args = parser.parse_args()

    return Args(args.syllable)


# --------------------------------------------------
def main() -> None:
    """ Make a jazz noise here """

    args = get_args()
    syllables = args.syllable

    song = {
            'Do': 'A deer, a female deer',
            'Re': 'A drop of golden sun',
            'Mi': 'A name I call myself',
            'Fa': 'A long long way to run',
            'Sol': 'A needle pulling thread',
            'La': 'A note to follow sol',
            'Ti': 'A drink with jam and bread'
            }
    
    for syllable in syllables:
        if syllable not in song.keys():
            print(f'I don\'t know "{syllable}"')
            continue
        print(f'{syllable}, {song[syllable]}')


# --------------------------------------------------
if __name__ == '__main__':
    main()

#!/usr/bin/env python3

"""
title: Independent Alleles
author: Colin Phoebe
date: 2024-12-14
"""

from typing import NamedTuple
import argparse
from scipy import stats

# -------------------------
# Command line stuff

class Args(NamedTuple):
    """ Command line arguments """

    k: int
    N: int


def get_args() -> Args:
    """ Process command line arguments """

    parser = argparse.ArgumentParser(
            description = "Compute P(at least N children are AaBb in k-th \
                    generation) if all parent pairs are AaBb.",
            formatter_class = argparse.ArgumentDefaultsHelpFormatter
    )

    parser.add_argument(
            "k",
            metavar = "gen",
            type = int,
            help = "Input number of generations"
    )

    parser.add_argument(
            "N",
            metavar = "children",
            type = int,
            help = "Input N as in P(at least N children ...) (see description)"
    )

    args = parser.parse_args()

    return Args(args.k, args.N)


# -------------------------
# MAIN

def main() -> None:
    """ The main brain """

    args = get_args()

    # P(AaBb child from AaBb x AaBb cross)
    p = 0.25

    print(1 - (stats.binom.cdf(args.N - 1, 2 ** args.k, p)))



if __name__ == "__main__":
    main()

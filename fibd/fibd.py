#! /usr/bin/env python3

"""
title: Mortal Fibonacci Rabbits
author: Colin Phoebe
date: 2025-01-23
"""

import argparse
from typing import NamedTuple
import numpy as np



# -----------------------------------
# Handle command-line input

class Args(NamedTuple):
    """ Command-line arguments """

    gens: int
    lifespan: int


def get_args() -> Args:
    """ Get command-line arguments """

    parser = argparse.ArgumentParser(
        description = "Fibonacci rabbits after n generations, but if they were mere mortals. Litter size is always 1.",
        formatter_class = argparse.ArgumentDefaultsHelpFormatter
    )

    parser.add_argument(
        "gens",
        metavar = "GENERATIONS",
        type = int,
        help = "Input number of generations (Fibonacci iterations)"
    )

    parser.add_argument(
        "lifespan",
        metavar = "LIFESPAN",
        type = int,
        help = "Input number of months each generation of rabbits lives for."
    )

    args = parser.parse_args()

    return Args(gens = args.gens, lifespan = args.lifespan)



# -----------------------------------
# Functions

def fibd(n: int, m: int) -> int:
    """
    Fibonacci rabbits but if they died after M months.
    Litter size is always 1.
    """

    rabbits = np.zeros((n + 1), dtype = int)
    rabbits[:2] = 1

    for i in range(2, n + 1):
        if i <= m:
            rabbits[i] = rabbits[i - 2] + rabbits[i - 1]
        else:
            rabbits[i] = rabbits[i - 2] + rabbits[i - 2] - rabbits[i - m - 1]

    return rabbits


# -----------------------------------
# MAIN

def main() -> None:
    """ The main brain """

    args = get_args()

    # compute and print
    rabbids = fibd(args.gens, args.lifespan)
    print(rabbids)


if __name__ == "__main__":
    main()

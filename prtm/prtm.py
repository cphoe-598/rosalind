#!/usr/bin/env python3

"""
title: Calculating Protein Mass
author: Colin Phoebe
date: 2024-12-12
"""

import argparse
from typing import NamedTuple


# -------------------------
# Command Line Stuff

class Args(NamedTuple):
    """ Command line arguments """

    prt: str


def get_args() -> Args:
    """ Get command-line arguments """

    parser = argparse.ArgumentParser(
            description = "Calculate monoisotopic mass of protein string",
            formatter_class = argparse.ArgumentDefaultsHelpFormatter
            )

    parser.add_argument(
            "prt",
            metavar = "PRT",
            type = str,
            help = "Input amino acid string"
    )

    args = parser.parse_args()

    return Args(args.prt)


# -------------------------
# MAIN

def main() -> None:
    """ The main brain """

    monoisotope_masses = {
            "A" : 71.03711, "C" : 103.00919, "D" : 115.02694, "E" : 129.04259,
            "F" : 147.06841, "G" : 57.02146, "H" : 137.05891, "I" : 113.08406,
            "K" : 128.09496, "L" : 113.08406, "M" : 131.04049, "N" : 114.04293,
            "P" : 97.05276, "Q" : 128.05858, "R" : 156.10111, "S" : 87.03203,
            "T" : 101.04768, "V" : 99.06841, "W" : 186.07931, "Y" : 163.06333
    }

    args = get_args()

    print(sum(monoisotope_masses[aa] for aa in args.prt))


if __name__ == "__main__":
    main()

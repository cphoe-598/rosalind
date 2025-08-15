#!/usr/bin/env python3

"""
title: Inferring mRNA From Protein
author: Colin Phoebe
date: 2025-04-29
description:
    - Given: A protein string of length at least 1000 aa
    - Return: The total number of different RNA strings from which the protein
        could have been translated, modulo 1,000,000 for memory considerations
"""

from collections import Counter
from typing import NamedTuple
import argparse


# ----------------------------------------------------------------------------
# ARGPARSE

class Args(NamedTuple):
    """ Command line arguments """

    prot: str


def get_args() -> Args:
    """ Get command line arguments """

    parser = argparse.ArgumentParser(
            description = "Inferring mRNA From Protein",
            formatter_class = argparse.ArgumentDefaultsHelpFormatter
    )

    parser.add_argument(
            "prot",
            metavar = "PROT",
            type = str,
            help = "Input protein string"
    )

    args = parser.parse_args()

    return Args(args.prot.upper())


# ----------------------------------------------------------------------------
# FUNCTIONS

def count_reverse_translations(prot: str) -> int:
    """
    Count the possible reverse translations (aa -> mRNA) of a protein.
    For memory considerations, the returned value is modulo 1,000,000.
    """

    modulo = 1000000

    # counts of possible codons that could've translated into each amino acid
    from_codons = {'A': 4, 'C': 2, 'D': 2, 'E': 2, 'F': 2, 'G': 4, 'H': 2,
                   'I': 3, 'K': 2, 'L': 6, 'M': 1, 'N': 2, 'P': 4, 'Q': 2,
                   'R': 6, 'S': 6, 'T': 4, 'V': 4, 'W': 1, 'Y': 2}

    # number of STOP codons
    stop_codons = 3

    # count the frequency of each amino acid
    aa_freqs = Counter(prot)

    combinations = 1
    for aa, freq in aa_freqs.items():

        # incorporate the number of combinations that this amino acid will add
        added_combinations = from_codons[aa] ** freq
        combinations = (combinations * added_combinations) % modulo

    return (combinations * stop_codons) % modulo


# ----------------------------------------------------------------------------
# MAIN

def main():
    """ The main brain """

    prot = get_args().prot
    print(count_reverse_translations(prot))



if __name__ == "__main__":
    main()

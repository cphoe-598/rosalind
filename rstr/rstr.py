#!/usr/bin/env python3

"""
title: Matching Random Motifs
author: Colin Phoebe
date: 2025-06-29
description: ...
"""

from functools import reduce
from operator import mul


# ----------------------------------------------------------------------------
# FUNCTIONS

def prob_random_motif(dna: str, gc: float, n: int) -> float:
    """
    Given a DNA string S, return the probability that at least one out of N
    randomly created hypothetical DNA strings will match S exactly, given a
    certain GC-content.
    """

    p_gc = gc / 2
    p_at = (1 - gc) / 2

    # P( one match )
    p_match = reduce(mul, [p_gc if bp in ("G", "C") else p_at for bp in dna])

    # P( no match )
    p_no_match = 1 - p_match

    # P( at least one match out of n )
    return round(1 - (p_no_match ** n), 3)


# ----------------------------------------------------------------------------
# MAIN

def main():
    """ The main brain """

    filename = "rosalind_rstr.txt"
    with open(filename, "r") as f:
        n_dna, gc = f.readline().strip().split(" ")
        n_dna = int(n_dna)
        gc = float(gc)
        dna = f.readline().strip()

    print(prob_random_motif(dna, gc, n_dna))


if __name__ == "__main__":
    main()

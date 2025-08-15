#!/usr/bin/env python3

"""
title: Introduction To Random Strings
author: Colin Phoebe
date: 2025-06-29
description: ...
"""

import math
from functools import reduce
from operator import mul


# ----------------------------------------------------------------------------
# FUNCTIONS

def prob_random_dna(dna: str, gc: float) -> float:
    """
    Given a DNA string S, return the probability of a random string being
    created that matches S exactly, given a floating-point value representing
    the hypothetical string's GC-content.
    """

    p_gc = gc / 2  # P(G) = P(C) = GC-content / 2
    p_at = (1 - gc) / 2

    return round(math.log10(reduce(mul, [p_gc if bp in ("G", "C") else p_at for bp in dna])), 3)
    

# ----------------------------------------------------------------------------
# MAIN

def main():
    """ The main brain """
    
    filename = "rosalind_prob.txt"

    with open(filename, "r") as f:
        s = f.readline().strip()
        gc_contents = tuple(map(float, f.readline().strip().split(" ")))

    print(*[prob_random_dna(s, gc) for gc in gc_contents], end = " ")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3

"""
title: Majority Element
author: Colin Phoebe
date: 2025-06-29
description: Find the majority element (if exists) of an array.
    An array has a majority element if over half its entries are the same.
"""

from collections import defaultdict
from itertools import islice


# ----------------------------------------------------------------------------
# FUNCTIONS

def majority_element(arr):
    """ Return the majority element (if exists) of an array """

    counts = defaultdict(int)

    for ele in arr:
        counts[ele] += 1

    half = len(arr) // 2
    for item in counts:
        if counts[item] > half:
            return item

    return -1


# ----------------------------------------------------------------------------
# MAIN

def main():
    """ The main brain """

    filename = "./rosalind_maj.txt"
    with open(filename, "r") as f:
        n, size = f.readline().strip().split(" ")
        arrays = [tuple(map(int, a.strip().split(" "))) for a in islice(f, 0, None)]

    print(*[majority_element(arr) for arr in arrays], end = " ")


if __name__ == "__main__":
    main()

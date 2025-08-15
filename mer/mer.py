#!/usr/bin/env python3

"""
title: Merge Two Sorted Arrays
author: Colin Phoebe
date: 2025-06-20
description: Merge two sorted arrays (ascending)
"""

from itertools import islice


# ----------------------------------------------------------------------------
# FUNCTIONS

def merge_sorted_arrays(arr1, arr2):
    """ Merge Sorted Arrays """

    res = []
    while arr1 and arr2:
        a, b = arr1[0], arr2[0]
        if a < b:
            res.append(arr1.pop(0))
        elif b < a:
            res.append(arr2.pop(0))
        else:
            res.append(arr1.pop(0))
            res.append(arr2.pop(0))

    if arr1:
        res.extend(arr1)
    if arr2:
        res.extend(arr2)

    return res

# ----------------------------------------------------------------------------
# MAIN

def main():
    """ The main brain """

    filename = "./rosalind_mer.txt"

    with open(filename, "r") as f:
        arr1, arr2 = [list(map(int, a.split(" "))) for a in islice(f, 1, None, 2)]

    merged = merge_sorted_arrays(arr1, arr2)

    print(*[item for item in merged], end = " ")


if __name__ == "__main__":
    main()

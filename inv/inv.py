#!/usr/bin/env python3

"""
title: Counting Inversions
author: Colin Phoebe
date: 2025-06-29
description: The number of inversions of an array represents how far away it
    is from being sorted.

    Given array [-6 1 15 8 10], travel left to right. At each element, count
    how many elements to the right of it are smaller than it. Add this to the
    total number of inversions. Continue until you've covered the entire array
"""

from itertools import dropwhile


# ----------------------------------------------------------------------------
# FUNCTIONS

def count_inversions(arr):
    """ DOCSTRING """

    total = 0
    for i in range(len(arr)):
        total += len(list(dropwhile(lambda x: x > arr[i], arr[i+1:])))

    return total


# ----------------------------------------------------------------------------
# MAIN

def main():
    """ The main brain """

    filename = "./rosalind_inv.txt"
    with open(filename, "r") as f:
        size = int(f.readline())
        arr = [int(item) for item in f.readline().split(" ")]

    inversions = count_inversions(arr)
    print(inversions)


if __name__ == "__main__":
    main()

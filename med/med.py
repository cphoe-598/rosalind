#!/usr/bin/env python3

"""
title: Median
author: Colin Phoebe
date: 2025-06-30
description: Find the k-th smallest (non-unique) element of an array
"""


# ----------------------------------------------------------------------------
# FUNCTIONS

def kth_smallest(arr, k: int):
    """ Return the k-th smallest (non-unique) element of an array """

    return sorted(arr)[k - 1]


# ----------------------------------------------------------------------------
# MAIN

def main():
    """ The main brain """

    filename = "./rosalind_med.txt"
    with open(filename, "r") as f:
        size = int(f.readline().strip())
        arr = tuple(map(int, f.readline().strip().split(" ")))
        k = int(f.readline().strip())

    print(kth_smallest(arr, k))


if __name__ == "__main__":
    main()

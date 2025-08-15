#!/usr/bin/env python3

"""
title: Binary Search
author: Colin Phoebe
date: 2025-06-28
description: Binary search
"""

from itertools import islice


# ----------------------------------------------------------------------------
# FUNCTIONS

def binary_search(arr, query, start_idx = 0) -> int:
    """ Binary search of ALREADY-SORTED collection """

    # if item not in arr
    if not arr:
        return -1
    
    # find middle position, item
    mid_i = len(arr) // 2
    mid = arr[mid_i]

    # item found!
    if mid == query:
        return mid_i + start_idx + 1

    # search in upper half
    if mid < query:
        return binary_search(arr[mid_i+1:],
                             query,
                             start_idx + mid_i + 1)

    # search in lower half
    if mid > query:
        return binary_search(arr[:mid_i],
                             query,
                             start_idx)


# ----------------------------------------------------------------------------
# MAIN

def main():
    """ The main brain """

    filename = "rosalind_bins.txt"

    with open(filename, "r") as f:
        # get array size, and the number of searches
        arr_size, n_searches = map(int, [l.strip() for l in islice(f, 0, 2)])

        # get the array, and the searches to be made
        arr, searches = [tuple(map(int, l.strip().split(" "))) for l in islice(f, 0, None)]

    res = " ".join([str(binary_search(arr, searches[i])) for i in range(n_searches)])
    print(res)


if __name__ == "__main__":
    main()

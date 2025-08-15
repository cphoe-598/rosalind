#!/usr/bin/env python3

"""
title: Merge Sort
author: Colin Phoebe
date: 2025-06-29
description: Merge sort
"""


# ----------------------------------------------------------------------------
# FUNCTIONS

def merge_sorted_arrays(arr1, arr2):
    """ Merge two sorted arrays """

    res = []

    while arr1 and arr2:
        a, b = arr1[0], arr2[0]
        if a < b:
            res.append(arr1.pop(0))
        elif b < a:
            res.append(arr2.pop(0))
        else:
            res.extend([arr1.pop(0), arr2.pop(0)])

    if arr1:
        res.extend(arr1)
    if arr2:
        res.extend(arr2)

    return res


def merge_sort(arr):
    """ Merge sort """

    length = len(arr)

    # base case; found singleton
    if length == 1:
        return arr

    # divide array in two
    mid = length // 2
    return merge_sorted_arrays(merge_sort(arr[:mid]), merge_sort(arr[mid:]))


# ----------------------------------------------------------------------------
# MAIN

def main():
    """ The main brain """

    filename = "./rosalind_ms.txt"

    with open(filename, "r") as f:
        size = int(f.readline())
        unsorted = list(map(int, f.readline().split(" ")))

    sorto = merge_sort(unsorted)
    print(*[item for item in sorto], end = " ")



if __name__ == "__main__":
    main()

#!/usr/bin/env python3

"""
title: Enumerating Gene Orders
author: Colin Phoebe
date: 2025-06-14
description: Compute the number of permutations of length n, and list all
    those permutations. I utilize Heap's Algorithm.
"""

from typing import Generator
import math


def heap_permutation(arr: list, size: int) -> Generator[list, None, None]:
    """ Generate all unique permutations for a sequence of integers 1 to n """

    if size == 1:
        yield arr.copy()
        return

    # keep swapping items of the original sequence.
    # each swapped version will end up having size == 1 eventually, and will
    #   be yielded
    for i in range(size):
        yield from heap_permutation(arr, size - 1)

        if size % 2 == 1:
            arr[0], arr[size - 1] = arr[size - 1], arr[0]
        else:
            arr[i], arr[size - 1] = arr[size - 1], arr[i]

def main():

    filename = "./params.txt"
    with open(filename, "r") as f:
        n = int(f.read())

    arr = [i for i in range(1, n + 1)]
    perms = heap_permutation(arr, n)
    print(math.factorial(n))
    for p in perms:
        print(" ".join([str(p[i]) for i in range(len(p))]))


if __name__ == "__main__":
    main()

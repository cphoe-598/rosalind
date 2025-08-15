#!/usr/bin/env python3

"""
title: 2sum
author: Colin Phoebe
date: 2025-07-26
"""

def find_2sum(arr) -> tuple:
    """ idk """

    d = dict()
    for i, val in enumerate(arr):
        if (-val in d) and (d[-val] != i):
            return (d[-val]+1, i+1)
        d[val] = i
    return [-1]


def main() -> None:
    """ The main brain """

    with open("./rosalind_2sum.txt", "r") as f:
        k, n = f.readline().split(" ")
        arrs = [list(map(int, line.split(" "))) for line in f]

    res = [find_2sum(arr) for arr in arrs]
    for r in res:
        print(*r)


if __name__ == "__main__":
    main()

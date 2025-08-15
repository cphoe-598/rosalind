#!/usr/bin/env python3

"""
title: 2-Way Partition
author: Colin Phoebe
date: 2025-06-21
description: Algorithm for 2-way partition of array |
    You keep track of three variables, INDEX (current position as you move across the array), POSITION (will stick at the position of the first largest item until that item is swapped with a smaller item from the right), and APERTURE (the value of the first item in the array).
    The algorithm moves across the list, incrementing INDEX. It compares the item at INDEX to the APERTURE. If greater than APERTURE, then INDEX is incremented, and POSITION stays at its current position. If, however, the item at INDEX is less than or equal to APERTURE, it is swapped with the item in front of POSITION, and POSITION is incremented.
    Finally, the first item in the array is swapped with the item at position POSITION.
    ---
    See a visual of what the algorithm does at the end of this script.
    ---
    I stole the linear-time solution from the Rosalind.info explanation page.
"""

# ----------------------------------------------------------------------------
# FUNCTION
def two_way_partition(arr):
    """ 2-Way Partition """
    arr = arr.copy()

    idx, pos, apt = -1, -1, arr[0]
    while idx < len(arr) - 1:
        idx += 1
        if arr[idx] <= apt:
            arr[idx], arr[pos + 1] = arr[pos + 1], arr[idx]
            pos += 1
    arr[0], arr[pos] = arr[pos], arr[0]

    return arr


# ----------------------------------------------------------------------------
# MAIN
def main():
    """ The main brain """

    filename = "rosalind_par.txt"
    with open(filename, "r") as f:
        arr = list(map(int, f.readlines()[1].split(" ")))
    print(" ".join(list(map(str, two_way_partition(arr)))))


if __name__ == "__main__":
    main()


"""
Showing what has happened at the end of each step ...

# idx: -1, pos: -1, apt: 7
7 9 2 5 8 4

# idx: 0, pos: 0, apt: 7
7 9 2 5 8 4

# idx: 1, pos: 0, apt: 7
7 9 2 5 8 4

# idx: 2, pos: 1, apt: 7
7 2 9 5 8 4

# idx: 3, pos: 2, apt: 7
7 2 5 9 8 4

# idx: 4, pos: 2, apt: 7
7 2 5 9 8 4

# idx: 5, pos: 3, apt: 7
7 2 5 4 8 9

# idx: 6, pos: 3, apt: 7
4 2 5 7 8 9

DONE
"""

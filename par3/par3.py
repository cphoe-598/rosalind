#!/usr/bin/env python3

"""
title: 3-Way Partition
author: Colin Phoebe
date: 2025-06-23
description: Algorithm creating a 3-way partition of a collection. The first
    item in the collection is the pivot. Using that, the three partitions
    of the final collection are as follows: P1 <= P2+pivot < P3, such that all
    the items in the second partition are equal to the pivot.
"""

def three_way_partition(arr):
    """ 3-Way Partition """

    arr = arr.copy()

    idx, pos, apt, dups = -1, -1, arr[0], 0
    while idx < len(arr) - 1:
        idx += 1
        
        # if find duplicate of pivot
        if arr[idx] == apt:
            pos += 1
            arr = [arr.pop(idx)] + arr
            dups += 1

        # if find item smaller than pivot
        elif arr[idx] < apt:
            pos += 1
            arr[idx], arr[pos] = arr[pos], arr[idx]
        
        # step-by-step for debugging
        # print(f"idx:{idx}, pos:{pos}, apt:{apt}, dups:{dups}\n{arr}\n")

    arr = [arr[pos]] + arr[dups:pos] + arr[:dups] + arr[pos+1:]
    return arr


def main():
    """ The main brain """

    # arr = [4, 5, 6, 4, 1, 2, 5, 7, 4]
    filename = "rosalind_par3.txt"
    with open(filename, "r") as f:
        arr = list(map(int, f.readlines()[1].split(" ")))
    print(" ".join(list(map(str, three_way_partition(arr)))))

    

if __name__ == "__main__":
    main()

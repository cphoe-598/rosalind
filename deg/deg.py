#!/usr/bin/env python3

"""
title: Degree Array
author: Colin Phoebe
date: 2025-06-27
description: ...
"""

from collections import defaultdict
from itertools import islice


# ----------------------------------------------------------------------------
# FUNCTIONS

def net_from_file(filename: str) -> defaultdict:
    """
    Read file containing rows representing network edges.
    Return dictionary of edges. Example:
        { a : [b, c],
          b : [a],
          c : [a] }
    """

    net = defaultdict(set)
    with open(filename, "r") as f:
        for line in islice(f, 1, None):  # start from second line
            try:
                start, end = map(int, line.split())
                net[start].add(end)
                net[end].add(start)
            except ValueError:
                break

    return net


def node_degrees(net: dict) -> list:
    """
    Return (ordered, alphanumeric) node degrees
    for a network created by net_from_file().
    """

    return [len(net[key]) for key in sorted(net)]


# ----------------------------------------------------------------------------
# MAIN

def main():
    """ The main brain """

    filename = "rosalind_deg.txt"
    # filename = "random_net.txt"

    """ 
    SIMPLER, FASTER APPROACH
    Only need to count how many times each node appears in the edge list
    
    from collections import Counter
    counts = Counter(open(filename).read().split()[2:])
    for i in range(len(counts)):
        print(counts[str(i+1)], end = " "),
    """
    
    net = net_from_file(filename)
    deg = node_degrees(net)
    # print(sorted(net))
    print(" ".join(map(str, deg)))


if __name__ == "__main__":
    main()

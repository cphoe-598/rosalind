#!/usr/bin/env python3

"""
title: Double-Degree Array
author: Colin Phoebe
date: 2025-06-28
description: ...
"""

from collections import defaultdict
from itertools import islice


# ----------------------------------------------------------------------------
# FUNCTIONS

def network_from_file(filename: str) -> defaultdict:
    """ Return network from file containing edge list """

    with open(filename, "r") as f:
        size = int(f.readline().split(" ")[0])
        
        edges = defaultdict(list)
        for line in islice(f, 0, None):
            try:
                start, end = map(int, line.split(" "))
                edges[start].append(end)
                edges[end].append(start)
            except ValueError:
                break

        return edges, size


def sum_of_neighbor_degs(net: defaultdict, size: int) -> defaultdict:
    """ Return, for each node, the sum of the degrees of its neighbors """

    # will decrement with each item counted
    singletons = size

    ddegs = defaultdict(int)
    for node, neighbors in sorted(net.items()):
        ddegs[node] += sum([len(net[neigh]) for neigh in neighbors])
        singletons -= 1

    # add empty values for singletons
    for i in range(singletons):
        ddegs[hash(i)] = 0

    return ddegs


# ----------------------------------------------------------------------------
# MAIN

def main():
    """ The main brain """

    filename = "rosalind_ddeg.txt"
    net, size = network_from_file(filename)
    ddeg = sum_of_neighbor_degs(net, size)

    # print(net)
    # print(ddeg)

    ddeg_out = " ".join([str(ddeg[i]) for i in ddeg])
    print(ddeg_out)


if __name__ == "__main__":
    main()



#!/usr/bin/env python3

"""
title: DNA String Overlap Graph
author: Colin Phoebe
date: 2024-12-10
"""

import argparse
import sys
from typing import NamedTuple, TextIO
from collections import defaultdict
from Bio import SeqIO


# -----------------------------------
# Command line stuff

class Args(NamedTuple):
    """ Command Line Arguments """

    file: TextIO


def get_args() -> Args:
    """ Parse Command Line Args """

    parser = argparse.ArgumentParser(
            description = "DNA String Overlap Graph From FASTA",
            formatter_class = argparse.ArgumentDefaultsHelpFormatter
    )

    parser.add_argument(
            "file",
            metavar = "FILE",
            type = argparse.FileType("rt"),
            nargs = "?",
            default = sys.stdin,
            help = "Input FASTA file"
    )

    args = parser.parse_args()

    return Args(args.file)


# -----------------------------------
# Functions

def overlap_graph_edges(file: TextIO) -> defaultdict:
    """
    Get adjacency list of sequences.

    In this case, an adjacency is defined as a sequence's suffix (last 3)
        matching the prefix (first 3) of another sequence.
    """

    records = list(SeqIO.parse(file, 'fasta'))

    # map unique prefixes to seqs from FASTA file
    unique_prefixes = defaultdict(list)
    for record in records:
        unique_prefixes[str(record.seq)[:3]].append(record.id)

    # match seq suffixes to prefixes
    edges = defaultdict(list)
    for record in records:
        prefix = record.seq[-3:]
        if prefix in unique_prefixes:
            edges[record.id] = unique_prefixes[prefix]
            # remove self links
            if record.id in edges[record.id]:
                edges[record.id].remove(str(record.id))

    return edges


# -----------------------------------
# MAIN

def main() -> None:
    """ The main brain """

    args = get_args()

    # get edges, print
    edges = overlap_graph_edges(args.file)
    for from_node, to_nodes in edges.items():
        for to_node in to_nodes:
            print(from_node, to_node)


if __name__ == "__main__":
    main()

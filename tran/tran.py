#!/usr/bin/env python3

"""
title: Transitions/Transversions Ratio
author: Colin Phoebe
date: 2025-06-14
description: Transitions/Transversions Ratio
"""

from Bio.SeqIO.FastaIO import SimpleFastaParser


# ----------------------------------------------------------------------------
# FUNCTIONS

def transitions_transversions(s1, s2):
    """
    Computes the ratio of transitions:transversions
    for two DNA strings of equal length
    """

    transitions = {"A":"G", "G":"A", "T":"C", "C":"T"}
    mutations = [transitions[b1] == b2 for b1, b2 in zip(s1, s2) if b1 != b2]
    return sum(mutations) / (len(mutations) - sum(mutations))


# ----------------------------------------------------------------------------
# MAIN

def main():
    """ The main brain """

    with open("./seqs.fa") as handle:
        s1, s2 = tuple([seq for (name, seq) in SimpleFastaParser(handle)])

    tt = transitions_transversions(s1, s2)
    print(tt)


if __name__ == "__main__":
    main()

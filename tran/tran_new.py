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

def transitionTransversionRatio(s1, s2):
    trans = {"A":"G", "G":"A", "T":"C", "C":"T"}
    mut = [0 if trans[b1] == b2 else 1 for b1, b2 in zip(s1, s2) if b1 is not b2]
    return mut.count(0) / float(mut.count(1))


# ----------------------------------------------------------------------------
# MAIN

def main():
    """ The main brain """

    with open("./seqs.fa") as handle:
        s1, s2 = tuple([seq for (name, seq) in SimpleFastaParser(handle)])

    tt = transitionTransversionRatio(s1, s2)
    print(tt)


if __name__ == "__main__":
    main()

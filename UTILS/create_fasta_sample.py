#! /usr/bin/env python3

"""
title: create_fasta_sample.py
author: Colin Phoebe
date: 2025-01-26
description:
    This module will write a file with a large sample of randomly generated
    FASTA sequence IDs/records. This is useful for benchmarking that requires
    FASTA input using tools like Hyperfine.
"""

import random


# -----------------------
# FUNCTIONS

def random_dna() -> str:
    """ Generate a random DNA sequence """

    return "".join(random.choices("ACGT", k = 1000))


# -----------------------
# MAIN
def main() -> None:
    """ Generate 1000 FASTA records with randomized ID and sequence """

    with open("seqs.fa", "w") as out:
        for i in range(1):
            record = f">seq_{i}\n{random_dna()}\n"
            out.write(record)


if __name__ == "__main__":
    main()

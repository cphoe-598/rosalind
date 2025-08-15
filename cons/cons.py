#!/usr/bin/env python3

"""
title: Consensus and Profile
author: Colin Phoebe
date: 2024-12-06
"""

import argparse
from typing import NamedTuple, TextIO
import sys
from Bio import SeqIO
import numpy as np


# -----------------------------------
# Handle command-line input


class Args(NamedTuple):
    """Command-line arguments"""

    file: TextIO


def get_args() -> Args:
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Consensus String And Profile Matrix",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "file",
        metavar="FILE",
        type=argparse.FileType("rt"),
        nargs="?",
        default=sys.stdin,
        help="Input FASTA file",
    )

    args = parser.parse_args()

    return Args(file=args.file)


# -----------------------------------
# Functions


def sequence_matrix_from_fasta(file: TextIO) -> np.ndarray:
    """Matrix of sequences from FASTA file"""

    seqs = [list(str(rec.seq)) for rec in SeqIO.parse(file, "fasta")]
    return np.array(seqs, dtype=str)


def profile_matrix(matrix: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """
    Profile matrix of a matrix of values (likely nucleotide base pairs).
    """

    # get unique characters and their counts; and the FASTA file "dimensions"
    unique_chars = np.unique(matrix.flatten())
    num_chars = len(unique_chars)
    num_positions = len(matrix[0])

    # create empty profile matrix
    prof_mtx = np.zeros((num_chars, num_positions), dtype=np.int64)

    # sum up counts of each character, building up profile matrix
    for i, char in enumerate(unique_chars):
        prof_mtx[i] = np.sum(matrix == char, axis=0)

    return prof_mtx, unique_chars


def consensus_string(matrix: np.ndarray) -> str:
    """
    Consensus string from a profile matrix, and a list of characters
    corresponding to the rows of the profile matrix
    """

    prof_mtx, chars = profile_matrix(matrix)
    return "".join([chars[max_idx] for max_idx in list(np.argmax(prof_mtx.T, axis=1))])


# -----------------------------------
# MAIN


def main() -> None:
    """The main brain"""

    args = get_args()

    # (1) matrix of sequences from FASTA file
    # (2) profile matrix of sequences, and unique chars corresponding to rows
    # (3) consensus string
    seq_mtx = sequence_matrix_from_fasta(args.file)
    prof_mtx, bases = profile_matrix(seq_mtx)
    cons_str = consensus_string(seq_mtx)

    # print consensus string
    print(cons_str)

    # print sequences
    for base, prof in zip(bases, prof_mtx):
        print(f"{base}: {' '.join(map(str, prof))}")


if __name__ == "__main__":
    main()

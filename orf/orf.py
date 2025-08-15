#!/usr/bin/env python3

"""
title: Open Reading Frames
author: Colin Phoebe
date: 2025-05-06
description:
    Given: A DNA string, s, of length at most 1 kbp in FASTA format.
    Return: Every distinct candidate protein string that can be translated from ORFs of s.
"""

from Bio import SeqIO

codon_to_aa = {
        'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
        'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
        'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
        'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',                 
        'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
        'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
        'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
        'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
        'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
        'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
        'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
        'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
        'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
        'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
        'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
        'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W',
}

def translate_dna(dna: str) -> str:
    """ Translate DNA to amino acid sequence """

    aa = ""
    for i in range(0, len(dna) - 2, 3):
        codon = dna[i:i+3]
        aa += codon_to_aa.get(codon, '?')
    return aa

def dna_revc(dna: str) -> str:
    """ Returns the reverse complement of a DNA string """

    comps = { "A":"T", "T":"A", "G":"C", "C":"G" }
    return "".join([comps[n] for n in dna])[::-1]


def orf_coords(dna: str) -> list[tuple]:
    """ Returns coordinates of open reading frames (ORFs) in DNA string """

    stop_codons = {"TAA", "TAG", "TGA"}
    orfs = []  # completed ORFs
    active_orfs = []  # starting positions of ORFs being built
    i = 0
    while i <= (len(dna) - 1):
        codon = dna[i:i+3]

        # if START, add new item to active_orfs, skip to next nucleotide after START
        if codon == "ATG":
            active_orfs.append(i)

        # if STOP, pop now completed ORF(S) from active_orfs to ORF list; skip to next nucleotide after STOP
        elif codon in stop_codons:
            completed = []
            for start in active_orfs:
                if (i - start) % 3 == 0:
                    orfs.append((start, i))  # exclude STOP from completed ORF
                    completed.append(start)
            active_orfs = [s for s in active_orfs if s not in completed]

        i += 1

    return orfs


def find_orfs(dna: str) -> list[str]:
    """ Returns translated open reading frames (ORFs) in DNA string """

    revc = dna_revc(dna)

    coords_dna = orf_coords(dna)
    coords_revc = orf_coords(revc)
    orfs_dna = set([ translate_dna(dna[c[0]:c[1] + 1]) for c in coords_dna ])
    orfs_revc = set([ translate_dna(revc[c[0]:c[1] + 1]) for c in coords_revc ])
    return orfs_dna.union(orfs_revc)


def main() -> None:
    """ The main brain """

    filename = "sample.fna"
    records = SeqIO.parse(filename, "fasta")
    for rec in records:
        orfs = find_orfs(str(rec.seq))
        for orf in orfs:
            print(orf)

if __name__ == "__main__":
    main()

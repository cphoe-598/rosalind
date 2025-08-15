#!/usr/bin/env python3

"""
title: RNA Splicing
author: Colin Phoebe
description: DNA -> RNA, introns spliced out
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
        'TAC':'Y', 'TAT':'Y', 'TAA':'*', 'TAG':'*',
        'TGC':'C', 'TGT':'C', 'TGA':'*', 'TGG':'W',
}


# ----------------------------------------------------------------------------
# FUNCTIONS

def transcribe_spliced(gene: str, introns: list[str]) -> str:
    """ DNA -> RNA, introns spliced out """

    # find ranges of introns in gene
    intron_starts = dict(zip(introns, [gene.find(intron) for intron in introns]))
    intron_ranges = [range(s, s + len(i)) for i, s in intron_starts.items()]

    # exclude ranges from gene
    r = set(range(len(gene)))  # set of all indices in gene
    for rng in intron_ranges:
        r -= set(rng)

    spliced_rna = "".join(exon for i, exon in enumerate(gene) if i in r)

    return spliced_rna


def translate(rna: str) -> str:
    """ Translate RNA to amino acid sequence """

    # automatically add M; translate subsequent codons; don't bother with STOP
    prot = "M" + "".join([codon_to_aa[rna[i:i+3]] for i in range(3, len(rna) - 5, 3)])

    return prot


# ----------------------------------------------------------------------------
# MAIN

def main():
    """ The main brain """

    # read FASTA file; extract sequences
    filename = "./seqs.fa"
    records = SeqIO.parse(filename, "fasta")
    seqs = [str(rec.seq) for rec in records]
    
    # get the gene (first seq) and introns (the rest)
    gene = seqs[0]
    introns = seqs[1:]

    # splice; translate; print
    spliced_rna = transcribe_spliced(gene, introns)
    prot = translate(spliced_rna)
    print(prot)


if __name__ == "__main__":
    main()

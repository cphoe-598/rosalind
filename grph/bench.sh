#!/usr/bin/env bash

# Benchmark grph.py

PRG="./grph.py"
SAMPLE="./seqs.fa"
hyperfine -i --warmup 10 "$PRG $SAMPLE"

#!/usr/bin/env bash

# Benchmark mrna.py

PRG="./mrna.py"
SAMPLE="./seqs.fa"
hyperfine -i --warmup 10 "$PRG $SAMPLE"

#!/usr/bin/env bash

# Benchmark fibd.py

PRG="./fibd.py"
SAMPLE="./seqs.fa"
hyperfine -i --warmup 10 "$PRG $SAMPLE"

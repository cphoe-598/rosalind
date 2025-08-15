#!/usr/bin/env bash

# Benchmark iev.py

PRG="./iev.py"
SAMPLE="./seqs.fa"
hyperfine -i --warmup 10 "$PRG $SAMPLE"

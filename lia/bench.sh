#!/usr/bin/env bash

# Benchmark lia.py

PRG="./lia.py"
SAMPLE="./seqs.fa"
hyperfine -i --warmup 10 "$PRG $SAMPLE"

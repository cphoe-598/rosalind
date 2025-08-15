#!/usr/bin/env bash

# Benchmark cons.py

PRG="./cons.py"
SAMPLE="./seqs.fa"
hyperfine -i --warmup 10 "$PRG $SAMPLE"

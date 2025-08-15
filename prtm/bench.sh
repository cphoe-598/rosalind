#!/usr/bin/env bash

# Benchmark prtm.py

PRG="./prtm.py"
SAMPLE="./seqs.fa"
hyperfine -i --warmup 10 "$PRG $SAMPLE"

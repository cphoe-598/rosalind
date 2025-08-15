#!/usr/bin/env bash

# Benchmark cons.py

PRG="./prob.py"
SAMPLE="./rosalind_prob.txt"
hyperfine -i --warmup 10 "$PRG"

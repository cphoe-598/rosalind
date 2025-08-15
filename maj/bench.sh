#!/usr/bin/env bash

# Benchmark cons.py

PRG1="./maj.py"
PRG2="./moores_voting_algorithm.py"
hyperfine -i --warmup 10 "$PRG1" "$PRG2"

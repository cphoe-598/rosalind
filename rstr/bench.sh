#!/usr/bin/env bash

# Benchmark cons.py

PRG="./rstr.py"
hyperfine -i --warmup 10 "$PRG"

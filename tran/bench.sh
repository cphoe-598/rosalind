#!/bin/bash

hyperfine -i --warmup 10 ./tran.py ./tran_new.py

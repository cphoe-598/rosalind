#!/bin/bash

pyinstrument -r html -o profile_tran.html tran.py
pyinstrument -r html -o profile_tran_new.html tran_new.py

mv profile_tran*.html /mnt/c/Users/colin/Downloads/
wslview /mnt/c/Users/colin/Downloads/

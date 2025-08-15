"""
title: Tests for cons.py
author: Colin Phoebe
date: 2025-01-26
"""

import os
import platform
import random
import string
import re
from subprocess import getstatusoutput


PRG = "./cons.py"
RUN = f"python {PRG}" if platform.system() == "Windows" else PRG
SAMPLE1 = "./tests/inputs/small_input.fa"


# ----------------------------------------
def test_exists() -> None:
    """ Program exists """

    assert os.path.isfile(PRG)


# ----------------------------------------
def test_usage() -> None:
    """ Usage """

    for flag in ['-h', '--help']:
        rv, out = getstatusoutput(f"{RUN} {flag}")
        assert rv == 0
        assert out.lower().startswith("usage:")


# ----------------------------------------
def test_bad_input() -> None:
    """ Fails on bad input """

    bad = random_string()
    rv, out = getstatusoutput(f"{RUN} {bad}")
    assert rv != 0
    assert out.lower().startswith("usage:")
    assert re.search(f"No such file or directory: '{bad}'", out)


# ----------------------------------------
def test_good_input() -> None:
    """ Works on good input """

    rv, out = getstatusoutput(f"{RUN} {SAMPLE1}")
    assert rv == 0
    expected_output = """ATGCAACT
A: 5 1 0 0 5 5 0 0
C: 0 0 1 4 2 0 6 1
G: 1 1 6 3 0 1 0 0
T: 1 5 0 0 0 1 1 6"""
    assert out.strip() == expected_output

# ----------------------------------------
def test_stdin() -> None:
    """ Works on STDIN """

    rv, out = getstatusoutput(f"cat {SAMPLE1} | {RUN}")
    assert rv == 0
    expected_output ="""ATGCAACT
A: 5 1 0 0 5 5 0 0
C: 0 0 1 4 2 0 6 1
G: 1 1 6 3 0 1 0 0
T: 1 5 0 0 0 1 1 6"""
    assert out.strip() == expected_output


# ----------------------------------------
def random_string() -> str:
    """ Generate a random string """

    k = random.randint(5, 10)
    return "".join(random.choices(string.ascii_letters + string.digits, k = k))

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


PRG = "./grph.py"
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
    expected_output = """Rosalind_0498 Rosalind_2391
Rosalind_0498 Rosalind_0442
Rosalind_2391 Rosalind_2323"""
    assert out.strip() == expected_output

# ----------------------------------------
def test_stdin() -> None:
    """ Works on STDIN """

    rv, out = getstatusoutput(f"cat {SAMPLE1} | {RUN}")
    assert rv == 0
    expected_output = """Rosalind_0498 Rosalind_2391
Rosalind_0498 Rosalind_0442
Rosalind_2391 Rosalind_2323"""
    assert out.strip() == expected_output


# ----------------------------------------
def random_string() -> str:
    """ Generate a random string """

    k = random.randint(5, 10)
    return "".join(random.choices(string.ascii_letters + string.digits, k = k))

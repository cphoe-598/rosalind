.PHONY: test bench clean

# default target
all: test bench

# PyTest (PyLint and MyPy) in virtual environment
test:
	./venv/bin/python3 -m pytest -xv --disable-pytest-warnings --pylint --mypy fibd.py tests/fibd_test.py

# (for benchmarking) create large sample FASTA file
seqs.fa:
	python3 create_fasta_sample.py

# benchmark in virtual environment
bench: seqs.fa
	./bench.sh

# remove generated files
clean:
	rm -f seqs.fa
	find . -type d -name "__pycache__" -exec rm -rv {} +

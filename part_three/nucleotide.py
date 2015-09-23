#! /usr/bin/env python3

# Nucleotide Counter
#
# Given a sequence consisting only of the characters 'A', 'C', 'T', and 'G',
# return a count of how frequently each one occurs.
#

import sys


def count(sequence):
    totals = {'A': 0, 'C': 0, 'T': 0, 'G': 0}

    for nucleotide in sequence:
        nucleotide = nucleotide.upper()  # normalise the value before using it
        totals[nucleotide] += 1

    return totals


# Entry point for invocation as a script, expects one command line argument
if __name__ == "__main__":
    sequence = sys.argv[1]
    totals = count(sequence)

    for nucleotide, count in totals.items():
        print("{0} total is {1}".format(nucleotide, count))

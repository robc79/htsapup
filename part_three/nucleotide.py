#! /usr/bin/env python3

# Nucleotide Counter
#
# Given a sequence consisting only of the characters 'A', 'C', 'T', and 'G',
# return a count of how frequently each one occurs.
#

import sys


def parse_sequence_argument(args):
    if len(args) < 2:
        raise ValueError("Argument missing")

    return args[1]


def count(sequence):
    totals = {'A': 0, 'C': 0, 'T': 0, 'G': 0}

    for nucleotide in sequence:
        nucleotide = nucleotide.upper()  # normalise the value before using it
        totals[nucleotide] += 1

    return totals


def show_totals(totals, out):
    for nucleotide, count in totals.items():
        print("{0} total is {1}".format(nucleotide, count), file=out)


# Entry point for invocation as a script, expects one command line argument
if __name__ == "__main__":
    sequence = parse_sequence_argument(sys.argv)
    totals = count(sequence)
    show_totals(totals, sys.stdout)

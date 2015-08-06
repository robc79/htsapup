# Complete solution

sequence = "ATGTTCA"
totals = {'A': 0, 'C': 0, 'T': 0, 'G': 0}

for nucleotide in sequence:
    totals[nucleotide] += 1

for nucleotide, count in totals.items():
    print("{0} total is {1}".format(nucleotide, count))

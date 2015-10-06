#!/usr/bin/env python

# Command line script to calculate base frequency from a .fasta file

import sys
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("fasta_file")
args = parser.parse_args()

###########################################################

fasta = args.fasta_file

a_count = 0
c_count = 0
g_count = 0
t_count = 0

with open(fasta, 'r') as fasta:
    for line in fasta:
        if line.startswith(">"):
            # Header line, skip it
            continue
        for base in line.strip():
            if base == "A":
                a_count += 1
            elif base == "C":
                c_count += 1
            elif base == "G":
                g_count += 1
            elif base == "T":
                t_count += 1

total = a_count + c_count + g_count + t_count

print("Base counts for file %s:" % fasta)
print("A: %d\t%d%%" % (a_count, a_count*100.0/total))
print("C: %d\t%d%%" % (c_count, c_count*100.0/total))
print("G: %d\t%d%%" % (g_count, g_count*100.0/total))
print("T: %d\t%d%%" % (t_count, t_count*100.0/total))

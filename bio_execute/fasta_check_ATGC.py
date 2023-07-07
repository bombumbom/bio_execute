#!/usr/bin/env python3
# Reverse sequences
from Bio import SeqIO
import argparse

parser = argparse.ArgumentParser(description='fasta file reverse sequence')

parser.add_argument('-f', required=True, help='File name')
args = parser.parse_args()

file = args.f
filename = file.split('/')[-1]
filename = filename.split('.fasta')
filename = filename[0]

record = SeqIO.read(file,"fasta")

seq = record.seq

count = 0
for i, s in enumerate(seq):
    if str(s) not in 'ATGC':
        print(i, s)
        count += 1
print('이상한 시퀀스 : %s' % count)
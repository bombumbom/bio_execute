#!/usr/bin/env python3
# reverse genbank
from Bio import SeqIO
import argparse

parser = argparse.ArgumentParser(description='fasta file reverse sequence')

parser.add_argument('-f', required=True, help='File name')
parser.add_argument('-p', required=False, default='./',help='Path')
args = parser.parse_args()
if args.p[-1] != '/':
    args.p = args.p + "/"
print("file or number : %s \n save path : %s" % (args.f, args.p))
file = args.f
filename = file.split('/')[-1]
filename = filename.split('.gb')
filename = filename[0]

record = SeqIO.read(file, "genbank")

rc = record.reverse_complement(id="rev_"+record.id, description = "reverse complement", annotations=record.annotations)

SeqIO.write(rc,args.p+filename+'_rev.gb',"genbank")

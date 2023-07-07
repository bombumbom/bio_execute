#!/usr/bin/env python3
# Reverse sequences
from Bio import SeqIO
from Bio.Seq import Seq
import argparse

parser = argparse.ArgumentParser(description="fasta file reverse sequence")

parser.add_argument("-f", required=True, help="File name")
parser.add_argument("-p", required=False, default="./", help="Path")
args = parser.parse_args()
if args.p[-1] != "/":
    args.p = args.p + "/"
print("file or number : %s \n save path : %s" % (args.f, args.p))
file = args.f
filename = file.split("/")[-1]
filename = filename.split(".fasta")
filename = filename[0]

record = SeqIO.read(file, "fasta")

rev_rec = record.seq.reverse_complement()

# seq = Seq("ACCGAGACGGCAAAGGCTAGCATAGGTATGAGACTTCCTTCCTGCCAGTGCTGAGGAACTGGGAGCCTAC")
# feature = SeqFeature(FeatureLocation(5, 18), type="gene", strand=-1)
# feature_seq0 = seq[feature.location.start:feature.location.end]

# feature_seq = seq[feature.location.start:feature.location.end].reverse_complement()
f = open(args.p + filename + "_rev.fasta", "w")
f.write(">%s\n" % record.id)
f.write(str(rev_rec))
f.close()

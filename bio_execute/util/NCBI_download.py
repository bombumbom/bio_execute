#!/usr/bin/env python3
from Bio import Entrez
import argparse

Entrez.email = "sacrificek2b@gmail.com"

parser = argparse.ArgumentParser(description='NCBI Download')
parser.add_argument('-a', required=True, help='Access Number or List file')
parser.add_argument('-t', required=False, default='fasta',help='File Type')
parser.add_argument('-p', required=False, default='./',help='')

args = parser.parse_args()


if args.p[-1] != '/':
    args.p = args.p + "/"
print("file or number : %s \n type : %s \n save path : %s" % (args.a, args.t, args.p))

if args.t == "gbk" or args.t == "genbank":
    args.t = "gb"

try:
    f = open(args.a, 'r')
    lines = f.readlines()
    f.close()
    for id0 in lines:
        id = id0.strip()
        handle = Entrez.efetch(db="nucleotide", id=id, rettype=args.t, retmode="text")
        filename = args.p+"%s.%s" % (id, args.t)
        print(id)
        out_handle = open(filename, "w")
        record = handle.read()
        out_handle.write(record)
        out_handle.close()
        handle.close()
except FileNotFoundError:
    handle = Entrez.efetch(db="nucleotide", id=args.a, rettype=args.t, retmode="text")
    filename = args.p+"%s.%s" % (args.a, args.t)
    print(args.a)
    out_handle = open(filename, "w")
    record = handle.read()
    out_handle.write(record)
    out_handle.close()
    handle.close()

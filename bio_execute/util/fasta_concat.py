#!/usr/bin/env python3
#* fasta파일 한줄로 합치기
import argparse

parser = argparse.ArgumentParser(description='fasta file concat')

parser.add_argument('-f', required=True, help='File name')
parser.add_argument('-p', required=False, default='./',help='Path')

args = parser.parse_args()

if args.p[-1] != '/':
    args.p = args.p + "/"
print("file or number : %s \n save path : %s" % (args.f, args.p))


path = args.f

filename = path.split('/')[-1]
filename = filename.split('.fasta')
filename = filename[0]

fr = open(path,'r')

lines = fr.readlines()

head = []
seq = []
seq1 = ''
for i, line in enumerate(lines):
    line1 = []
    if line[0] == '>':
        head.append(line)
        if i != 0:
            seq.append(seq1)
        seq1 = ''
    else:
        seq1 += line.strip()
seq.append(seq1)

fw = open(args.p+filename+'_edit.fasta','w')

for h,s in zip(head,seq):
    fw.write(h)
    fw.write(s+'\n')
fw.close()


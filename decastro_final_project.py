#! /usr/bin/env python3

import argparse
from Bio import SeqIO
from Bio.Blast import NCBIWWW
import sys

pspAseq='pspAseq.txt'
gene_name='Streptococcus pneumoniae pneumococcal surface protein A'
genome=open("pspA.fasta","w+")

genome.write('>'+gene_name+('\n'))

#def get_args():
	# create an argument parser object
	#parser = argparse.ArgumentParser(description = 'Parses a txt file')

	# add positional argument for the input position in the Fibonacci sequence
	#parser.add_argument("pspAseq.txt", help="txt-formatted file")

	# parse the arguments
	#return parser.parse_args()

#def parse_fasta():
	#genome_object = SeqIO.read(args.pspAseq.txt, 'fasta')
	#return genome_object.seq()
    

#create fasta file

with open(pspAseq, 'r') as pspA:
    next(pspA)
    #print('>'+gene_name)

    for line in pspA:
        #remove line breaks
        line = line.rstrip('\n')
        line=line.replace(' ', '')
        pspA_clean=line.upper()
        #print(pspA_clean)
        genome.write(pspA_clean)
genome.close()
        #sys.stdout.write(pspA_clean)
        #sys.stdout.close()


#def pspa_fasta(pspA_clean):
    #pspA_seq = SeqIO.read(pspA_clean, 'fasta')
   # SeqIO.write(pspA_seq, "pspA.fasta", "fasta")
   # print(pspA_seq)
   # return pspA_seq()
    

#blast pspA
#record = SeqIO.read("m_cold.fasta", format="fasta")
#result_handle = NCBIWWW.qblast("blastn", "nt", record.seq)
fasta_string = open("pspA.fasta").read()
result_handle = NCBIWWW.qblast("blastn", "nt", fasta_string)

#read results
with open("my_blast.xml", "w") as out_handle:
    out_handle.write(result_handle.read())
    result_handle.close()


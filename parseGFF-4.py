#! usr/bin/env python3

import argparse
import csv
import re
from Bio import SeqIO
from collections import defaultdict

def get_args():
    #create an argument parser object
    parser=argparse.ArgumentParser(description='parses a GFF file')


    # add positional argument for the input position in the Fibonacci sequence
	parser.add_argument("parse_gff", help="")
    parser.add_arguments("parse_fasta", help="")

    # parse the arguments
	return parser.parse_args()

def 

def parse_fasta():
    genome_object= SeqIO.read(args.fasta_file, 'fasta')
    return genome_object.seq

def parse_gff(genome):
    #dictionary to hold CDS sequence key= genome name, value = dictionary #2 where key =exon number, value=the sequence
    coding_seqs=defaultdict(dict)
    #open and read and parse GFF files
    with open (args.gff_file, 'r') as gff:
        #create a cvs reader object
        reader = csv.reader(gff, delimiter='\t')

        for line in reader:

            #skip blank lines
            if not line:
                continue
            #skip commented lines
            elif re.match("^#", line):
                continue
            #this is data line
            else:
                #extract the star and end coordinates for tgis feature
                #remember python counts from zero and last value not inclusive. But csv starts from 1
                begin=int(line[3]-1)
                end=int(line[4])
                strand=line[6]
                feature_type = line[2] #cds exons etc
                attributes = line[8]
                species = line[0]

                #extract seq for this feature
                feature_sequence=genome[begin:end]

                #reverse complement the sequence if necessary. If strand is a - then you need reverse complement
                if (strand=='-'):
                   feature_sequence = rev_comp(feature_sequence)
               # print(len(feature_sequence), line[5])
               #calculate the GC content of feature
               gc_content=gc(feature_sequence)

               if (feature_type == 'CDS'):
                   #split the attribute field into its separate parts, to get the gene info
                   exon_info = attributes.split(' ; ') #split everything into a list and to call the part we need, we call the list zero

                   
                   #extract the exon number
                   exon_number=exon_info[0].split()[-1] #-1 means grab the last element
                   #test whether there is or there isnt an entry in index2 which holds the value 'exon' for genes that have introns. If there is no value in index 2 then the gene does not hvae an intron, and we can just print it.
                   if len(exon_info[0].split())>2:
                       #extract the gene name
                       gene_name = exon_info[0].split()[1] #defaut for split is white space ()
                       if gene_name in coding_seqs:
                           #store coding seq for this exon
                           coding_seqs[gene_name][exon_number]=feature_sequence
                    
                       else:
                           #first time encountering this gene, so declare the dictionary for it.
                           coding_seqs[gene_name]={}
                           #store the coding sequence for this exon
                           coding_seqs[gene_name][exon_number]=feature_sequence
                   else:                        
                       #print the sequence in FASTA format
                       print('>'+ line[0].replace(' ','_') + '_' + gene_name)
                       print(feature_sequence)
                       
    #done reading the GFF file, loop over coding_Seqs to print the CDS sequence
    #gene=gene names, exons= dictinoary of exon sequences, key=exon_num, value=exon_seq)
    for gene, exons in coding_seqs.items():
        #we are looping over a dictionary where they key is exon number that's why we use .items
        #loop over all the exons for this particular gene
        #IMPORTANT need to sort the exons first. Sort the dictionary by its keys
        #make a variable htat will hold the concatinated cds sequence
        cds_for_this_gene='' # it euqals nothing its a string
        #print the FASTA header for this gene
        print('>'+line[0].replace(' ', '_')+ '_' +gene)
        for exon_num, exon_seq in sorted(exons.items()):
            #print (gene, exon_num, exon_seq)
            cds_for_this_gene += exon_seq
        #print the cds sequence for this gene
        print(cds_for_this_gene)
                         

def rev_comp(seq):
    return seq.reverse_complement()
    #print(seq)
    #print(seq_revcomp)

def gc(seq):
    seq = seq.upper()
    count_of_G= seq.count('G')
    count_of_C= seq.count('C')

    return (count_of_G + count_of_C/len(seq))
    print(gc_content) #you can check this by comparing to value usin GC calculator online

def main():
    genome=parse_fasta()
    parse_gff(genome)


args  get_args()

if _name_



google how to test for wheter an index exist in a list

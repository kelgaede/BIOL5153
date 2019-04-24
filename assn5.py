#! /usr/bin/env python3

from Bio import SeqIO

# specify the input files
gff_file   = 'watermelon.gff'
fasta_file = 'watermelon.fsa'

#open the fasta file, read it and split the lines using .splitlines to do it at linebreaks and [1:] to skip the header
genome=SeqIO.read(fasta_file, 'fasta')

#the variable genome holds the genome sequence 

#open the gff file
with open(gff_file) as gff:
    #read gff file line by line
    for line in gff:
        #remove line breaks
        line = line.rstrip('\n')
            # split each line on the tab character
            # # sequence, source, feature, begin, end, length, strand, phase, attributes = line.split('\t')
        fields = line.split('\t')
        # print(fields[3], fields[4])
        # extract the DNA sequence from the genome for this feature
        #when I came to your office we had this as coding_seq=genome[fields[3]:fields[4]] but I got an error.
        coding_seq = genome.seq[int(fields[3]):int(fields[4])]
        # print(coding_seq)


        # print the DNA sequence for this feature

        # calculate the GC content for this feature, and print it to the screen
        #first calculate the length of the DNA
        seq_len=len(coding_seq)

        # calculate numbers of A, C, G, T
        numA = coding_seq.count('A')
        numC = coding_seq.count('C')
        numG = coding_seq.count('G')
        numT = coding_seq.count('T')



        #add all G and C
        total_CG = 0
        total_CG = numC + numG
        print(total_CG)

        #calculate GC content

 #       GC_content=total_CG/seq_len


# next step is to use biopython to parse the fasta file to get the genome sequence

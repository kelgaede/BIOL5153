#! /usr/bin/env python3

# specify the input files
gff_file   = 'watermelon.gff'
fasta_file = 'watermelon.fsa'



# open the GFF file
gff = open(gff_file, 'r')

# read GFF file, line by line
for line in gff:
	# skip blank lines

	# remove line breaks
	line = line.rstrip('\n')
	# print(line)
	
	# split each line on the tab character
	# sequence, source, feature, begin, end, length, strand, phase, attributes = line.split('\t')
	fields = line.split('\t')
	print(fields[3], fields[4])

	# extract the DNA sequence from the genome for this feature
	coding_seq =fields[fields3:fields4]

	# print the DNA sequence for this feature


	# calculate the GC content for this feature, and print it to the screen

gff.close()

#open and read the fasta file
fsa_whole=open(fasta_file, 'r').read()

#remove the first two strings from the file
fsa_seq=

#remove any linebreaks
fsa_seq=fsa_seq.rstrip('\n')
#read fsa file, line by line
for lines in fsa:
	

	# split each line on the tab character
	# sequence, source, feature, begin, end, length, strand, phase, attributes = line.split('\t')
	fsa_fields = fsa_lines.split('\t')
	print(fsa_fields[3], fsa_fields[4])

# extract the DNA sequence from the genome for this feature
	substring =

	# print the DNA sequence for this feature


	# calculate the GC content for this feature, and print it to the screen


















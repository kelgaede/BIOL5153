#! /usr/bin/env python3

# specify the input files
gff_file   = 'watermelon.gff'
fasta_file = 'watermelon.fsa'


# open the FASTA file
fasta=open(fasta_file, 'r')

#Solution one to remove the first two lines of .fsa
#sequence=next(fasta_file)
#sequence=fasta_file.read()
#sequence=sequence.rstrip('\n')
#print(len(sequence))


#solution #2
counter=1
for line in fasta_file:
    if line_counter==2
        sequence=line.rstrip('\n')
    line_counter+=1


#solution #3 for his to work you have to read the entire file at once not line by line
fasta_contents=fasta.read()
header=fasta_contents.split('\n')[0]
sequence=fasta_contents.split('\n')[1]
fasta.close()

#solution #4

#to be able to see genome once you are done going throught the loop you have to define the variable outside of the loop. That was the error I was getting.
with open(fasta_file) as fasta:
    file_in_list=fasta.read().splitlines()
    #andys way file_in_list=fasta.splitlines()
genome=file_in_list[1:]
#andys way genome=file_in_list[1]
    


# the variable 'genome' holds the genome sequence
# genome = file_in_list[1]


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
	substring =

	# print the DNA sequence for this feature


	# calculate the GC content for this feature, and print it to the screen


gff.close()



#next step is to use biopython to parse the fasta file to get the genome sequence 



















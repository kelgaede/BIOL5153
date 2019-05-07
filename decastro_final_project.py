#! /usr/bin/env python3

from Bio.Blast import NCBIWWW
import xml.etree.ElementTree as ET

pspAseq='pspAseq.txt'
gene_name='Streptococcus pneumoniae pneumococcal surface protein A'
genome=open("pspA.fasta","w+")

genome.write('>'+gene_name+('\n'))

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
    
#blast pspA
fasta_string = open("pspA.fasta").read()
result_handle = NCBIWWW.qblast("blastn", "nt", fasta_string)

#read results
with open("my_blast.xml", "w") as out_handle:
    out_handle.write(result_handle.read())
    result_handle.close()

#read in the file with ElementTree

tree=ET.parse('/Users/kel/Desktop/bio_programming/my_blast.xml')
root=tree.getroot()

for child in root:
    print(child.tag, child.attrib)
    #to look at the entire file
    # print(ET.tostring(root, encoding='utf8'))
    
#for bit_score in root.findall('./BlastOutput_iterations/Iteration/Hit/Hspbit-score'):
 #   print(bit_score)
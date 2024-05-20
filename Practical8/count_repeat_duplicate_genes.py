import re
import os

#Ask user to input repetitive sequence
repetitive_sequence = input("Please enter the repetitive sequence (GTGTGT or GTCTGT): ").strip().upper()

#Create output filename based on repetitive sequence
output_filename = f"{repetitive_sequence}_duplicate_genes.fa"

#Open the input file for reading
os.chdir("D:\桌面\IBI\IBI1_2023-24\Practical8")
input_file = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa', 'r')

#Open the output file for writing
output_file = open(output_filename, 'w')

#Define variables
gene_name = ''
sequence = ''

#through each line in the input file
for line in input_file:
    line = line.strip()
    if line.startswith(">"):
        #If the sequence contains the repetitive element, write gene info to output file
        if repetitive_sequence in sequence:
            output_file.write(f'>{gene_name} {sequence.count(repetitive_sequence)}\n{sequence}\n\n')  #Add an extra newline between gene name and sequence

        #Update gene name and reset sequence
        gene_name = re.findall(r'gene:(.+)\sgene_biotype', line)[0]
        sequence = ''
    else:
        sequence += line

#Write last gene info to output file
if repetitive_sequence in sequence:
    output_file.write(f'>{gene_name} {sequence.count(repetitive_sequence)}\n{sequence}\n\n')  #Add an extra newline between gene name and sequence

#Close input and output files
input_file.close()
output_file.close()

print(f"Duplicate genes containing {repetitive_sequence} extracted and saved to '{output_filename}'")
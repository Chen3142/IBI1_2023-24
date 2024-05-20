#import library
import re

#set the input and output file
input_file = 'D:\桌面\IBI\IBI1_2023-24\Practical8\Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa'
output_file = 'D:\桌面\IBI\IBI1_2023-24\Practical8\duplicate_genes.fa'

#open the file
with open(input_file, 'r') as input_f, open(output_file, 'w') as output_f:
     # find different sequence 
     for line in input_f:
        if line.startswith(">"):
            if re.search('duplication', line):
              name = re.findall(r'gene:(.+)\sgene_biotype', line) # see if it matches the regular expression
              name = str(name) + '\n'
              output_f.write(name) # write
        else:
            continue
print("Duplicate genes extracted and saved to 'duplicate_genes.fa'")
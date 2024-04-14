import re
input_file = 'D:\桌面\IBI\IBI1_2023-24\Practical8\Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa'
output_file = 'D:\桌面\IBI\IBI1_2023-24\Practical8\duplicate_genes.fa'
with open(input_file, 'r') as input_f, open(output_file, 'w') as output_f:
    gene_name = ''
    sequence = ''
    for line in input_f:
        line = line.rstrip()
        if line.startswith('>'):  
            match = re.search(r'gene:(\S+)', line)
            if match and 'duplication' in line:
                if gene_name:
                    output_f.write(f'>{gene_name}\n{sequence}\n')
                gene_name = match.group(1)
                sequence = ''
        else:
            sequence += line
    if gene_name:
        output_f.write(f'>{gene_name}\n{sequence}\n')
print("Duplicate genes extracted and saved to 'duplicate_genes.fa'")
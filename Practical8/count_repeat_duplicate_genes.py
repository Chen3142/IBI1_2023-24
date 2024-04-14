import re

# Ask user to input repetitive sequence
repetitive_sequence = input("Please enter the repetitive sequence (GTGTGT or GTCTGT): ").strip().upper()

# Create output filename based on repetitive sequence
output_filename = f"{repetitive_sequence}_duplicate_genes.fa"

# Open the input file for reading and the output file for writing
input_file = 'D:\桌面\IBI\IBI1_2023-24\Practical8\Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa'
with open(input_file, 'r') as input_f, open(output_filename, 'w') as output_f:
    gene_name = ''
    sequence = ''

    for line in input_f:
        line = line.strip()

        if line.startswith('>'):
            match = re.search(r'gene:(\S+)', line)
            if match and repetitive_sequence in sequence:
                # Write the previous gene's sequence to the output file
                output_f.write(f'>{gene_name}\n{sequence}\n')

            # Update the gene name and reset the sequence
            gene_name = match.group(1)
            sequence = ''
        else:
            # Append the sequence to the current gene
            sequence += line

    # Write the last gene's sequence to the output file
    if gene_name and repetitive_sequence in sequence:
        output_f.write(f'>{gene_name}\n{sequence}\n')

print(f"Duplicate genes containing {repetitive_sequence} extracted and saved to '{output_filename}'")
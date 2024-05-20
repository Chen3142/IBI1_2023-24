#import libraries
import blosum as bl
import os
import re

# Load the BLOSUM62 matrix
matrix = bl.BLOSUM(62)

# Change the working directory
os.chdir("D:\桌面\IBI\IBI1_2023-24\Practical13")

# open input files
human = open('SLC6A4_HUMAN.fa', 'r')
mouse = open('SLC6A4_MOUSE.fa', 'r')
rat = open('SLC6A4_RAT.fa', 'r')

# Define a function to get the sequence from files
def get_sequence(input_file):
    seq = ""
    for line in input_file:
        if line.startswith(">"):
            continue #Skip header lines
        seq += re.sub(r'\n','', line)  #Remove newline and possible spaces  
    return seq

#apply the function
human_seq = get_sequence(human)
mouse_seq = get_sequence(mouse)
rat_seq = get_sequence(rat)

def compare(seq1, seq2):
    #use BLOSUM62 to compare two sequence
    score = 0 #Set initial score
    #Loop through all points of the sequence
    for i in range(len(seq1)):
        score += matrix[seq1[i]][seq2[i]] #Use BLOSUM62 matrix to get the score and add it to the score.
    print("BLOSUM score:", score)#print the output

    #calculate the Hamming distance
    Hamming_distance = 0  #set initial distance
    #Loop through all points of the amino acid sequence
    for i in range(len(seq1)): 
        if seq1[i] != seq2[i]:
            Hamming_distance += 1  #if amino acids are different, add 1.
    print("percentage identity:", 100 - 100 * Hamming_distance / len(seq1),"%") #print the output

# Results
print("compare SLC6A4_HUMAN with SLC6A4_MOUSE")
compare(human_seq, mouse_seq)
#BLOSUM score: 3137.0
#percentage identity: 92.53968253968254%

print("compare SLC6A4_HUMAN with SLC6A4_RAT")
compare(human_seq, rat_seq)
#BLOSUM score: 3107.0
#percentage identity: 91.74603174603175%

print("compare SLC6A4_MOUSE with SLC6A4_RAT")
compare(mouse_seq, rat_seq)
#BLOSUM score: 3261.0
#percentage identity: 96.82539682539682%
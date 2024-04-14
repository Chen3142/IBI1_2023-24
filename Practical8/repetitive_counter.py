#import the regular expression module
import re

#define the sequence
seq = 'ATGCAATCGGTGTGTCTGTTCTGAGAGGGCCTAA'

#extract the GTGTGT sequence and count
GTGTGT = re.findall(r'GTGTGT',seq)
count_GTGTGT=len(GTGTGT)
print(count_GTGTGT,"repeat(s) of GTGTGT" )

#extract the GTCTGT sequence and count
GTCTGT = re.findall(r'GTCTGT',seq)
count_GTCTGT=len(GTCTGT)
print(count_GTCTGT,"repeat(s) of GTCTGT" )

#count the total number
count= count_GTGTGT+count_GTCTGT
if count>0:
    print ("There are", count,"repeats of GTGTGT and GTCTGT.")
else:
    print("There is no GTGTGT or GTCTGT sequence.")
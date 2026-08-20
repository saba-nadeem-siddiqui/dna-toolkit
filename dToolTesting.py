from DNA_Toolkit import *
import random


rndDNAstr = ''.join([random.choice(Nucleotides)
                     for nuc in range(50)])

DNAStr = validateSeq(rndDNAstr)
print(countNucFrequency(DNAStr))
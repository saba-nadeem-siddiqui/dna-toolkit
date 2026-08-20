import collections 

Nucleotides = ["A", "C", "G", "T"]

# Validate if the given string is a DNA Sequence
def validateSeq(dna_seq):
    tmpseq = dna_seq.upper()
    for nuc in tmpseq:
        if nuc not in Nucleotides:
            return False
    return tmpseq

# Count the number of nucleotides
def countNucFrequency(seq):
    tmpFreqDict = {"A":0, "C":0, "G":0, "T":0}
    for nuc in seq:
        tmpFreqDict[nuc] += 1
    return tmpFreqDict
# Another method:
#   return dict(collections.counter(seq))

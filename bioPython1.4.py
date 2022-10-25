from Bio.Align import substitution_matrices
from Bio import pairwise2

matrix = substitution_matrices.load("BLOSUM62") 

alignments = pairwise2.align.globaldx("KEVLA", "EVL", match_dict=matrix)
for alignment in alignments:
    print(pairwise2.format_alignment(*alignment))
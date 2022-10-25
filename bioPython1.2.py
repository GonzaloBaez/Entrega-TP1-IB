from ctypes import alignment
from Bio import pairwise2

alignments = pairwise2.align.globalmx("ACCGGT", "ACGT", match=2, mismatch=-1) 

for alignment in alignments:
    print(pairwise2.format_alignment(*alignment))
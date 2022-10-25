from ctypes import alignment
from Bio import pairwise2

alignments = pairwise2.align.globalxs("ACCGGT", "ACGT", open=-2, extend=-1)

for alignment in alignments:
    print(pairwise2.format_alignment(*alignment))
from ctypes import alignment
from Bio import pairwise2

alignments = pairwise2.align.globalxx("ACCGGT", "ACGT") 
## De este modo grficamos el alineamiento
for alignment in alignments:
    print(pairwise2.format_alignment(*alignment))
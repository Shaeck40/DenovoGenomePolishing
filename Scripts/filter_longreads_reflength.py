import pysam

in_bam 
out_bam 
min_span = 25000  # alignment span ≥ 25 kbp

with pysam.AlignmentFile(in_bam, "rb") as infile, \
     pysam.AlignmentFile(out_bam, "wb", template=infile) as outfile:

    for read in infile:
        if (not read.is_unmapped and 
            read.reference_length is not None and 
            read.reference_length >= min_span):
            
            outfile.write(read)

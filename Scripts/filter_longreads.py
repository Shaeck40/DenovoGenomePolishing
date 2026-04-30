import pysam

in_bam = input bamfile
out_bam = output bamfile
min_len = 2500  # reads ≥ 2500 bp

with pysam.AlignmentFile(in_bam, "rb") as infile, \
     pysam.AlignmentFile(out_bam, "wb", template=infile) as outfile:

    for read in infile:
        if read.query_length >= min_len:
            outfile.write(read)

import pysam

in_bam = "/mnt/c/Users/Sarah/Documents/Internship/WGS_output/A2_output_lr_OPENPvsOPENP/data/reference.bam"
out_bam = "/mnt/c/Users/Sarah/Documents/Internship/Denovo_genome_polishing/reference_filtered.bam"
min_len = 2500  # reads ≥ 2500 bp

with pysam.AlignmentFile(in_bam, "rb") as infile, \
     pysam.AlignmentFile(out_bam, "wb", template=infile) as outfile:

    for read in infile:
        if read.query_length >= min_len:
            outfile.write(read)

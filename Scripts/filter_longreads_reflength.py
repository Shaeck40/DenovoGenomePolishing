import pysam

in_bam = "/mnt/c/Users/Sarah/Documents/Internship/WGS_output/A2_output_lr_OPENPvsOPENP/data/reference.bam"
out_bam = "/mnt/c/Users/Sarah/Documents/Internship/Denovo_genome_polishing/51kbpins/reference_filtered_reflength.bam"
min_span = 25000  # alignment span ≥ 25 kb

with pysam.AlignmentFile(in_bam, "rb") as infile, \
     pysam.AlignmentFile(out_bam, "wb", template=infile) as outfile:

    for read in infile:
        if (not read.is_unmapped and 
            read.reference_length is not None and 
            read.reference_length >= min_span):
            
            outfile.write(read)
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import csv

def parse_vcf(filename):
    variants = {}
    headers = []
    with open(filename, 'r') as f:
        for line in f:
            if line.startswith('#'):
                headers.append(line)
                continue
            parts = line.strip().split('\t')
            chrom, pos, vid, ref, alt, qual, filt, info = parts[:8]
            variants[(chrom, pos)] = {
                "ref": ref,
                "alt": alt,
                "vid": vid,
                "qual": qual,
                "filt": filt,
                "info": info
            }
    return variants, headers


def compare_vcfs(output_csv="vcf_comparison.csv",
                 unique_vcf1="unique_to_vcf1.vcf",
                 unique_vcf2="unique_to_vcf2.vcf"):
    
    vcf1_path = "/home/sarah/Internship_CMB_VIB/vcf_files/aln_NCBIv2_vs_newCBS.vcf"
    vcf2_path = "/home/sarah/Internship_CMB_VIB/vcf_files/aln_NCBIv2_vs_OPENPichia.vcf"

    vcf1, headers1 = parse_vcf(vcf1_path)
    vcf2, headers2 = parse_vcf(vcf2_path)

    all_positions = set(vcf1.keys()) | set(vcf2.keys())

    # --- CSV OUTPUT ---
    with open(output_csv, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["VARIANT_TYPE", "CHROM", "POS", "REF_A", "ALT_A", "REF_B", "ALT_B", "STATUS"])

        for chrom, pos in sorted(all_positions, key=lambda x: (x[0], int(x[1]))):
            a = vcf1.get((chrom, pos))
            b = vcf2.get((chrom, pos))

            if a and b:
                if (a["ref"], a["alt"]) == (b["ref"], b["alt"]):
                    variant_type = "same_variant"
                    status = "Same_variant"
                else:
                    variant_type = "differ_variant"
                    status = "Differ_in_variant"
                writer.writerow([variant_type, chrom, pos, a["ref"], a["alt"], b["ref"], b["alt"], status])
            elif a:
                variant_type = "only_in_vcf1"
                writer.writerow([variant_type, chrom, pos, a["ref"], a["alt"], "-", "-", "Only in file vcf1"])
            else:
                variant_type = "only_in_vcf2"
                writer.writerow([variant_type, chrom, pos, "-", "-", b["ref"], b["alt"], "Only in file vcf2"])

    # --- VCF OUTPUT: unique to vcf1 ---
    with open(unique_vcf1, 'w') as out1:
        for h in headers1:
            out1.write(h)
        for (chrom, pos), a in vcf1.items():
            if (chrom, pos) not in vcf2:
                line = "\t".join([
                    chrom,
                    pos,
                    a["vid"],
                    a["ref"],
                    a["alt"],
                    a["qual"],
                    a["filt"],
                    "."
                ]) + "\n"
                out1.write(line)

    # --- VCF OUTPUT: unique to vcf2 ---
    with open(unique_vcf2, 'w') as out2:
        for h in headers2:
            out2.write(h)
        for (chrom, pos), b in vcf2.items():
            if (chrom, pos) not in vcf1:
                line = "\t".join([
                    chrom,
                    pos,
                    b["vid"],
                    b["ref"],
                    b["alt"],
                    b["qual"],
                    b["filt"],
                    "."
                ]) + "\n"
                out2.write(line)

    print(f"✅ Comparison completed. Results saved in: {output_csv}")
    print(f"✅ Unique variants (only in vcf1) saved in: {unique_vcf1}")
    print(f"✅ Unique variants (only in vcf2) saved in: {unique_vcf2}")
    print(f"   File 1: {vcf1_path}")
    print(f"   File 2: {vcf2_path}")


if __name__ == "__main__":
    compare_vcfs()

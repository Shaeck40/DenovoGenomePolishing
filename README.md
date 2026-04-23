# Denovo genome polishing

## Overview

This repository contains scripts for:

* VCF comparison between two genome datasets
* BAM filtering based on long-read alignment length

The pipeline is used in genomic variant analysis and genome assembly/polishing workflows.

---

# 1. VCF Comparison Script

## Purpose

Compares two VCF files and identifies:

* Shared variants (same or different)
* Variants unique to each file

---

## Requirements

* Python 3.x

---

## Input

Hardcoded paths:

```python id="v1x9aa"
vcf1_path = "...newCBS.vcf"
vcf2_path = "...OPENPichia.vcf"
```

---

## Method

Variants are stored as:

```
(chromosome, position)
```

Each variant is classified as:

| Type           | Meaning                         |
| -------------- | ------------------------------- |
| same_variant   | identical REF and ALT           |
| differ_variant | same position, different allele |
| only_in_vcf1   | unique to VCF1                  |
| only_in_vcf2   | unique to VCF2                  |

---

## Outputs

### 1. CSV summary

```
vcf_comparison.csv
```

Columns:

```
VARIANT_TYPE, CHROM, POS, REF_A, ALT_A, REF_B, ALT_B, STATUS
```

---

### 2. Unique VCF files

* `unique_to_vcf1.vcf`
* `unique_to_vcf2.vcf`

---

# 2.BAM Filtering Script

## Purpose

Filters BAM files to retain only **long alignments (≥ 25 kb)** for downstream genome analysis.

---

## Requirements

* Python 3.x
* pysam

Install:

```bash id="p2k8lm"
pip install pysam
```

---

## Input / Output

### Input BAM:

```python id="b1m8zx"
reference.bam
```

### Output BAM:

```python id="c8n2qp"
reference_filtered_reflength.bam
```

---

## Filtering Criteria

A read is kept if:

```
- mapped
- reference_length is not None
- reference_length ≥ 25,000 bp
```

---

## Method

* BAM is read using `pysam.AlignmentFile`
* Output BAM uses input as template
* Reads are filtered in streaming mode
* Only valid long alignments are written

---

## Output

Filtered BAM file containing:

* long reads only
* suitable for assembly or polishing workflows

---

## Post-processing

Index the BAM file:

```bash 
samtools index reference_filtered_reflength.bam
```

---

# Notes & Limitations

### VCF script:

* Position-based comparison only
* INFO field not compared
* No multi-allelic handling

### BAM script:

* Uses `reference_length` only (not MAPQ or CIGAR complexity)
* No CLI arguments (paths are hardcoded)

---


# Sarah Haeck


